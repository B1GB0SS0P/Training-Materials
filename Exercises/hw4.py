"""
All texts written in quotations are instructions and examples for you to use. Do not edit them.

Write your code in the functions given below and return the necessary values.

Uncomment out the test cases to test if your function returns the right values.
Comment it back when moving on to the next question
"""

# QUESTION 1
class Wallet:
    """
    A wallet that stores cash and cards.

    >>> w = Wallet(0, [])
    >>> w.pay(1)
    'Insufficient cash. Requires $1 more.'
    >>> w.top_up(10)
    >>> w.pay(5)
    'Balance: $5'
    >>> w.pay(7)
    'Insufficient cash. Requires $2 more.'
    >>> w.display_cards()
    >>> w.add_card("IC")
    >>> w.display_cards()
    'IC'
    >>> w.add_card("11B")
    >>> w.add_card("Debit")
    >>> w.add_card("Credit")
    >>> w.add_card("Timezone")
    >>> w.display_cards()
    '11B'
    'Credit'
    'Debit'
    'IC'
    'Timezone'

    """

    "*** YOUR CODE HERE ***"
    return


w = Wallet(0, [])
print(w.pay(1))
w.top_up(10)
print(w.pay(5))
print(w.pay(7))
w.display_cards()
w.add_card("IC")
w.display_cards()
w.add_card("11B")
w.add_card("Debit")
w.add_card("Credit")
w.add_card("Timezone")
w.display_cards()
print()



# QUESTION 2
class Taxi:
    """
    A taxi that can carry passengers.

    >>> t = Taxi(4, 0, 1)
    >>> t.get_status()
    'Open'
    >>> t.book()
    >>> t.get_status()
    'Booked'
    >>> t.board(5)
    'Exceeding maximum capacity. Please get out.'
    >>> t.board(4)
    'Starting trip. Metre running.'
    >>> t.get_status()
    'Hired'
    >>> t.travel(1)
    >>> t.travel(1)
    >>> t.travel(2)
    >>> t.payment()
    'Total amount to pay: $5'
    >>> t.get_status()
    'Open'

    """

    "*** YOUR CODE HERE ***"
    return

t = Taxi(4, 0, 1)
print(t.get_status())
t.book()
print(t.get_status())
t.board(5)
t.board(4)
print(t.get_status())
t.travel(1)
t.travel(1)
t.travel(2)
print(t.payment())
print(t.get_status())
print()



# QUESTION 3
class VendingMachine:
    """
    A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'Please add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'Please add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    
    """

    "*** YOUR CODE HERE ***"
    return
            


v = VendingMachine('candy', 10)
print(v.vend())
print(v.add_funds(15))
print(v.restock(2))
print(v.vend())
print(v.add_funds(7))
print(v.vend())
print(v.add_funds(5))
print(v.vend())
print(v.add_funds(10))
print(v.vend())
print(v.add_funds(15))
print()

w = VendingMachine('soda', 2)
print(w.restock(3))
print(w.restock(3))
print(w.add_funds(2))
print(w.vend())
print()



# QUESTION 4
class ShoppingCart:
    """
    A shopping cart that stores products of different prices.

    >>> s = ShoppingCart()
    >>> s.display_items()
    'Items in shopping cart:'
    'None'
    >>> s.add_item(eggs, 1, 5)
    >>> s.calculate_total_sum()
    'Current cost: $5'
    >>> s.add_item(milk, 2, 3)
    >>> s.add_item(bread, 1, 2)
    >>> s.display_items()
    'Items in shopping cart:'
    '1 eggs'
    '2 milk'
    '1 bread'
    'TOTAL: 4'
    >>> s.calculate_total_sum()
    'Current cost: $13'
    >>> s.remove_item(milk, 1)
    >>> s.calculate_total_sum()
    'Current cost: $10'
    >>> s.add_item(beef, 3, 12)
    >>> s.calculate_total_sum()
    'Current cost: $46'
    >>> s.checkout()  # 50.14 rounded down to 50
    'Total paid: $50'
    >>> s.display_items()
    'Items in shopping cart:'
    'None'
    
    """

    "*** YOUR CODE HERE ***"
    return

s = ShoppingCart()
s.display_items()
s.add_item('eggs', 1, 5)
print(s.calculate_total_sum())
s.add_item('milk', 2, 3)
s.add_item('bread', 1, 2)
s.display_items()
print(s.calculate_total_sum())
s.remove_item('milk', 1)
print(s.calculate_total_sum())
s.add_item('beef', 3, 12)
print(s.calculate_total_sum())
print(s.checkout())
s.display_items()
print()



# QUESTION 5
class SchoolMember:
    """
    A member of the school that has a name and age.

    >>> john = SchoolMember("john", 13)
    >>> john.greet()
    'My name is John and I am 13.'

    >>> jean = SchoolMember("jean", 29)
    >>> jean.greet()
    'My name is Jean and I am 29.'
    
    """

    "*** YOUR CODE HERE ***"
    return

