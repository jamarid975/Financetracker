from tkinter import *
import functions

class Gui:
    def __init__(self, window):
        self.window = window

        #Income
        self.frame_income = Frame(self.window)
        self.input_income = Entry(self.frame_income, width=20)
        self.label_income = Label(self.frame_income, text='Income')
        self.label_income.pack(side='left')
        self.input_income.pack(padx=5, side='left')
        self.frame_income.pack(anchor='w', padx=10, pady=10)

        # Bills
        self.frame_bills = Frame(self.window)
        self.input_bills  = Entry(self.frame_bills, width=20)
        self.label_bills = Label(self.frame_bills, text='Bills')
        self.label_bills.pack(side='left')
        self.input_bills.pack(padx=20, side='left')
        self.frame_bills.pack(anchor='w', padx=10, pady=10)

        #Savings
        self.frame_savings = Frame(self.window)
        self.input_savings = Entry(self.frame_savings, width=20)
        self.label_savings = Label(self.frame_savings, text='Savings')
        self.label_savings.pack(side='left')
        self.input_savings.pack(padx=20, side='left')
        self.frame_savings.pack(anchor='w', padx=10, pady=10)

        #Spending
        self.frame_spending = Frame(self.window)
        self.input_spending = Entry(self.frame_spending, width=20)
        self.label_spending = Label(self.frame_spending, text='Spending')
        self.label_spending.pack(side='left')
        self.input_spending.pack(padx=20, side='left')
        self.frame_spending.pack(anchor='w', padx=10, pady=10)

        # enter button
        self.frame_enter = Frame(self.window)
        self.button_enter = Button(self.frame_enter, text="SAVE", command=self.submit)
        self.button_enter.pack()
        self.frame_enter.pack()

        # bottom lable
        self.frame_bottomtext = Frame(self.window)
        self.lable_bottomtext = Label(self.frame_bottomtext, text="Please fill out all values for this month's spending")
        self.lable_bottomtext.pack()
        self.frame_bottomtext.pack()

    def submit(self):
        try:
            income = self.input_income.get().strip()
            bills = self.input_bills.get().strip()
            savings = self.input_savings.get().strip()
            spending = self.input_spending.get().strip()

            self.lable_bottomtext.config(text=f'This month you {functions.Calc(income,bills,savings,spending)}')
        except TypeError:
            self.lable_bottomtext.config("Values must be greater than or equal to 0 ")




