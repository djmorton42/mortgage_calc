from datetime import datetime
from decimal import Decimal

from parser.ArgumentFileParserFactory import ArgumentFileParserFactory
from CalculationProperties import CalculationProperties
from renderer.ConsoleRenderer import ConsoleRenderer
from renderer.CsvRenderer import CsvRenderer

import sys
import calendar
import argparse
import getopt

def add_month(original_date):
    if original_date.month == 12:
        return original_date.replace(
            year = original_date.year + 1, 
            month = 1)
    else:
        return original_date.replace(
            month = original_date.month + 1)

def retrieve_args():
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-f", "--file", 
        help="A json, yaml or properties file to load calculation settings from. "
        + "All other properties are optional if this is specified. "
        + "Other specified properties will override properties read from the file."
        + "The settings that can be specified in the file are "
        + "initial_payment_date, quoted_rate, monthly_payment, opening_balance, "
        + "number_of_months and months_per_compound_period.")
    argument_parser.add_argument("-d", "--startdate", 
        help="The first payment date (usually 1 month after the mortgage start date) in YYYY-MM-DD format.")
    argument_parser.add_argument("-b", "--balance", 
        help="The initial mortgage balance")
    argument_parser.add_argument("-r", "--rate", 
        help="The annual interest rate")
    argument_parser.add_argument("-p", "--payment", 
        help="The amount being paid montly")
    argument_parser.add_argument("-n", "--months", 
        help="The number of months desired in theamortization table")
    argument_parser.add_argument("-c", "--compound", 
        help="The number of months in a compounding period.  6 for semi-annually, 1 for monthly.")
    argument_parser.add_argument("-ca", "--creepa",
        help="The percentage amount to be added to the quoted interest rate at regular intervals")
    argument_parser.add_argument("-cf", "--creepf",
        help="How often (in months) to apply the -ca argument"),
    argument_parser.add_argument("-o", "--output",
        help="Write the output to a formatted file instead of the console. "
        + "Presently, only csv files are supported.")

    args = vars(argument_parser.parse_args())
    return args, argument_parser    

def create_output_renderer(args):
    if args["output"] is not None:
        outputFileName = args["output"]
        if outputFileName.lower().endswith(".csv"):
            return CsvRenderer(outputFileName)
        else:
            raise NotImplementedError(
                "Only csv files are presently supported")
    else:
        return ConsoleRenderer()

def get_rate_creep_from_args(args):
    creepf = None
    creepa = None

    if args["creepf"] is not None:
        creepf = int(args["creepf"])

    if args["creepa"] is not None:
        creepa = Decimal(args["creepa"]) / 100

    if creepf is not None and creepa is not None:
        return creepf, creepa
    else:
        return None, None

if __name__ == '__main__':
    args, argument_parser = retrieve_args()

    calculator_properties = None
    output_renderer = create_output_renderer(args)

    try:
        if args["file"] is not None:
            print "Loading properties from file " + args["file"]
            calculator_properties = ArgumentFileParserFactory.get_instance(args["file"]).parse()
            calculator_properties.replace_with_args(args)
        else:
            calculator_properties = CalculationProperties.from_args(args)
    except Exception:
        argument_parser.print_help();
        sys.exit();

    calculator_properties.print_properties()
    creep_frequency, creep_amount = get_rate_creep_from_args(args)

    if creep_frequency is not None:
        print("Creep Frequency: " + str(creep_frequency) + " months")

    if creep_amount is not None:
        print("Creep Amount: " + "{0:.2f}%".format(creep_amount * 100))

    effective_annual_interest_rate = calculator_properties.effective_annual_interest_rate
    effective_monthly_interest_rate = calculator_properties.effective_monthly_interest_rate

    print("")

    table = []

    current_date = calculator_properties.start_date
    current_balance = calculator_properties.opening_balance
    for month_index in range(0, calculator_properties.number_of_months):        

        if month_index > 0 and creep_frequency is not None:
            if month_index % creep_frequency == 0:
                calculator_properties.interest_rate += creep_amount
                effective_annual_interest_rate = calculator_properties.effective_annual_interest_rate
                effective_monthly_interest_rate = calculator_properties.effective_monthly_interest_rate

        current_date = add_month(current_date)        
        monthly_interest = effective_monthly_interest_rate * current_balance
        principal_paid = calculator_properties.monthly_payment - monthly_interest
        new_balance = current_balance + monthly_interest - calculator_properties.monthly_payment

        table.append(
            {
                "month_index" : month_index, 
                "current_date" : current_date,
                "interest_rate" : calculator_properties.interest_rate,
                "current_balance" : current_balance,
                "principal_paid" : principal_paid,
                "monthly_interest" : monthly_interest,
                "new_balance" : new_balance
            }
        )
        
        current_balance = new_balance

    output_renderer.render(table)