mortgage_calc
=============

A simple mortgage calculator for creating amortization tables.  Written in Python, by Daniel Morton.

This utility allows you to input a variety of parameters and view a mortgage amortization table for any number of months you wish.  Presently, this only supports a montly payment schedule, but other payment schedules wont be hard to add.

This was written to deal with Canadian Mortgages, so your milleage may vary when dealing with other countries.  Specifically, it is assumed that payment happens monthly, at the end of the period (If you take possesion on the first of the month, you pay on the first of the following month).

Execute the script by running the following command inside the src directory:

python mortgagecalc.py

You can specify many parameters, either through the command line or through a file.

Command Line Arguments:

-d the start date, specified in YYYY-MM-DD format.  Your first payment will be assumed to be one month later.
-b the balance at the inception of the mortgage
-r the quoted annual interest rate
-p the montly payment you expect to make
-n the number of months you wish to display in the table
-c the number of months in each compounding period (6 for semi-annually, 1 for montly, for example)

In Canada, for fixed rate mortgages, use 6 for the number of months in each compounding period.  For variable rate mortgages, use 1 (monthly).

In addition to the command line arguments, you may also specify these properties in JSON, YAML or Property files.  You pass the filename to use with the -f parameter.  If you also include any other command line parameters, the values passed on the command line will override the values in the file.  Below are examples of each:

JSON Example:

{
    "initial_payment_date" : "2014-11-01",
    "quoted_rate" : 4.05,
    "monthly_payment" : 900.00,
    "opening_balance" : 200000.00,
    "number_of_months" : 60,
    "months_per_compound_period" : 6
}

YAML Example:

initial_payment_date : 2014-11-01
quoted_rate : 4.05
monthly_payment : 900.00
opening_balance : 200000.00
number_of_months : 60
months_per_compound_period : 6

Properties Example:

initial_payment_date=2014-11-01
quoted_rate=4.05
monthly_payment=900.00
opening_balance=200000.00
number_of_months=60
months_per_compound_period=6

Note that the files must end in either .json, .yaml or .properties to be handled by the calculator.
