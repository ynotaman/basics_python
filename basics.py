
# 01
print(">>> basics outputs <<<")
print(1)
print("amaan ullah khan")
# 02
print(">>> by takink variable  <<<")
a=2
b=5
print(a , b)
print(a+b)
# 03
print(">>> the number as string <<<")
c="3"
d="8"
print (c+d)
a="1"
b=4

print(int(a)+b)
#04
print(" >>> type casting <<<")
print (int (c)+int(d))
x=str(123)
y=int(234)
z=float (9)
print (x)
print(y)
print (z)

# 05
print (" >>> taking  double quotes  between double quotes <<<  ")
print("amaan,\"ullah khan")
#06
print (" >>> multilining <<< ")
print(''' my name is 
          amaan ullah khan
     ''')
# 07
print(" >>> you can operate an operation in print built in function <<< ")
a=15
b=4
print (a)
print (b)
print (" the addition of the two numbers is                  :  " ,  a+b)
print (" the multiplication  of the two numbers is           :  " ,  a*b)
print (" the division  of the two numbers is                 :  " ,  a/b)
print (" the modulus  of the two numbers is                  :  " ,  a%b)
print (" the exponential  of the two numbers is              :  " ,  a**b)
print (" the greatest integer quotient of the two numbers is :  " ,  a//b)
# 08
print (" >>> to print the elements seprately <<< ")
print ("hey i am amaan ", 2 , 3 , 4, 5 , 6 ,sep  = "~"  , end = " ullah khan ")
print ( " >>> to find which type of data type we used <<< ")
a=123
b="harry"
c=True
d= 0.4
print ( " the type of a is : " , type(a))
print ( " the type of b is : " , type(b))
print ( " the type of c is : " , type(c))
print ( " the type of d is : " , type(d))
# 09.1

list = [ " amaan ", 1 , " khan " , 2 , "amaan , waris "]
print (list)

 #09.2
print ("unpacking")
list = [ " amaan ", 1 , " khan " , 2 , "amaan , waris "]
x=y=z=list
print(x)
print(y)
print(z)


#  10 
print (" >>> taking input in python <<< ")
a=input ("enetr the value  : ")
print (a)
print("amaan ullah khan " , a )

#  11
print (" >>> input with type casting <<< ")
x = input ("enter the  value of x : ")
y= input ("enter the value of  Y : ")
print ( "the result without  type casting : ",x+y)
print (" result with type casting : " ,int (x) +  int (y))


a = "amaan "
print ( a + " khan")

# 12
print (" >>> to print the  given number of charachters <<< ")
a= "mango"
print (a[0:5])
print (a[0])
print (a[3])
print (a[0:2])
print (a[-1:10])
print (a[-3:-8])
print (a[   : 5 ])
print (a[ 0 : ])

# 13

print (" >>> to find out the lenght od=f agiven string <<< ")
a= "amaan ullah khan"

b = print (" the length of the string is : ",len(a))
print(b)

# 14
amaan="amaan khan"
print (" >>> camel case variable name <<< ")
     # amaanUnllahKhan = "34567890"
     # print(amaanUllahKhan)
     
print (" >>> Assign multiple values <<< ")
x,y,z = "amaan", 1234567890 ,"khan"
print (x,y,z)

print (" >>> one value in multiple varibles <<< ")
x = y = z = "Orange"
print(x)
print(y)
print(z)
'''
print("Insert the correct keyword to make the variable x belong to the global scope.")
def myfunc():
  
global
 x
  x = "fantastic"
'''
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
