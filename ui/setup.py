from tkinter import *
from tkinter import ttk


class TaskManagerInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title("Task Manager")
        self.window.config(padx=100, pady=100)
        self.employees = []

        # Labels
        self.monday = Label(text="Monday XX")
        self.monday.grid(column=1, row=1, sticky="nsew")
        self.tuesday = Label(text="Tuesday XX")
        self.tuesday.grid(column=2, row=1, sticky="nsew")
        self.wednesday = Label(text="Wednesday XX")
        self.wednesday.grid(column=3, row=1, sticky="nsew")
        self.thursday = Label(text="Thursday XX")
        self.thursday.grid(column=4, row=1, sticky="nsew")
        self.friday = Label(text="Friday XX")
        self.friday.grid(column=5, row=1, sticky="nsew")
        self.saturday = Label(text="Saturday XX")
        self.saturday.grid(column=6, row=1, sticky="nsew")
        self.sunday = Label(text="Sunday XX")
        self.sunday.grid(column=7, row=1, sticky="nsew")

        self.get_employee()

        for item in self.employees:
            for key in item:
                print(key['Employe ID'])
                self.employee_name = Label(text=key['Employe ID'])
                # self.employee_name.grid(column=0, row=self.employees[item], sticky="nsew")

        # Combobox
        self.combobox = ttk.Combobox(self.window, width=10)
        self.combobox['values'] = ("ES", "LATAM")
        self.combobox.grid(column=0, row=1, sticky="nsew")

        self.window.mainloop()

    def get_employee(self):
        self.employees.append(employees_data())
