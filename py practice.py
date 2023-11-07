# Imylist=[i for i in range(4,20) if i%2==0]
# print(mylist)
# print(mylist[::-1])
# mylist1=[num**2 for num in range (1,15,2)]
# print (mylist)

""" mydict={"saop":100,"perform":200,"deo":300,"hairoil":250}
myset={x for x in mydict.values()}
print(myset)
myset1={x for x in mydict.keys() if len(x)>3}
print(myset1)
mydict1={x:x*2 for x in range(1,10)}
print(mydict1)
mydict3={x:x**2 for x in range(1,6)}
print(mydict3) """

""" product=["soap","perform","deo","hairoil"]
price=[10,20,30,40]
mydict={key:value for (key,value)in zip(product,price)}
print(mydict)

for (key,value) in zip(product,price):
    print(key,"\t",value) """

""" mydict={'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
'z': [31, 32, 33, 34, 35, 36, 37, 38, 39]}
print(mydict['x'][4])
print(mydict['y'][4])
print(mydict['z'][4]) """

""" mydict={0: 10, 1: 20}
mydict[2]=30
print(mydict) """
 
""" mydict={0: 10, 1: 20, 2: 30}
print(mydict)
keys=int(input("enter the key:"))
if keys in mydict:
    print("key in a dictionary")
else:
    print("retry") """
""" 
____________________________________________________________________________________________________
4) Write a Python program to count the values associated with key in a dictionary. 
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True

mydict= [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success': False, 'name': 'Rabi'}, {'id': 3, 'success': False, 'name': 'Alex'}]
print(mydict)
count=0
for i in mydict:
    if i['success']==True:
        count+=1

print(count) """

""" 
5) Write a Python program to create a dictionary from two lists without losing duplicate values. 
Sample lists: ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII'], [1, 2, 2, 3]
Expected Output: {'Class-VII': {2}, 'Class-VI': {2}, 'Class-VIII': {3}, 'Class-V': {1}}) 

classes=['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII']
value1=[1, 2, 2, 3]
mydict={key:value for (key,value) in zip(classes,value1)}
print(mydict)
 """
""" 
6) Write a Python program to check a dictionary is empty or not.

mydict={0: 10, 1: 20, 2: 30}
print(mydict)
if mydict.__len__()==0:
    print ("empty")
else:
    print(mydict.__len__()) """

""" 7) Write a Python program to combine two dictionary adding values for common keys. 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})


from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d1=Counter(d1)
d2=Counter(d2)
result=d1+
print(result)

s='sakshi'
print(Counter(s))
 
 
 
8) Write a Python program to count number of items in a dictionary value 
that is a list

sample data:

mydictionary1={'Names':['Rohit','Ganesh','SRK','Akshay'],'age':40,'addresses':['Mumbai','Delhi','Kolkara','Banglore'],'emails':['actor.gmail.com','movie.gmail.com']}

mydictionary1={'Names':['Rohit','Ganesh','SRK','Akshay'],'age':[40],'addresses':['Mumbai','Delhi','Kolkara','Banglore'],'emails':['actor.gmail.com','movie.gmail.com']}
print(mydictionary1)
count=0
for i in mydictionary1.values():
    count +=len(i)

print(count)

9) Write a Python program to create a dictionary from a string. 
Note: Track the count of the letters from the string.
Sample string : 'w3resource'
Expected output: {'3': 1, 's': 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}

from collections import Counter
string1='w3resource'
print(Counter(string1))

10) Write a Python program to get the key, value and item in a dictionary
e.g.
mydictionary={1:'xyz',3:'abc',5:'pqr',2:'xzz'}

output :
	key     value   
		total items are 4


mydictionary={1:'xyz',3:'abc',5:'pqr',2:'xzz'}

for key,values in mydictionary.items():
    print(key,"\t",values)

print("total items are : ",len(mydictionary))

11) Write a Python program to get the maximum and minimum value in a dictionary.

mydictionary={'a': 100, 'b': 200, 'c':300}

print(max(mydictionary.values()))
print(min(mydictionary.values()))

12) Write a Python program to map two lists into a dictionary. 
e.g. 
given
prnnos=[1,2,3,4,5,6]
names=['abc','def','pqr','lmn','xyz','uvw']

output:
{1: 'abc', 2: 'def', 3: 'pqr', 4: 'lmn', 5: 'xyz', 6: 'uvw'}


list1=['a','b','c','d','e']
list2=[1,2,3,4,5]
mydict=dict(zip(list1,list2))
print(mydict)


prnnos=[1,2,3,4,5,6]
names=['abc','def','pqr','lmn','xyz','uvw']
mydict2=dict(zip(prnnos,names))
print(mydict2)


13) Write a Python program to match key values in two dictionaries. 
Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
Expected output: key1: 1 is present in both x and y

a={'key1': 1, 'key2': 2, 'key3': 2}
b={'key1': 1, 'key2': 2}

for i in a.keys():
    if i in b.keys():
        if a[i]==b[i]:
            print(i,":",a[i]," is present")

            
             
 14) # Write a Python program to print a dictionary line by line. 

Players={'Rohit':{'runs':10000,'centuries':15},'Virat':{'runs':12000,'centuries':18}}

expected output:

Rohit
runs :	 10000
centuries :	 15
Virat
runs :	 12000
centuries :	 18

 """
