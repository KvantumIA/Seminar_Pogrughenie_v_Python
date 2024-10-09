import doctest


class Person:

    def __init__(self, last_name: str, first_name: str, patronymic: str,
                 age: int):
        self.last_name = last_name.title()
        self.first_name = first_name.title()
        self.patronymic = patronymic.title()
        self._age = age

    def full_name(self):
        """
        Returns the full name of the person.

        >>> person = Person("ivanov", "ivan", "ivanovich", 30)
        >>> person.full_name()
        'Ivanov Ivan Ivanovich'
        """
        return f'{self.last_name} {self.first_name} {self.patronymic}'

    def birthday(self):
        """
        Adds 1 year to the person's age.

        >>> person = Person("ivanov", "ivan", "ivanovich", 30)
        >>> person.birthday()
        >>> person.get_age()
        31
        """
        self._age += 1

    def get_age(self):
        return self._age


class Employee(Person):

    def __init__(self, last_name: str, first_name: str, patronymic: str,
                 age: int, position: str, salary: float):
        super().__init__(last_name, first_name, patronymic, age)
        self.position = position.title()
        self.salary = salary

    def raise_salary(self, percent: float):
        self.salary *= (1 + percent / 100)

    def __str__(self):
        """
        Returns a string representation of the employee.

        >>> employee = Employee("ivanov", "ivan", "ivanovich", 30, "manager", 50000)
        >>> str(employee)
        'Ivanov Ivan Ivanovich (Manager)'
        """
        return f'{self.full_name()} ({self.position})'

    def last_name(self):
        """
        Returns the last name of the Employee in title case.

        >>> employee = Employee("ivanov", "ivan", "ivanovich", 30, "manager", 50000)
        >>> employee.last_name
        'Ivanov'
        """
        return self.last_name


def test_employee_raise_salary():
    """
    Testing the raise_salary method of the Employee class.

       >>> emp = Employee("ivanov", "ivan", "ivanovich", 30, "manager", 50000)
        >>> emp.raise_salary(10)
        >>> emp.salary
        55000.0
    """
    pass


if __name__ == '__main__':
    __file__ = None
    doctest.testmod()
