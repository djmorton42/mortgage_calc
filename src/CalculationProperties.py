from decimal import Decimal
from datetime import datetime

class CalculationProperties(object):
    def __init__(self, start_date, opening_balance, interest_rate, monthly_payment, number_of_months, compounding_months):
        self.start_date = start_date
        self.opening_balance = opening_balance
        self.interest_rate = interest_rate
        self.number_of_months = number_of_months
        self.compounding_months = compounding_months
        self.monthly_payment = monthly_payment

    @property
    def effective_annual_interest_rate(self):
        factor = Decimal("12") / self.compounding_months
        return ((1 + self.interest_rate / factor) ** factor) - 1

    @property
    def effective_monthly_interest_rate(self):
        return ((self.effective_annual_interest_rate + 1) ** (Decimal(1)/12)) - 1

    def replace_with_args(self, args):
        if args["startdate"] != None:
            self.start_date = datetime.strptime(args["startdate"], "%Y-%m-%d")

        if args["balance"] != None:
            self.opening_balance = Decimal(args["balance"])

        if args["rate"] != None:
            self.interest_rate = Decimal(args["rate"]) / 100

        if args["payment"] != None:
            self.monthly_payment = Decimal(args["payment"])
    
        if args["months"] != None:
            self.number_of_months = int(args["months"])

        if args["compound"] != None:
            self.compounding_months = int(args["compound"])

    @staticmethod
    def from_args(args):
        return CalculationProperties(
            datetime.strptime(args["startdate"], "%Y-%m-%d"),
            Decimal(args["balance"]),
            Decimal(args["rate"]) / 100,
            Decimal(args["payment"]),
            int(args["months"]),
            int(args["compound"]))

    def print_properties(self):
        print("First Payment Date: " + str(self.start_date.strftime("%Y-%m-%d")))
        print("Opening Balance: $" + str(self.opening_balance))
        print("Monthly Payment: $" + str(self.monthly_payment))    
        print("Number of Months to display: " + str(self.number_of_months))    
        print("Quoted Interest Rate: " + str(self.interest_rate * 100) + "%")
        print("Compounding every " + str(self.compounding_months) + " months")
        print("Effective Annual Interest Rate: " + str(self.effective_annual_interest_rate * 100) + "%")
        print("Effective Monthly Interest Rate: " + str(self.effective_monthly_interest_rate * 100) + "%")
