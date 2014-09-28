from ArgumentFileParser import ArgumentFileParser
from CalculationProperties import CalculationProperties
from datetime import datetime
from decimal import Decimal

import re

class YamlArgumentFileParser(ArgumentFileParser):
    def __init__(self, filename):
        super(YamlArgumentFileParser, self).__init__(filename)

    def parse(self):
        handle = None

        try :
            handle = open(self.filename, "r")
            lines = handle.readlines()

            start_date = None
            opening_balance = None
            interest_rate = None
            number_of_months = None
            compounding_months = None
            monthly_payment = None

            for line in lines:
                search_result = re.search("^(.*?):(.*?)$", line)

                label = search_result.group(1).strip()
                value = search_result.group(2).strip()
                if label == "initial_payment_date":
                    start_date = datetime.strptime(value, "%Y-%m-%d")
                elif label == "opening_balance":
                    opening_balance = Decimal(value)
                elif label == "quoted_rate":
                    interest_rate = Decimal(value) / 100
                elif label == "monthly_payment":
                    monthly_payment = Decimal(value)
                elif label == "number_of_months":
                    number_of_months = int(value)
                elif label == "months_per_compound_period":
                    compounding_months = int(value)

            return CalculationProperties(
                start_date, 
                opening_balance, 
                interest_rate, 
                monthly_payment, 
                number_of_months, 
                compounding_months)

        finally:
            if handle is not None:
                handle.close()