""" Players={'Rohit':{'runs':10000,'centuries':15},'Virat':{'runs':12000,'centuries':18}}
 
for i in Players:
    print(i)
    for j in Players[i]:
        print(j," : ",Players[i][j]) """


""" for key,value in Players.items():
    print(key,"\t",value) 

 15) Write a Python program to remove a key from a dictionary. 
mydict={1: 'abc', 2: 'def', 3: 'pqr', 4: 'lmn', 5: 'xyz', 6: 'uvw'}
 del mydict[1]
print(mydict) 
mydict.pop(1)
print(mydict)

16) Write a Python program to remove spaces from dictionary keys. 

Students={'d 01':'Abc','d 0 2':'Xyz','d0 3':'Pqr'}

output:

{'d01': 'Abc', 'd02': 'Xyz', 'd03': 'Pqr'}
"""

""" #set1=({})
for i in (Students.keys()):
    i.replace(""," ")
    
print(Students)
 """
""" Students={'d 01':'Abc','d 0 2':'Xyz','d0 3':'Pqr'}
new=({})
for key,value in Students.items():
    newkey=key.replace(" ","")
    new[newkey]=value
print(new)    
 
 17) Write a Python program to sum all the items in a dictionary. 
 

mydict={1:2,2:4,3:9,4:16,5:25,6:36}
a=0
b=0
for key,values in mydict.items():
    a+=key
    b+=values
print(a+b)
 
 18) Write a Python script to merge two Python dictionaries. 

mydictionary1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
mydictionary2={7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

output:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}

 
 
mydictionary1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
mydictionary2={7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}




mydictionary1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
mydictionary2={7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
mydictionary1.update(mydictionary2)
print(mydictionary1)


mydict3={**mydictionary1,**mydictionary2}
print(mydict3)


19) Write a Python script to concatenate following dictionaries to create a new one. 
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : 
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


"""


""" dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
print({**dic1,**dic2,**dic3}) """

""" Players={'Rohit':{'runs':10000,'centuries':15},'Virat':{'runs':12000,'centuries':18}}
for i in Players:
    print (i)
    for j in Players[i]:
        print(j ,":",Players[i][j]) """

""" mydict1={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
del mydict1[1]
print(mydict1)
mydict1.pop(6)
print(mydict1)
mydict1[3]=1
print(mydict1) """

#____________________________________________________________________________________________________
""" import numpy as np
list=[]
for i in range(5):
    n=int(input("enter the number"))
    list.append(n)
print(list)
first=np.array(list)
print(first)
second=np.sum(first)
print(second) """

""" import numpy as np
first=np.arange(1,10,1).reshape(3,3)
print(first)
second=tuple(map(tuple,first))
print(second)
third=list(map(list,first))
print(third) """
# forth=set(map(set,first))
# print(set)

""" import numpy as np
first=np.random.randint(20,100,12).reshape(4,3)
print(first)
second=tuple(map(tuple,first))
print(second) """

""" import numpy as np
first=np.array([[1,2,3],[4,5,6]])
second=np.array([[7,8,9],[10,11,12]])
print(first,second)
third=np.stack((first,second),axis=0)
forth=np.stack((first,second),axis=1)
fifth=np.stack((first,second),axis=2)
print(third)
print(forth)
print(fifth) """


""" import numpy as np
first=np.array([1,2,3,4])
second=np.array([5,6,7,2])
print(first)
print(second)
third=np.intersect1d(first,second)
print(third)
forth=np.setdiff1d(first,second)
print(forth)
forth=np.setdiff1d(second,first)
print(forth) """

# import numpy as np
# from numpy import *
""" list=[]
print("no of rows")
rows=int(input())
print("no of column")
cols=int(input())
print("number of element \t",rows*cols)
first=np.random.randint(1,100,(rows*cols)).reshape(rows,cols)
print(first) """
""" for i in range(1,(rows*cols)+1):
    n=int(input())
    list.append(n)

print(list)
first=array([list])
first=first.reshape(rows,cols)
print(first) """
""" f1=np.array([[1,2,3,4],[5,6,7,8]])
print(f1)
f2=np.array([[10,20,30,40],[50,60,70,80]])
print(f2)
second=np.sum((f1,f2),axis=0)
third=np.sum((f1,f2),axis=1)
forth=np.sum((f1,f2),axis=1)
print(second)
print("********************")
print(third)
print("********************")
print(forth) """

