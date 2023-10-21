"""
1)accept a number and display its table.

a=int(input("Enter the number"))
print(a)
print("display the table")
for n in range (1,11):
    print(a*n)

2)using switch ….case   display whether accepted character is vowel or not.
a=str(input("enter the character"))
print (a)
match a:
    case 'a':
        print("character is vowel")
    case 'e':
        print("character is vowel")
    case 'i':
        print("character is vowel")
    case 'o':
        print("character is vowel")
    case 'u':
        print("character is vowel")
    case 'A':
        print("character is vowel")
    case 'E':
        print("character is vowel")
    case 'I':
        print("character is vowel")
    case 'O':
        print("character is vowel")
    case 'U':
        print("character is vowel")
    case _:
        print("character is not vowel")

3)	Display numbers  1 to 10 using  While loop
a=1
while (a<11):
    print(a)
    a+=1

4)	Display numbers from 3 to 30 except number 24  using while loop
a=3
while(a<31):
    if(a==24):
        a += 1
        continue
    print(a)
    a+=1

5)	accept marks from the user. Using if…….elif….  Else,
display whether result is  fail, pass, second class , first class, Distinction etc.


a=int(input("enter the marks"))
if 100>a>=80:
    print("pass with Distiction")
elif 80>a>=70:
    print("pass with first class")
elif 70>a>=60:
    print("pass with b second class")
elif 60>a>=35:
    print("pass")
else:
    print("fail")


6) print the total of first 10 numbers.
b=0
for a in range(0,11):
    b+=a
    print(b)

7) accept numbers till user enters 0 and display the total of all the numbers entered.

b=0
while True:
    a = int(input("enter the number"))
    if (a==0):
        break
    else:
        b+=a
print(b)

8) accept a character and display whether
it is upper case or lower case or not an alphabet.
"""

"""
asc = ord(a)
print(asc)
if 65<=asc<=90:
    print("upper case")
elif (asc>=97 and asc<=122):
    print("lower case")
else:
    print("not an alphabet")
    """
"""
a=input("Enter the Alphabet")
if a.isalpha():
    if a.isupper():
        print("upper case")
    else:
        print("lower case")
else:
    print("not an alphabet")
    
9) display fibonicii series of 10 numbers

    
t,t1=0,1
print(t,t1,end=" ")
s=0
for a in range (1,11):
    s=t+t1
    print(s,end=" ")
    t=t1
    t1=s

10) display prime numbers from 3 to 30  
    
for i in range (3,31):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(i)

#11) accept a number and display whether it is prime or not

a = int(input("enter the number"))
for i in range(a,a//2):
    if(a%i==0):
        print("not a prime ")
        break
    else:
        print("prime number")
        
12)print the following pattern:
*
* *
* * *
* * * *
* * * * *
        
for i in range(1,6):
    for j in range(1,i):
        print("*",end=" ")
    print( )
    
#13)print the following pattern:
* * * * * 

* * * * 

* * * 

* * 

* 

for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print( )
    
14) print the following pattern
		        *
	         *  *
          *  *  *
       *  *  *  *
    *  *  *  *  *
    

for i in range (1,6):
    for s in range (i,6):
        print(" ",end=" ")
    for j in range (1,i):
        print("*",end=" ")
    print()





15) print the following pattern

    * 
   * * 
  * * * 
 * * * * 
* * * * * 

for i in range (1,6):
    for s in range (i,5):
        print(" ",end=" ")
    for j in range (1,i):
        print(" * ",end=" ")
    print()


16) print the following pattern

*   *   *   *   *   

  *   *   *   *   

    *   *   *   

      *   *   

        *   

for i in range (5,0,-1):
    for s in range (5,i,-1):
        print(" ",end=" ")
    for j in range (i,0,-1):
        print(" * ",end=" ")
    print()


17) print the following

     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 

"""

for i in range (1,7):
    for s in range (i,6):
        print(" ",end=" ")
    for j in range (1,i):
        print(" * ",end=" ")
    print()
for i in range (4,0,-1):
    for s in range (5,i,-1): #spaces should be one more than row number
        print(" ",end=" ")
    for j in range (i,0,-1):
        print(" * ",end=" ")
    print()
























