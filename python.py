Python 3.14.6 (tags/v3.14.6:c63aec6, Jun 10 2026, 10:26:10) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> age_list = [24, 25, 26, 27, 28]
... print(age_list)
...
[24, 25, 26, 27, 28]
>>> name_list = ["Asha", "Ravi", "Meena", "Arun", "Kiran"]
... print(name_list)
...
['Asha', 'Ravi', 'Meena', 'Arun', 'Kiran']
>>> name_list.append("Yazhini")
... print(name_list)
...
['Asha', 'Ravi', 'Meena', 'Arun', 'Kiran', 'Yazhini']
>>> age_list.insert(2, 30)
... print(age_list)
...
[24, 25, 30, 26, 27, 28]
>>> name_list.remove("Yazhini")
... print(name_list)
...
['Asha', 'Ravi', 'Meena', 'Arun', 'Kiran']
>>> age_list.pop()
... print(age_list)
...
[24, 25, 30, 26, 27]
>>> age_list.extend([29, 30, 26])
... print(age_list)
...
[24, 25, 30, 26, 27, 29, 30, 26]
>>> age_list.sort(reverse=True)
... print(age_list)
...
[30, 30, 29, 27, 26, 26, 25, 24]
>>> print("Maximum age:", max(age_list))
... print("Minimum age:", min(age_list))
... print("Sum of ages:", sum(age_list))
...
Maximum age: 30
Minimum age: 24
Sum of ages: 217
>>> print(name_list[0])
Asha
>>>
>>> print(name_list[-1])
Kiran
>>> print(name_list[2:5])
['Meena', 'Arun', 'Kiran']
>>> print(name_list[::-1])
['Kiran', 'Arun', 'Meena', 'Ravi', 'Asha']
>>> student_marks = {
...     "Asha": 85,
...     "Ravi": 92,
...     "Meena": 78,
...     "Arun": 88,
...     "Kiran": 95
... }
... print(student_marks)
...
{'Asha': 85, 'Ravi': 92, 'Meena': 78, 'Arun': 88, 'Kiran': 95}
>>> print(student_marks["Asha"])
85
>>>
>>> student_marks["Janani"] = 80
... print(student_marks)
...
{'Asha': 85, 'Ravi': 92, 'Meena': 78, 'Arun': 88, 'Kiran': 95, 'Janani': 80}
>>> student_marks["Asha"] = 82
... print(student_marks)
...
{'Asha': 82, 'Ravi': 92, 'Meena': 78, 'Arun': 88, 'Kiran': 95, 'Janani': 80}
>>> print(student_marks.keys())
... print(student_marks.values())
... print(student_marks.items())
...
dict_keys(['Asha', 'Ravi', 'Meena', 'Arun', 'Kiran', 'Janani'])
dict_values([82, 92, 78, 88, 95, 80])
dict_items([('Asha', 82), ('Ravi', 92), ('Meena', 78), ('Arun', 88), ('Kiran', 95), ('Janani', 80)])
>>> my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}
... print(my_set)
...
{'u', 'e', 'i', 'a', 'o'}
>>> my_set[4] = 's'
Traceback (most recent call last):
  File "<python-input-21>", line 1, in <module>
    my_set[4] = 's'
    ~~~~~~^^^
TypeError: 'set' object does not support item assignment
>>> my_set.add('s')
>>>
>>> set1 = {1, 3, 5, 7, 9}
... set2 = {2, 3, 5, 8, 10}
...
... print("set1:", set1)
... print("set2:", set2)
...
set1: {1, 3, 5, 7, 9}
set2: {2, 3, 5, 8, 10}
>>> set1 = {1, 3, 5, 7, 9}
... set2 = {2, 3, 5, 8, 10}
...
... print("Union:", set1.union(set2))
... print("Intersection:", set1.intersection(set2))
...
Union: {1, 2, 3, 5, 7, 8, 9, 10}
Intersection: {3, 5}
>>> score = int(input("Enter a score from 0 to 10: "))
Enter a score from 0 to 10: 0 to 10
Traceback (most recent call last):
  File "<python-input-26>", line 1, in <module>
    score = int(input("Enter a score from 0 to 10: "))
ValueError: invalid literal for int() with base 10: '0 to 10'
>>> set1 = {1, 3, 5, 7, 9}
... set2 = {2, 3, 5, 8, 10}
...
... print("Union:", set1.union(set2))
... print("Intersection:", set1.intersection(set2))
...
Union: {1, 2, 3, 5, 7, 8, 9, 10}
Intersection: {3, 5}
>>>
>>> set1 = {1, 3, 5, 7, 9}
... set2 = {2, 3, 5, 8, 10}
...
... print("Union:", set1.union(set2))
... print("Intersection:", set1.intersection(set2))
... score = int(input("Enter a score from 0 to 10: "))
...
Union: {1, 2, 3, 5, 7, 8, 9, 10}
Intersection: {3, 5}
Enter a score from 0 to 10: 7
>>>
>>> set1 = {1, 3, 5, 7, 9}
... set2 = {2, 3, 5, 8, 10}
...
... print("Union:", set1.union(set2))
... print("Intersection:", set1.intersection(set2))
... score = int(input("Enter a score from 0 to 10: "))
...
Union: {1, 2, 3, 5, 7, 8, 9, 10}
Intersection: {3, 5}
Enter a score from 0 to 10: 7
>>> score = int(input("Enter a score from 0 to 10: "))
...
... ... if score > 7:
... ...     print("Above Average")
... ...
... Enter a score from 0 to 10: 7
... >>> score = int(input("Enter a score from 0 to 10: "))
... ...
... ... if score > 7:
... ...     print("Above Average")
... ... elif 4 <= score <= 7:
... ...     print("Average")
... ...
... Enter a score from 0 to 10: 4
... Average
... >>> score = int(input("Enter a score from 0 to 10: "))
... ...
... ... if score > 7:
... ...     print("Above Average")
... ... elif 4 <= score <= 7:
... ...     print("Average")
... ... else:
... ...     print("Below Average")
... ...
... Enter a score from 0 to 10: 3
... Below Average
... >>> score = int(input("Enter a score from 0 to 10: "))
... ...
... ... if score > 7:
... ...     print("Above Average")
... ... elif 4 <= score <= 7:
... ...     print("Average")
... ... else:
... ...     print("Below Average")
... ...
... Enter a score from 0 to 10: 5
... Average
... >>> score = int(input("Enter a score from 0 to 10: "))
... ...
... ... if score > 7:
... ...     print("Above Average: Great job! Keep it up.")
... ... elif 4 <= score <= 7:
... ...     print("Average: Good effort! Keep practicing.")
... ... else:
... ...     print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")
... ...
... Enter a score from 0 to 10: 2
... Below Average: Need to improve your performance. Consistent practice will lead to better results.
