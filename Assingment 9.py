""" 1) store marks of 5 subjects
	here use marks as actual data and subject names as indexes.
accept both marks and subjects from the user.

2) create dictionary to store player name and runs scored of at least 5 players. Display it. Now convert this dictionary ‌into Series object and print it.

3) accept 10 values and store them in the Series. Now perform following operations:

a) display the entire Series
b) extract 3rd element
c) extract elements from 4 to 7
d) extract elements from fourth last till the last element
e) extract first 3 elements
f) extract elements from the 5th position


4) accept 5 values in a Series and perform the following operations:
	a) display their sum
	b) add the value accepted from the user
	c) subtract the value accepted from the user
	d) multiply the value accepted from the user
	e) add the value accepted from the user



**********  DataFrame Assignments ************************************

5) accept 5 names,designations and salaries and display them with DataFrame.

6) create a csv file (with whatever columns and rows you want) manually and then read using pandas.

7) create "Vita.xlsx" using pandas. In this Excel file you have to create 2 sheets "DBDA", and "DAC". 
in each sheet you have to write name,address and age of all the team leaders.
make sure Excel file gets created successfully.
"""
""" 1) store marks of 5 subjects
	here use marks as actual data and subject names as indexes.
accept both marks and subjects from the user. 

from pandas import *
dict={}
for i in range (5):
	subject=input("enter the subject: ")
	marks=int(input("enter the marks: "))
	dict[subject]=marks
print(dict)

myseries=Series(dict)
print(myseries)

2) create dictionary to store player name and runs scored of at least 5 players. 
Display it. Now convert this dictionary ‌into Series object and print it.



from pandas import *
dict={}
for i in range (5):
    player=input("name of player:")
    score=int(input("scores: "))
    dict[player]=score
print(dict)
myseries=Series(dict)
print(myseries)

3) accept 10 values and store them in the Series. Now perform following operations:
a) display the entire Series
b) extract 3rd element
c) extract elements from 4 to 7
d) extract elements from fourth last till the last element
e) extract first 3 elements
f) extract elements from the 5th position


from pandas import *
dict={}
for i in range(10):
    name=input("enter the name: ")
    age=int(input("enter age"))
    dict[name]=age
print(dict)
myseries=Series(dict)
print(myseries)
print(myseries[2])   
print(myseries[4:8])
print(myseries[-4:])
print(myseries[1:4])
print(myseries[5:])

4) accept 5 values in a Series and perform the following operations:
	a) display their sum
	b) add the value accepted from the user
	c) subtract the value accepted from the user
	d) multiply the value accepted from the user
	e) add the value accepted from the user

 #import pandas as np
#myseries=np.Series({'name':"sakshi",'age':22}) 
from pandas import *
dict={}
for i in range(5):
    name=input("enter the name: ")
    age=int(input("enter age"))
    dict[name]=age
print(dict)
myseries=Series(dict)
print(myseries)
print(myseries.sum())
x=int(input("enter the number:"))
print(myseries.add(x))
print(myseries.subtract(x))
print(myseries.mul(x))

**********  DataFrame Assignments ************************************

5) accept 5 names,designations and salaries and display them with DataFrame.

import pandas as np
mydataframe=np.DataFrame({"name":['sakshi','komal','rushi','swara','divya'],"designation":['engineering','pharma','iot','engi','market'],"display":[23,45,34,23,56]})
print(mydataframe)

6) create a csv file (with whatever columns and rows you want) manually 
and then read using pandas.

import pandas as np
mydataframe=np.DataFrame({"name":['sakshi','komal','rushi','swara','divya'],"designation":['engineering','pharma','iot','engi','market'],"display":[23,45,34,23,56]})
print(mydataframe)
mydataframe.to_csv("mycsvfile.csv")
myread=np.read_csv("mycsvfile.csv")
print(myread)

7) create "Vita.xlsx" using pandas. In this Excel file you have to create 2 sheets "DBDA", and "DAC". 
in each sheet you have to write name,address and age of all the team leaders.
make sure Excel file gets created successfully.

"""
import pandas as np
Vita=np.DataFrame({"name":['sakshi','komal','rushi','swara','divya'],"designation":['engineering','pharma','iot','engi','market'],"display":[23,45,34,23,56]})
print(Vita)

mydict2=np.DataFrame({'name':['Abc','Xyz','Pqr'],'designation':['officer','manager','salesexecutive'],'salary':[40000,60000,70000]})
print(mydict2)

with np.ExcelWriter("Q7.xlsx") as mywriter:
    Vita.to_excel(mywriter,sheet_name="sheet1",index=False)
    mydict2.to_excel(mywriter,sheet_name="sheet2",index=False)
