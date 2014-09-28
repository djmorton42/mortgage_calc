import locale

from OutputRenderer import OutputRenderer

class ConsoleRenderer(OutputRenderer):
    def __init__(self):
        super(ConsoleRenderer, self).__init__()

    def render(self, table):
        for row in table:
            if row["month_index"] % 12 == 0:
                print("")
                self.__print_header();

            self.__print_row(row)
        
    def __print_header(self):
        print("Month #  Date        Rate %  " 
            + "Start Balance  Principal  Interest  End Balance")

    def __print_row(self, row):
        self.__print_formatted_line(
            row["month_index"],
            row["current_date"],
            row["interest_rate"],
            row["current_balance"],
            row["principal_paid"],
            row["monthly_interest"],
            row["new_balance"]
        )

    def __print_formatted_line(self, month_index, current_date, rate, 
        current_balance, principal_paid, monthly_interest, new_balance):
        print(str(month_index + 1).rjust(3, " ") 
            + "      "
            + current_date.strftime("%Y-%m-%d")
            + "  "
            + "{0:.2f}%".format(rate * 100).rjust(6, " ")
            + "  "
            + locale.currency(current_balance).rjust(13, " ")
            + "  "
            + locale.currency(principal_paid).rjust(9, " ")
            + "  "
            + locale.currency(monthly_interest).rjust(8, " ")
            + "  "
            + locale.currency(new_balance).rjust(11, " ")
            )
