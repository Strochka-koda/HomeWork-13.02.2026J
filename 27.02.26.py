from abc import ABC, abstractmethod

class Employee(ABC):
    def init(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    def display_info(self):
        print(f"ID: {self.employee_id} | Сотрудник: {self.name}", end=" | ")

class FullTimeEmployee(Employee):
    def init(self, name, employee_id, monthly_salary):
        super().init(name, employee_id)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class ContractEmployee(Employee):
    def init(self, name, employee_id, hourly_rate, hours_worked):
        super().init(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

    def init(self, name, employee_id, salary):
        super().init(name, employee_id)
        self.salary = salary

    def calculate_salary(self):
        return self.salary - 5000
