from ArgumentFileParser import ArgumentFileParser
from CalculationProperties import CalculationProperties
from datetime import datetime
from decimal import Decimal
import json

class JsonArgumentFileParser(ArgumentFileParser):
    def __init__(self, filename):
        super(JsonArgumentFileParser, self).__init__(filename)

    def parse(self):
        handle = None

        try :
            handle = open(self.filename, "r")
            jsonProperties = json.load(handle, parse_float=Decimal)
            
            return CalculationProperties(
                 datetime.strptime(
                    jsonProperties["initial_payment_date"], "%Y-%m-%d"), 
                 Decimal(jsonProperties["opening_balance"]), 
                 Decimal(jsonProperties["quoted_rate"]) / 100, 
                 Decimal(jsonProperties["monthly_payment"]), 
                 int(jsonProperties["number_of_months"]),
                 int(jsonProperties["months_per_compound_period"]))

        finally:
            if handle != None:
                handle.close()        