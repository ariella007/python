""" mylist=[i for i in range(4,20) if i%2==0]
print(mylist)
print(mylist[::-1])
mylist1=[num**2 for num in range (1,15,2)]
print (mylist)
 """
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
result=d1+d2
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
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)
print({**dic1,**dic2,**dic3})
"""
#________________________________________________________________________________________________________
"""1)Write a Python program to find all the values in a list are greater than a specified number.

list1=[10,20,30,40,50,60,70,80,90]
n=int(input("enter the nunber:"))
for i in list1:
    if n<i:
        print(i)

"""   
# 2) Write a Python program to find the list of words that are longer than n 
# from a given list of words.


""" list1=["sakshi","salunkhe","rishikesh","nimbalkar"]
n=int(input("enter the length"))
for i in list1:
    if len(i)>n:
        print(i) """

# 3) Write a Python program to get the largest number from a list.

""" list1=[10,20,30,40,90,60,70,80,50]
max=0
for i in list1:
    if i>max:
        max=i
print(max) """

#4) Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# Sample List : ['abc', 'xyz', 'aba', '1221'] """

# output
# 	aba      1221

""" List1 = ['abc', 'xyz', 'aba', '1221'] 
for i in List1:
    if len(i)>1:
        if i[:1]==i[-1:]:
            print(i)
    
print(List1[2:])
 """

#5) Write a Python program to multiply all the items in a list.

""" list1=[10,20,30,40,50,60,70,80,90]
n=1
for i in list1:
    i=i*n
    n=i
print(i)
 """
# 6) Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. 
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black'] """
""" List1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(List1[1:4]) """

# 7) Write a Python program to 
# print the numbers of a specified list after removing even numbers from it.
""" a=[i for i in range(1,19) if i%2!=0] 
print(a)
 """
# 8) Write a Python program access the index of a list.
# 	output : all the elements along with their index
""" a=[i for i in range(1,20)]
for i in range(0,19):
    print(i,"\t",a[i])
 """
#9) Write a Python program to check a list is empty or not
""" list=[]
if len(list)==0:
    print("empty")
else:
    print("not empty") """
#10) Write a Python program to check whether the n-th element exists in a given list.
""" a=[i for i in range(1,21)]
b=len(a)
n=int(input("enter the number"))
if  b>=n:
    print("yess")
else:
    print("no") """
#11) Write a Python program to clone or copy a list
a=[i for i in range(1,21)]
b=a.copy()
print(b)
# 12) Write a Python program to convert list to list of dictionaries. 
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, 
# {'color_name': 'Red', 'color_code': '#FF0000'},
#  {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

""" x=["Black", "Red", "Maroon", "Yellow"]
y=["#000000", "#FF0000", "#800000", "#FFFF00"]
mydict=[{"color_name":a,"color_code":b} for a,b in zip(x,y)]
print(mydict) """


#13) Write a Python program to find the index of an item in a specified list.
""" list1=[10,20,30,40,50]
n=int(input("enter the number:"))
count=0
for i in list1:
    if i==n:
        break
    count+=1
print(count) """

#14) Write a Python program to insert a given string at the beginning of all items in a list. 
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
""" list1=[1,2,3,4]
string='emp'
list2=[]
for i in list1:
    list2.append(string+f"{i}")
print(list2) """

#15) Write a Python program to iterate over two lists simultaneously.
""" list1=[1,2,3,4]
list2=['a','b','c','d']
list3=["sakshi","salunkhe","rushikesh","nimbalkar"]
l=len(list2)
for i in range(0,l):
    print(list1[i],"\t",list2[i],"\t",list3[i]) """

#16) Write a Python program to print a nested lists (each list on a new line)
#  using the print() function.

""" list1=[[1,2,3,4],[5,6,7,8]]
for i in list1:
    print(i) """

#17) Write a Python program to remove duplicates from a list.
""" list1=[1,2,3,4,5,2,4,2,4,3,6,7]
a=set(list1)
print([a]) """

#18) Write a Python program to replace the last element in a list with another list. 
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

""" list1=[1, 3, 5, 7, 9, 10]
list2=[2, 4, 6, 8]
list1.remove(10)
print(list1)
print(list1+list2) """
#19) Write a Python function that takes two lists and returns True if they have at least one common member. 
""" list1=[1, 3, 5, 2]
list2=[2, 4, 6, 8]
for i in list1:
    if i in list2:
        print("true")
        print(i)
    else:
        print("false") """
# mydictionary1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# mydictionary2={7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144}
# """ mydictionary1.update(mydictionary2)
# print(mydictionary1)
#  """

# mydict3={**mydictionary1,**mydictionary2}
# print(mydict3)

""" prnnos=[1,2,3,4,5,6]
names=['abc','def','pqr','lmn','xyz','uvw']
mydict2=dict(zip(prnnos,names))
print(mydict2) """
# Players={'Rohit':{'runs':10000,'centuries':15},'Virat':{'runs':12000,'centuries':18}}

# for i in Players:
#     print(i)
#     for j in Players[i]:
#         print(j ,":",Players[i][j])

if __name__ == '__main__':
    for _ in range(int(input("enter rank"))):
        name = input("enter the name")
        score = float(input("enter the score"))
        mydict=list(zip(name,score))
        print(mydict)




