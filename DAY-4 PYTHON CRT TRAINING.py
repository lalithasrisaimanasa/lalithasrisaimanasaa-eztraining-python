##dictionary comprehension
d={n:n*n for n in range(1,5)}
print(d)
#caluculating product price for 5 units
old={'rice':60,'dhaal':120,'oil':150}
new={product:price*5 for (product,price) in old.items()}
print(new)
#with checks
real={'sam':24,'angel':18,'kumar':35}
now={name:age for (name,age) in real.items() if age>20}
print(now)
#create a list with 8 customer names display a dictionary which has customers names along with discounts for them from a particular shop
import random
cust=["manasa","sruj","hi","hello","happy","yamini","lalitha","hafsa"]
cust_dict={names:random.randint(1,100)for names in cust}
print(cust_dict)
#create 2 list, 1st list with 5 students  names and 2nd list with total marks and create dictionary along with percentage
names=["manasa","hi","hello","jyo","mustaf"]
marks=[100,50,30,80,64]
per=[]
for i in marks:
    p=(i*100)/500
    per.append(p)
d={keys:values for(keys,values)in zip(names,per)}
print(d)
#user input dict comprehesion
import random
student_names=list(map(str,input("enter names:")))
marks=[]
for i in range(len(student_names)):
                       a=(random.randint(300,500)/500)*100
                       marks.append(a)
my_dict={x:y for (x,y) in zip(student_names,marks)}
print(my_dict)
#string methods
s="manasa"
s.upper()
'MANASA'
s.lower()
'manasa'
s.casefold()
'manasa'
s.capitalize()
'Manasa'
s.replace("j","a")
'manasa'
s.replace("a","j")
'mjnjsj'
s.strip()
'manasa'
m="   ma na sa "
m.strip()
'ma na sa'
m.center(31,'*')
'**********   ma na sa *********'
s.split()
['manasa']
s="lalitha sri sai manasa"
s.count('a')
6
s.count('a',5,len(s))#start with 5th index and till end of string it checks 'a'
5
s.endswith('a',0,len(s))#check string end with a or not returns booleannfunction
True
s.find('a',0,len(s))##checks a and returns index value of 1st occurence of a
1
s.index('a',7,len(s))#from 7 to end where a three returns first occurence of character index
13
#1)after getting a string as input  check your string contains spaces or not if yes then count no of spaces in it and find it
#2)get one string as input along with one character and find out and display whether that particular character is present or not
#3)check whether string is palindrome or not
#4)create a list with vowels get one string as input count vowel from the string and display result
##2)
k=input("string")
j=input("character")
if j in k:
    print("present")
else:
        print("not")
##iteration -2nd logic
k=input("enter string")
j=input("enter character")
for i in k:
    if i==char:
        flag=1
        break
    else:
        flag=0
    if flag==1:
        print("present")
    else:
        print("not present")
##3rd logic
s=input("enter string")
k=input("enter character")
a="yes" if k in s else no
print(a)
##program-1
s=input("enter string")
count=0
for i in s:
    if i==" ":
        count=count+1
print(count)
##program-4
l=input("enter string")
j=['a','e','i','o','u']
count=0
for i in l:
    if i in j:
        count=count+1
print(count)

##math module

import math
print("ceil of 12.1:",math.ceil(12.1))
print("floor of 12.1:",math.floor(12.1))
print("sqrt of 16:",math.sqrt(16))
print("factorial of 5:",math.factorial(5))
print("power of 3,4:",math.pow(3,4))
print("remainder of 12,9:",math.fmod(12,9))
a,b=divmod(12,9)
print(a,b)

                    

                       
                       
   


