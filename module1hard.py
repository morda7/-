grades = [[5, 3, 3, 5, 4],[2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a1 = sum(grades[0]) / len(grades[0])
a2 = sum(grades[1]) / len(grades[1])
a3 = sum(grades[2]) / len(grades[2])
a4 = sum(grades[3]) / len(grades[3])
a5 = sum(grades[4]) / len(grades[4])
students1 = list(students)
students1.sort()
print((dict([[students1[0], a1], [students1[1], a2], [students1[2], a3], [students1[3], a4], [students1[4], a5]])))
