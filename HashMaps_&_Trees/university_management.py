from abc import ABC, abstractmethod
from enum import Enum
from datetime import date


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"


class Person(ABC):
    __max_parking_lots: int = 50
    __used_parking_lots: int = 0

    def __init__(self, _id: int, _name: str, _surname: str, _birth_year: int, _gender: Gender, _email: str,
                 _has_parking_lot=False):
        self._id: int = _id
        self._name: str = _name
        self._surname: str = _surname
        self._birth_year: int = _birth_year
        self._gender: Gender = _gender
        self._email: str = _email
        self._has_parking_lot: bool = _has_parking_lot

    def book_parking_lot(self) -> None:
        self._has_parking_lot = True
        self.__class__.__used_parking_lots += 1

    @abstractmethod
    def get_description(self):
        pass

    @property
    def get_age(self) -> int:
        return date.today().year - self._birth_year

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _name: str):
        self._name = _name

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, _surname: str):
        self._surname = _surname

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, _gender: Gender):
        self._gender = _gender

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, _email: str):
        self._email = _email

    @property
    def has_parking_lot(self):
        return self._has_parking_lot

    @has_parking_lot.setter
    def has_parking_lot(self, _has_parking_lot: bool):
        self._has_parking_lot = _has_parking_lot

    @classmethod
    def get_available_parking_lots(cls) -> int:
        return cls.__max_parking_lots - cls.__used_parking_lots


class Faculty(Person):
    def __init__(self, _department: str, _courses_taught: list,
                 __salary: float, _id: int, _name: str, _surname: str,
                 _birth_year: int, _gender: Gender, _email: str, _has_parking_lot: bool):

        super().__init__(_id, _name, _surname, _birth_year, _gender, _email, _has_parking_lot)
        self._department: str = _department
        self._courses_taught: list = _courses_taught
        self.__salary: float = __salary

    def teach(self, course: str) -> None:
        found = False
        for course_names in self._courses_taught:
            if course_names == course:
                print(f"{self._name} teaches the course {course}")
                found = True
        if not found:
            print(f"{self._name} does not teach the course {course}")

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, _department: str):
        self._department = _department

    @property
    def courses_taught(self):
        return self._courses_taught

    @courses_taught.setter
    def courses_taught(self, _courses_taught: list):
        self._courses_taught = _courses_taught

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, __salary: float):
        self.__salary = __salary

    def get_description(self):
        print(f"This is the description of the Faculty member {self.name} {self.surname}")


class Executive:
    @abstractmethod
    def define_budget(self) -> int:
        pass

    @abstractmethod
    def get_direct_reports(self) -> list:
        pass

    @abstractmethod
    def hire_faculty_member(self, faculty: Faculty) -> bool:
        pass

    @abstractmethod
    def fire_faculty_member(self, faculty: Faculty) -> bool:
        pass


class Dean(Faculty, Executive):
    def __init__(self, _direct_reports: list, _department: str, _courses_taught: list,
                 __salary: float, _id: int, _name: str, _surname: str,
                 _birth_year: int, _gender: Gender, _email: str, _has_parking_lot: bool):
        super().__init__(_department, _courses_taught, __salary, _id, _name, _surname,
                         _birth_year, _gender, _email, _has_parking_lot)
        self._direct_reports: list = _direct_reports

    def get_description(self):
        print(f"This is the description of the Dean {self.name} {self.surname}")

    @property
    # Instructions unclear... how can I implement this function for dean if it is meant for the university
    def define_budget(self) -> int:
        faculty_salary = 0
        for i in self._direct_reports:
            faculty_salary += int(i.__salary)
        return int(self.__salary) + faculty_salary

    @property
    def get_direct_reports(self) -> list:
        return self._direct_reports

    # Unclear Instructions, why would it return a boolean?
    def hire_faculty_member(self, faculty: Faculty) -> bool:
        return True if self._direct_reports.append(faculty) else False

    # Unclear Instructions, why would it return a boolean?
    def fire_faculty_member(self, faculty: Faculty) -> bool:
        return True if self._direct_reports.remove(faculty) else False


class Student(Person):
    def __init__(self, _grade: int, _courses_enrolled: list, _id: int, _name: str, _surname: str,
                 _birth_year: int, _gender: Gender, _email: str, _has_parking_lot: bool):
        super().__init__(_id, _name, _surname, _birth_year, _gender, _email, _has_parking_lot)
        self._grade: int = _grade
        self._courses_enrolled: list = _courses_enrolled

    def enroll(self, course) -> None:
        self._courses_enrolled.append(course)

    def get_courses_taken(self) -> list:
        return self._courses_enrolled

    def get_description(self):
        print(f"This is the description of the Student {self.name} {self.surname}")

    # Compare by students by their name and surname
    def __eq__(self, other):
        return self.name == other.name and self.surname == other.surname

    def __lt__(self, other):
        if self.name == other.name:
            return self.surname < other.surname
        return self.name < other.name

    def __gt__(self, other):
        if self.name == other.name:
            return self.surname > other.surname
        return self.name > other.name

    def __le__(self, other):
        if self.name == other.name:
            return self.surname <= other.surname
        return self.name <= other.name

    def __ge__(self, other):
        if self.name == other.name:
            return self.surname >= other.surname
        return self.name >= other.name

    def __ne__(self, other):
        if self.name == other.name:
            return self.surname != other.surname
        return self.name != other.name

class Course:
    def __init__(self, _code: str, _name: str):
        self._code: str = _code
        self._name: str = _name

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, _new_code):
        self._code = _new_code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, _new_name):
        self._name = _new_name


class University:
    def __init__(self, _name: str, _executives: list, _courses: list, _students: list, _faculty: list, _members: list):
        self._name: str = _name
        self._executives: list = _executives
        self._courses: list = _courses
        self._students: list = _students
        self._faculty: list = _faculty
        self._members: list = _members

    def get_executives(self):
        return self._executives

    def add_executive(self, executive) -> None:
        self._executives.append(executive)

    def remove_executive(self, executive) -> None:
        self._executives.remove(executive)

    def get_courses(self):
        return self._courses

    def add_course(self, course) -> None:
        self._courses.append(course)

    def remove_course(self, course) -> None:
        self._courses.remove(course)

    def get_students(self):
        return self._students

    def add_student(self, student) -> None:
        self._students.append(student)

    def remove_student(self, student) -> None:
        self._students.remove(student)

    def get_faculty(self):
        return self._faculty

    def add_faculty(self, faculty) -> None:
        self._faculty.append(faculty)

    def remove_faculty(self, faculty) -> None:
        self._faculty.remove(faculty)

    def get_member(self):
        return self._members

    def add_member(self, member) -> None:
        self._members.append(member)

    def remove_member(self, member) -> None:
        self._members.remove(member)
