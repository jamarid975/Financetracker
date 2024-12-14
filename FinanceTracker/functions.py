import csv

class Calc:
    OVERSPENT = 'Overspent'
    UNDERSPENT = 'Underspent'

    def __init__(self,income, bills, savings, spending):
        self.__income = income
        self.__bills = bills
        self.__savings = savings  #initialize
        self.__spending = spending
        self.__message = ''
        self.__total_spending = 0
        self.__new_row = []
        self.budget()

    def budget(self):
        try:
            self.__income = float(self.__income)
            self.__bills = float(self.__bills)
            self.__savings = float(self.__savings)   # sets variables to floats
            self.__spending = float(self.__spending)
            if self.__income >= 0 and self.__spending >=0 and self.__savings >= 0 and self.__bills >=0:
                self.__total_spending = float(self.__bills + self.__savings + self.__spending)
                if self.__total_spending >= self.__income:
                    self.__message = Calc.OVERSPENT
                    return self.append_database()   #compares total spending to income
                else:
                    self.__message = Calc.UNDERSPENT
                    return self.append_database()
            else:
                raise TypeError
        except TypeError:
            raise TypeError("Values must be greater than or equal to 0 ")

    def append_database(self):
        file_path = 'spending.csv'
        with open(file_path, 'a', newline='') as file:
            new_content = csv.writer(file)          # appends new list to file
            new_content.writerow(self.new_row())


    def new_row(self):
        self.__new_row.append(self.__income)
        self.__new_row.append(self.__bills)
        self.__new_row.append(self.__savings)       #creates new list for file
        self.__new_row.append(self.__spending)
        self.__new_row.append(self.__message)
        return self.__new_row


    def __str__(self):
        return f"{self.__message}"