""" first=np.linspace(1,101,20)
print(first) """
""" first=np.arange(1,9)
print(first[1:5])
print(first[3:])
print(first[-3:]) """
""" first=np.array([[10,20,30,40],[50,60,70,80],[90,100,110,120]])
print(first[1,:3])
print(first[2,1:3])
print(first[:,2:3])
print(first[1:3,:2]) """


""" list=[]

while True:
    n=int(input("enter the number until 0"))
    if (n==0):
        break
    list.append(n)
print(list)
myseries=Series(list)
print(myseries)
print(len(myseries)) """

""" mytuple=(120,123,455,666,577,433)
myseries=Series(mytuple)
print(myseries.to_string(index=False)) """

""" first=Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(first) """
""" mydict=({1:'sakshi',2:'salunkhe',3:'engi',4:'entc'})
myseries=Series(mydict)
print(myseries) """
 
""" first=Series([10,20,30,40,50])
second=Series([1,2,3,4,5])
print(first[4])
print(first[-2:])
print(first,second)
print(first.sum())
print(first.mul(10))
print(first.div(10))
print(first.subtract(5)) """

""" from pandas import *
mydict={"Names":['sakshi','salunkhe','sharvari','pari'],"age":[12,34,56,66]}
print(mydict)
mydata=DataFrame(mydict)
print(mydata)
print(mydata["Names"].values.tolist())
print(mydata["age"].values.tolist())
print(mydata.values.tolist())
print(mydata.iloc[:,0:1].values.tolist()) """

""" dict={}
for i in range (5):
    marks=int(input("enter the number:"))
    subject=input("enter the subject:")
    dict[subject]=marks
print(dict)
myseries=Series(dict)
print(myseries) """

""" dict={}
for i in range(5):
    players=input("player name: ")
    runs=int(input("enter runs: "))
    dict[players]=runs
print(dict)

mydataframe=Series(dict)
print(mydataframe) """

""" myseries=Series([x for x in range (10,110,10)])
print(myseries)
print(myseries[:])
print(myseries[3:4])
print(myseries[4:8])
print(myseries[-4:])
print(myseries[1:3])
print(myseries[5:])
print(myseries.sum())
addnum=int(input("enter the number"))
print("addition","\n",myseries.add(addnum))
print("substraction","\n",myseries.sub(addnum))
print("multiplication","\n",myseries.mul(addnum)) """
""" import pandas as np
a=[]
b=[]
c=[]
for i in range(5):
    name=input("enter name: ")
    designations=input("enter designation: ")
    salaries=int(input("enter salaries"))
    a.append(name)
    b.append(designations)
    c.append(salaries)
data={"name":a,"designation":b,"display":c}
print(data)
mydataframe=np.DataFrame(data)
print(mydataframe)
mydataframe.to_csv("mycsvpract.csv")
myread=np.read_csv("mycsvpract.csv")
print(myread)
 """
# import pandas as np
# Dbda=np.DataFrame({"name":['sa','ks','hi','sa'],"age":[12,23,34,56]})
# print(Dbda)
# dac=np.DataFrame({'name':['abc','xyz','pqr','efg'],'salaries':[10,20,30,40]})
# print(dac)
#
# with np.ExcelWriter("Vita.xlsx")as mywriter:
#     Dbda.to_excel(mywriter,sheet_name="sheet1")
#     dac.to_excel(mywriter,sheet_name="sheet2")

# mylist=[]
# for i in range(10):
#     num=int(input("enter the number: "))
#     mylist.append(num)
# peint(mylist)
# myset=set(mylist)
# print(myset)
# num1=int(input("enter the number: "))
# if num1 in myset:
#     myset.discard(num1)
# else:
#     myset.add(num1)
# print(myset)

# """ name=input("enter your name")
# print(name)
# print(name.swapcase())
# print(name) """

# s1=("Tejal",24,"Kalyan","MSc")
# s2=("Sakshi",22,"Nashik","BE")
# s3=("Aishwarya",26,"Kalyan","MD")
# s4=("Riddhi",22,"Ghatkopar","MSc")
# mylist=[s1,s2,s3]
# print(mylist)

n=input("enter the word: ")
s=str(n)
if (s==s[::-1]):
    print("palindrone")
else:
    print("not palindrone")


