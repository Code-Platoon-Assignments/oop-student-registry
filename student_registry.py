class Student:
    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def get_name(self):
        return self._name

    @get_name.setter
    def set_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3 and new_name.isalpha():
            self._name = new_name.title()
        else:
            print("Invalid name format.")

    @property
    def get_age(self):
        return self._age

    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and 11 < new_age < 18:
            self._age = new_age
        else:
            print("Invalid age value.")

    @property
    def get_grade(self):
        return self._grade

    @get_grade.setter
    def set_grade(self, new_grade):
        valid_grades = ["9th", "10th", "11th", "12th"]
        if isinstance(new_grade, str) and new_grade in valid_grades:
            self._grade = new_grade
        else:
            print("Invalid grade value.")

    def __str__(self):
        return f"Student 1: Name: {self.get_name}, Age: {self.get_age}, Grade: {self.get_grade}"

    def advance(self, years_advanced=1):
        self.set_grade = f"{int(self.get_grade[0]) + years_advanced}th"
        print(f"{self.get_name} has advanced to the {self.get_grade} grade.")

    def study(self, subject):
        print(f"{self.get_name} is studying {subject}")