john = SchoolMember("john", 13)
print(john.greet())
print()

lisa = SchoolMember("lisa", 29)
print(lisa.greet())
print()



class Student(SchoolMember):
    """
    A school member of the school that has a name, age and grade.

    >>> joshua = Student("joshua", 13, 78)
    >>> joshua.greet()
    'My name is Joshua and I am 13.'
    'My score is 78.'

    >>> jolene = Student("jolene", 13, 98)
    >>> jolene.greet()
    'My name is Jolene and I am 13.'
    'My score is 98.'
    
    """

    "*** YOUR CODE HERE ***"
    return

joshua = Student("joshua", 13, 78)
print(joshua.greet())
print()
jolene = Student("jolene", 29, 98)
print(jolene.greet())
print()



class Teacher(SchoolMember):
    """
    A school member of the school that has a name, age, subject and salary.

    >>> jamal = Teacher("jamal", 35, 'math', 5000)
    >>> jamal.greet()
    'My name is Jamal and I am 35.'
    'I teach math and I make 5000 a month.'

    >>> jennie = Teacher("jennie", 28, 'korean', 5000)
    >>> jennie.greet()
    'My name is Jennie and I am 28.'
    'I teach korean and I make 5000 a month.'
    
    """

    "*** YOUR CODE HERE ***"
    return

jamal = Teacher("jamal", 13, 'math', 5000)
print(jamal.greet())
print()
jennie = Teacher("jennie", 29, 'korean', 5000)
print(jennie.greet())
print()



# QUESTION 6
class Class:
    """
    A class that has a teacher, a subject and students.

    >>> classA = Class(5)
    >>> classA.roll_call()
    'Total Students: 0/5'
    >>> classA.get_average_grades()  # Returns None since no teacher and no students
    'Subject: None'
    'Average Grade: None'

    >>> joshua = Student("joshua", 13, 78)
    >>> jolene = Student("jolene", 13, 98)
    >>> classA.assign_student(joshua)
    >>> classA.assign_student(jolene)
    >>> classA.get_average_grades()  # Returns error message since no teacher
    'Error: No subject assigned'

    >>> jennie = Teacher("jennie", 28, 'korean', 5000)
    >>> classA.assign_teacher(jennie)
    >>> classA.get_average_grades()
    'Subject: Korean'
    'Average Grades: 88'
    >>> classA.roll_call()
    'My name is Joshua and I am 13.'
    'My score is 78.'
    'My name is Jolene and I am 13.'
    'My score is 98.'
    'Total Students: 2/5'

    >>> jerome = Student("jerome", 13, 81)
    >>> classA.assign_student(jerome)
    >>> june = Student("june", 13, 80)
    >>> classA.assign_student(june)
    >>> jung = Student("jung", 13, 93)
    >>> classA.assign_student(jung)
    >>> jim = Student("jim", 13, 68)
    >>> classA.assign_student(jim)  # Returns error message since 6/5 students
    'Maximum capacity reached.'

    >>> classA.roll_call()
    'My name is Joshua and I am 13.'
    'My score is 78.'
    'My name is Jolene and I am 13.'
    'My score is 98.'
    'My name is Jerome and I am 13.'
    'My score is 81.'
    'My name is June and I am 13.'
    'My score is 80.'
    'My name is Jung and I am 13.'
    'My score is 93.'
    'Total Students: 5/5'
    >>> classA.get_average_grades()
    'Subject: Korean'
    'Average Grades: 86'

    >>> jamal = Teacher("jamal", 35, 'math', 5000) 
    >>> classA.assign_teacher(jamal)  # Reassigns teacher and subject only
    >>> classA.get_average_grades()
    'Subject: Math'
    'Average Grades: 86'

    """

    "*** YOUR CODE HERE ***"
    return

classA = Class(5)
classA.roll_call()
classA.get_average_grades()

joshua = Student("joshua", 13, 78)
jolene = Student("jolene", 13, 98)
classA.assign_student(joshua)
classA.assign_student(jolene)
classA.get_average_grades()

jennie = Teacher("jennie", 28, 'korean', 5000)
classA.assign_teacher(jennie)
classA.get_average_grades()
classA.roll_call()

jerome = Student("jerome", 13, 81)
classA.assign_student(jerome)
june = Student("june", 13, 80)
classA.assign_student(june)
jung = Student("jung", 13, 93)
classA.assign_student(jung)
jim = Student("jim", 13, 68)
classA.assign_student(jim)

classA.roll_call()
classA.get_average_grades()

jamal = Teacher("jamal", 35, 'math', 5000)
classA.assign_teacher(jamal)
classA.get_average_grades()