class Student:
    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3 and new_name.isalpha():
            self._name = new_name.title()
        else:
            print("Invalid name format.")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int) and 11 < new_age < 18:
            self._age = new_age
        else:
            print("Invalid age value.")

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, new_grade):
        valid_grades = ["9th", "10th", "11th", "12th"]
        if isinstance(new_grade, str) and new_grade in valid_grades:
            self._grade = new_grade
        else:
            print("Invalid grade value.")

    def __str__(self):
        return f"Student 1: Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def advance(self, years_advanced=1):
        self.grade = f"{int(self.grade[0]) + years_advanced}th"
        print(f"{self.name} has advanced to the {self.grade} grade.")

    def study(self, subject):
        print(f"{self.name} is studying {subject}")


