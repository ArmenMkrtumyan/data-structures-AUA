from hash_set import HashSet
from hash_map import HashMap
from hash_map import hash_iterator
import university_management

# print("Printing hash_set")
# my_hashset = HashSet()
#
# my_hashset.add("hello")
# my_hashset.add("something")
# my_hashset.add("something else")
# my_hashset.add("somethinggggggggggg")
# my_hashset.add("alividerchi")
# my_hashset.add("adiossss")
# my_hashset.add("HAPPY NEW YEAR")
#
# print(my_hashset)
# #
# print("Checking Contains method")
# print("Does it contain hello?: ", my_hashset.contains("hello"))
# print("Does it contain hellllllllllll?: ", my_hashset.contains("hellllllllllll"))
#
# print("Checking Remove method")
# print("Removing somethinggggggggggg")
# my_hashset.remove("somethinggggggggggg")
# print(my_hashset)
#
# print("Checking remove at method")
# print("Removing something")
# my_hashset.remove_element_at(0)
# print(my_hashset)
#
# print("Checking remove after method")
# print("Removing something")
# my_hashset.remove_after("something")
# print(my_hashset)
# print("_____________________________________________")

# print("Printing hash_map")
# my_hashmap = HashMap()
#
# my_hashmap.put(0, "testing")
# my_hashmap.put(1, "hello")
# my_hashmap.put(2, "something")
# my_hashmap.put(2, "what if I add this")
# my_hashmap.put(21, "somethinggggggggggg")
# my_hashmap.put(3, "something else")
# my_hashmap.put(5, "alividerchi")
#
# print(my_hashmap)
# #
# print("Checking get method")
#
# print("Getting value of key 1: ", my_hashmap.get(1))
# print("Getting value of key 2: ", my_hashmap.get(2))
#
# print("Checking remove method")
# print("Removing key 2")
# my_hashmap.remove(2)
# print(my_hashmap)

# print("Checking iterator method")
# print("Printing keys and values")
# print("Using next method")
# my_iterator = my_hashmap.__iter__()
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
#
# print("Using for loop")
# for i in my_hashmap:
#     print(i)

# print("_____________________________________________")
#
# print("Checking hash_set iterator")
# print("using next method")
# my_iterator = my_hashset.hash_set_iterator(2)
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# # print(next(my_iterator)) # ԳԳՄՓ
# print("using for loop")
# for i in my_hashset:
#     print(i)

# print("_____________________________________________")

print("Implementing university managment system with hash maps")

student_1 = university_management.Student(9, ['Calculus'], 0, 'weirdo',
                                          'weirdoyan', 2002, university_management.Gender.MALE,
                                          "weirdo_weirdoyan_2023@gmail.com", False)

student_2 = university_management.Student(10, ['Discrete Math'], 0, 'WHATEVER',
                                          "WHATEVERYAN", 2023, university_management.Gender.FEMALE,
                                          "some_mail@gmail.com", True)
student_3 = university_management.Student(9, ['Calculus'], 0, 'AOJSDIIJASDO',
                                          'weirdoyan', 2002, university_management.Gender.MALE,
                                          "weirdo_weirdoyan_2023@gmail.com", False)

student_4 = university_management.Student(10, ['Discrete Math'], 0, 'ASDJIOAOSIDJMASOKMDLKM',
                                          "WHATEVERYAN", 2023, university_management.Gender.FEMALE,
                                          "some_mail@gmail.com", True)

mentor_1 = university_management.Student(9, ['Course 1'], 10, 'MENTOR_1',
                                          'MENTOR_1_yan', 2002, university_management.Gender.MALE,
                                          "weirdo_weirdoyan_2023@gmail.com", False)
mentor_2 = university_management.Student(9, ['Course 2'], 20, 'MENTOR_2',
                                          'MENTOR_2_yan', 2002, university_management.Gender.MALE,
                                          "weirdo_weirdoyan_2023@gmail.com", False)
mentor_3 = university_management.Student(9, ['Course 3'], 30, 'MENTOR_3',
                                          'MENTOR_3_yan', 2002, university_management.Gender.MALE,
                                          "weirdo_weirdoyan_2023@gmail.com", False)
mentor_4 = university_management.Student(9, ['Course 4'], 40, 'MENTOR_4',
                                          'MENTOR_4_yan', 2002, university_management.Gender.MALE,
                                          "weirdo_weirdoyan_2023@gmail.com", False)


faculty_1 = university_management.Faculty('CS', ['Linear Algebra', 'Probability'],
                                          450000, 1, 'George', 'Orwell', 1984,
                                          university_management.Gender.MALE,
                                          "he_had_bad_relations_with_his_wife@gmail.com",
                                          True)

dean_1 = university_management.Dean([faculty_1], 'CS', ['Data Structures'],
                                    1000000, 2, 'Paruyr', "Sevak", 1924,
                                    university_management.Gender.MALE, "Anlreli_Zangakatun", True)

course_1 = university_management.Course('000', 'Calculus')

university_1 = university_management.University("EPH", [dean_1],
                                                ['Calculus', 'Linear Algebra', 'Probability', 'Data Structures'],
                                                [student_1], [faculty_1],
                                                [student_1, faculty_1, dean_1])

dean_2 = university_management.Dean([faculty_1], 'EC', ['ENGLISH 101'],
                                    100000, 5, 'Anahit', "mmyan", 2222,
                                    university_management.Gender.FEMALE, "THISTAKESTOOOLONGGGGG", True)

university_1.add_faculty(dean_2)
university_1.add_student(student_2)
university_1.add_course(course_1)
university_1.add_student(student_3)
university_1.add_student(student_4)

print("STUDENTS_____________________")
for i in university_1.get_students():
    i.get_description()
# print("MEMBERS______________________")
# for i in university_1.get_member():
#     i.get_description()


university_1.enable_mentorship(mentor_1, student_1)
university_1.enable_mentorship(mentor_1, student_2)
university_1.enable_mentorship(mentor_1, student_3)
university_1.enable_mentorship(mentor_1, student_2)
university_1.enable_mentorship(mentor_2, student_2)
university_1.enable_mentorship(mentor_3, student_4)
university_1.enable_mentorship(mentor_4, student_2)
university_1.enable_mentorship(mentor_4, student_2)
university_1.enable_mentorship(mentor_4, student_2)
university_1.enable_mentorship(mentor_4, student_2)
university_1.enable_mentorship(mentor_4, student_2)
university_1.enable_mentorship(mentor_4, student_2)

print(f"Checking the mentor name for the student called {student_2.name}")
print("Mentor: ", university_1.get_mentor(student_2))
print(f"Checking the mentor name for the student called {student_1.name}")
print("Mentor: ", university_1.get_mentor(student_1))
print(f"Checking the mentor name for the student called {student_4.name}")
print("Mentor: ", university_1.get_mentor(student_4))