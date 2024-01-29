from university_management import Student
from university_management import Gender
from university_management import University
from priority_que import MinPriorityQueue

student_1 = Student(9, ['Calculus'], 0, "Aram", "Mkheyan", 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
student_2 = Student(2, ["CS12423"], 4, 'Nane', "whateveryan", 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
student_3 = Student(2, ["CS^%$^&"], 21, 'Vasak', 'mkrtchyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
student_4 = Student(2, ["CS876567"],3,'Karen', 'manukyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
student_5 = Student(43, ["CS76545678"], 8, 'Khoren','mikaelian', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
student_6 = Student(2, ["CS567y8u"], 9, 'Whatever',  'abdulyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
student_7 = Student(3, ["CSi76543"], 8,'More_Whatever', 'dambulyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
student_8 = Student(5, ["CS654redfghj"], 5,'Even_More_Whateverer', 'daxosyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
student_9 = Student(2345, ["CS34567890"], 4,'No_WOrds_Could_describe_the_usefuleness', 'lazyan',  2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)
student_10 = Student(345, ["CS34567890"], 4,'LASSSSSSTTTTTT_ONEEEEEEEEEEEEEEEEEEEEEEEEEEEE',  'finalyan', 2002, Gender.MALE, "weirdo_weirdoyan_2023@gmail.com", False)

american_univeristy = University("AUA", [], [], [], [], [])

american_univeristy.add_student(student_1)
american_univeristy.add_student(student_2)
american_univeristy.add_student(student_3)
american_univeristy.add_student(student_4)
american_univeristy.add_student(student_5)
american_univeristy.add_student(student_6)
american_univeristy.add_student(student_7)
american_univeristy.add_student(student_8)
american_univeristy.add_student(student_9)
american_univeristy.add_student(student_10)

print("STUDENTS_____________________")
for i in american_univeristy.get_students():
    i.get_description()

print("Adding students to the priority queue")
priority_queue = MinPriorityQueue()
priority_queue._students_queue(student_1)
priority_queue._students_queue(student_2)
priority_queue._students_queue(student_3)
priority_queue._students_queue(student_4)
priority_queue._students_queue(student_5)
priority_queue._students_queue(student_6)
priority_queue._students_queue(student_7)
priority_queue._students_queue(student_8)
priority_queue._students_queue(student_9)
priority_queue._students_queue(student_10)

print("Printing the priority queue")
print(priority_queue)
print("____________________________")

print("Iterating through the queue")

for i in priority_queue:
    print(i._name)

print("____________________________")
print("Iterating using nexts")

my_iterator = iter(priority_queue)
print(next(my_iterator)._name)
print(next(my_iterator)._name)
print(next(my_iterator)._name)
print(next(my_iterator)._name)
print(next(my_iterator)._name)
print(next(my_iterator)._name)
print(next(my_iterator)._name)
print(next(my_iterator)._name)
print(next(my_iterator)._name)
print(next(my_iterator)._name)

print("____________________________")

print("Removing students from the priority queue")

for i in range(priority_queue.size()):
    print(priority_queue.dequeue()._name)

