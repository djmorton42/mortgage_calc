import locale

from OutputRenderer import OutputRenderer

class CsvRenderer(OutputRenderer):
    def __init__(self, filename):
        super(CsvRenderer, self).__init__()
        self.filename = filename

    def render(self, table):
        file_handle = None

        try:
            file_handle = open(self.filename, "w")
            self.__print_header(file_handle);
            for row in table:
                self.__print_row(row, file_handle)

        finally:
            if file_handle is not None:
                file_handle.close()

        
    def __print_header(self, file_handle):
        field_headers = [
            "Month #", 
            "Date", 
            "Rate %", 
            "Start Balance",
            "Principal", 
            "Interest", 
            "End Balance"]

        file_handle.write(",".join([self.__quote_string_if_necessary(header) for header in field_headers]) + "\n")

    def __quote_string_if_necessary(self, string):
        if self.__contains(string, " \t"):
            return "\"" + string + "\""
        else:
            return string
    
    def __contains(self, string, set):
        return 1 in [c in string for c in set]

    def __print_row(self, row, file_handle):
        self.__print_formatted_line(
            file_handle,
            row["month_index"],
            row["current_date"],
            row["interest_rate"],
            row["current_balance"],
            row["principal_paid"],
            row["monthly_interest"],
            row["new_balance"]
        )

    def __print_formatted_line(self, file_handle, month_index, current_date, rate, 
        current_balance, principal_paid, monthly_interest, new_balance):
        file_handle.write(
            str(month_index + 1) 
            + ","
            + current_date.strftime("%Y-%m-%d")
            + ","
            + "{0:.2f}%".format(rate * 100)
            + ","
            + "{0:.2f}".format(current_balance)
            + ","
            + "{0:.2f}".format(principal_paid)
            + ","
            + "{0:.2f}".format(monthly_interest)
            + ","
            + "{0:.2f}".format(new_balance)
            + "\n"
            )        