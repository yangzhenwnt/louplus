#!/usr/bin/env python3
n = int(input("Enter the number of students: "))
data = {}
Subjects = ("Physics","Maths",'History') #所有科目
for i in range(0,n):
    name = input('Enter the name of the students {}: '.format(i + 1))  #获取学生名称
    marks = []
    for x in Subjects:
        marks.append(int(input("Enter marks of {}: ".format(x))))  #获取每一科的分数
    data[name] = marks
for x,y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x,total))
    if total < 120:
        print(x,"failed :(")
    else:
        print(x,"passwd :)")
    
