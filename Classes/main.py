import university_management

student_1 = university_management.Student(9, ['Calculus'], 0, 'weirdo',
                                          'weirdoyan', 2002, university_management.Gender.MALE,
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
print("FACULTY______________________")
for i in university_1.get_faculty():
    i.get_description()
print("STUDENTS_____________________")
for i in university_1.get_students():
    i.get_description()
print("MEMBERS______________________")
for i in university_1.get_member():
    i.get_description()

print("DELETING A STUDENT")
university_1.remove_student(student_1)
print("STUDENTS AFTER REMOVAL________")
for i in university_1.get_students():
    i.get_description()
print("WE JUST ONLY HAD 1 student AND IM TOO LAZY TO CREATE ONE MORE, SO THIS IS GETS US NOTHING")

print("COURSES OF FACULTY1")
print(faculty_1.courses_taught)

print("AND SO ON AND SO FORTH..........")