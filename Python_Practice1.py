#!/usr/bin/env python
# coding: utf-8

# 1). <b> Write a python program to print the following string in a specific format </b>
# 
# Sample String: "Twinkle,twinkle little star, How I wonder what you are!Up above the world so high. Like a diamond in the sky.Twinkle,twinkle,little star,How I wonder what you are"
# 
# Output:
# 
# Twinkle,twinkle,little star,
#     How I wonder what you are!
#         Up above the world so high,
#         Like a diamond in the sky.
# Twinkle,twinkle,little star,
#     How I wonder what you are

# In[1]:


print("Twinkle,twinkle little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle,twinkle,little star,\n\tHow I wonder what you are")


# 2). <b> Write a python program to get the Python version </b>

# In[2]:


import sys
print("Python version")
print(sys.version)
print("Version info")
print(sys.version_info)


# 3). <b> Write a Python program to display the current date and time <b>

# In[3]:


import datetime
now = datetime.datetime.now()
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))


# 4). Write a python program which accepts the radius of a circle from the user and compute the area

# In[4]:


from math import pi
rad = float(input("Input the radius of the circle:"))
print("The area of the circle with radius" +str(rad)+ "is:" +str(pi*rad**2))


# 5). Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them

# In[5]:


first_name = str(input("Please enter the first name:"))
last_name = str(input("Please enter the last name:"))
print(last_name +" " +first_name)


# 6). Write a Python program which accepts a sequence of comma-seperated numbers from user and generate a list of and a tuple with those numbers

# In[6]:


input_numbers = input("Input some comma seperated numbers:")
list = input_numbers.split(",")
tuple = tuple(list)
print("List:", list)
print("Tuple:", tuple)


# 7). Write a Python program to accept a filename from the user and print the extension of that

# In[7]:


input_filename = input("Please enter the filename:")
file_extn = input_filename.split(".")
print("The extension of the file is: " + repr(file_extn[-1]))


# 8). Write a Python program to display the first and last colors from the following list:
#                 color_list = ["Red", "Green", "White", "Black"]

# In[8]:


color_list = ["Red", "Green", "White", "Black"]
color_list[::3]
#print("%s %s"%(color_list[0], color_list[-1]))


# 9). Write a python program to display the examination shcedule. (extract the date from exam_st_date): exam_st_date = (11,12,2019)
# 
# sample output = 11/12/2019
# 

# In[9]:


exam_st_date = (11,12,2019)
print("The examination will commence from: %i /%i /%i"%exam_st_date)


# 10). Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.

# In[10]:


a = int(input("Please enter the desired number:"))
n1 = int("%s" %a)
n2 = int("%s%s"% (a,a))
n3 = int("%s%s%s"% (a,a,a))
print(n1+n2+n3)


# 11). Write a Python program to print the documents (syntax, description, etc.) of Python built-in function(s)

# In[11]:


In-built function: abs()
print(abs.__doc__)


# 12). Write a Python program to print the calendar of a given month and year.

# In[ ]:


import calendar
Year = int(input("Enter the year:"))
Month = int(input("Enter the Month:"))
print(calendar.month(Year,Month))


# 13). <b> Write a Python program to print the following 'here document' </b>:
# 
# Sample String:
# 
# a string that you "don't" have to escape
# 
# This
# 
# is a ...... multi-line
# 
# heredoc string ------>example

# In[14]:


print("""

a string that you "don't" have to escape

This

is a ...... multi-line

heredoc string ------>example

""")


# 14). <b> Write a Python program to calculate number of days between two dates. </b>
#         
#         
#         sample dates :(2014,7,2), (2014,7,11)

# In[15]:


from datetime import date
f_date = date(2014,7,2)
l_date = date(2014,7,11)
No_of_days = l_date - f_date
print(No_of_days)


# 15). <b> Write a Python program to get the volume of a sphere with radius 6.

# In[13]:


Pi = 3.14
rad = 6
Vol = (4/3)*Pi*(rad**3)
print(Vol)


# 16). <b> Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference </b>

# In[12]:


def difference(n):
    if n <= 17:
        return 17-n
    else:
        return (n-17)*2
    
print(difference(32))


# 17). <b> Write a python program to test whether a number is 100 of 1000 or 2000 </b>

# In[24]:


def near_thousand(n):
    return ((abs(1000-n) <= 100) or (abs(2000-n) <=100))
print(near_thousand(1000))


# 18). <b> Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum </b>

# In[26]:


def three_numbers(a,b,c):
    sum = a+b+c
    
    if a == b == c:
        sum*= 3
    return sum
print(three_numbers(1,2,3))
print(three_numbers(2,2,2))


# 19). <b> Write a Python program to get a new string from a given string where "Is" has been added to the fornt. If the given string already begins with "Is" then return the string unchanged </b>

# In[29]:


def new_string(str):
    if len(str) >=2 and str[:2] == "Is":
        return str
    return "Is" + str

print(new_string("Array"))
print(new_string("IsEmpty"))


# 20). <b> Write a Python program to get a string which is n (non-negative integer) copies of a given string </b>

# In[33]:


def larger_string(str,n):
    result = ""
    for i in range(n):
        result+= str
    return result

print(larger_string('abc',2))
print(larger_string('.py',3))


# 21). <b> Write a Python program to find whether a given number (Accept from the user) is even or odd, print out an appropriate mesage to that user </b>

# In[36]:


Input = int(input("Enter the desired number: "))
if Input%2 == 0:
    print("The entered number is Even")
else:
    print("The entered number is Odd")


# 22). <b> Write a Python program to count the number 4 in a given list </b>

# In[38]:


def count(nums):
    counter = 0
    for i in nums:
        if i ==4:
            counter+=1
    return counter

print(count([1,4,6,4,7,4]))


# 23). <b> Write a Python program to get the n copies of the first 2 characters of a given string. Return the n copies of the whole string if less than 2 </b>

# In[40]:


def sub_string(str,n):
    flen = 2
    if flen > len(str):
        flen = len(str)
    substr = str[:flen]
    
    result = ""
    for i in range(n):
        result+=substr
    return result

print(sub_string('abcdef',2))


# 24).<b> Write a Python program to test whether a passed letter is a vowel or not. </b>

# In[46]:


def Isvowel(n):
    vowels = 'aeiou'
    return n in vowels

print(Isvowel('u'))
print(Isvowel('g'))


# 25). <b> Write a Python program to check whether a specified value is contained in a group of values </b>

# In[48]:


def Isgroup (grp_data, n):
    for i in grp_data:
        if n == i:
            return True
    return False
print(Isgroup([1,3,4,5,7,3],2))


# 26). <b>Write a Python program to create a histogram from a given list of integers </b>

# In[4]:


def histogram(IntList):
    for i in IntList:
        result = ''
        times = i
        while(times > 0):
            result += '*'
            times = times-1
        print(result)
        
histogram([2,3,4,5])


# 27) <b> Write a Python program to concatenate all elements in a list into a string and return it </b>

# In[11]:


def string(strlist):
    output = ''
    for i in strlist:
        output += str(i)
    return output
string(['P','h','a','n','i'])
#string([1,2,3,4,5])


# 28) <b> Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence </b>

# In[16]:


def even(list1):
    output = ''
    for i in list1:
        if (i==237):
            print(i)
            break
        elif i%2 == 0:
            print(i)
            
even([2,4,6,7,9])


# 29) <b> Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2 </b>
#     
#  - color_list_1 = set(["White", Black", "Red"])
#  - color_list_2 = set(["Red", "Green"])

# In[17]:


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

print(color_list_1.difference(color_list_2))


# 30) <b>Write a Python program that will accept the base and height of a triange and compute the area </b>

# In[20]:


def Area_Triangle(base,height):
    Area = (1/2)*(base)*(height)
    return Area

Area_Triangle(2,10)


# 31) <b> Write a Python program to compute the GCD of two positive integers </b>

# In[24]:


def gcd(x,y):
    gcd=1
    
    if x%y == 0:
        return y
    
    for k in range(int(y/2), 0, -1):
        if x % k ==0 and y % k==0:
            gcd =k
            break
    return gcd

print(gcd(240,360))
print((gcd(12,17)))


# 32) <b> Write a Python program to get the LCM of two positive integers </b>

# In[26]:


def lcm(x,y):
    if x>y:
        z = x
    else:
        z = y
        
    while(True):
        if((z%x == 0) and (z%y == 0)):
            lcm = z
            break
        z += 1
    return lcm

print(lcm(35,60))
print(lcm(15,17))


# 33) <b> Write a Python program to sum of three given integers. However, if two values are equal sum will be zero </b>

# In[29]:


def Sum(x,y,z):
    if(x == y or y == z or z == x):
        return 0
    else:
        return x+y+z
    
print(Sum(1,2,1))
print(Sum(1,2,3))


# 34) <b> Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20 </b>

# In[32]:


def sum(x,y):
    sum = x+y
    if sum in range(15,20):
        return 20
    else:
        return sum
print(sum(10,10))
print(sum(10,9))


# 35) <b> Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5 </b>

# In[34]:


def custom(x,y):
    if (x == y or x+y == 5 or abs(x-y) == 5):
        return True
    else:
        return False

print(custom(7,2))


# 36). <b> Write a Python program to add two objects if both objects are an integer type </b>

# In[4]:


def add_numbers(x,y):
    if not (isinstance(x,int) and isinstance(y,int)):
        raise TypeError("Inputs must be integers")
        
    return x+y

print(add_numbers(4,5))


# 37). <b> Write a Python program to display your details like name, age, address in three different lines </b>

# In[8]:


def personal_details():
    name, age = "Sachin", 19
    address = "Mumbai, India"
    print("Name: {}\n Age: {}\n Address: {}".format(name,age,address))

personal_details()


# 38). <b> Write a Python program to solve (x+y)*(x+y) </b>

# In[10]:


def square(x,y):
    #result = x*x+2*x*y+y*y
    result = (x+y)*(x+y)
    return result

print(square(4,2))


# 39). <b> Write a Python program to compute the future value of a specified principal amount, rate of interest, and number of years </b>
# 
# - Test Data: amt=1000, int=3.5, years=7

# In[12]:


def future_value(a,i,y):
    
    fut_val = a*((1+(0.01*i)) ** y)
    return fut_val
    
print(future_value(10000,3.5,7))


# 40) <b> Write a Python program to compute the distance between the points (x1, y1) and (x2, y2). </b>

# In[14]:


import math

p1 = [4,6]
p2 = [2,4]

dist = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))
print(dist)


# 41) <b> Write a Python program to check whether a file exists </b>

# In[17]:


import os.path
open('abc.txt','w')
print(os.path.isfile('abc.txt'))


# 42) <b> Write a Python program to determine if a Python shell is executing in 32 bit or 64 bit on OS </b>

# In[18]:


import struct
print(struct.calcsize("P")*8)


# 43) <b> Write a Python program to get OS name, platform and release information </b>

# In[19]:


import platform
import os
print(os.name)
print(platform.system())
print(platform.release())


# 44) <b> Write a Python program to locate Python site-packages </b>

# In[20]:


import site
print(site.getsitepackages())


# 45) <b> Write a Python program to call an external command in Python </b>

# In[31]:


#import subprocess
#subprocess.run(["ls", "-l"])


# 46) <b> Write a python program to get the path and name of the file that is currently executing </b>

# In[29]:


import inspect,os
print(inspect.getfile(inspect.currentframe()))
print(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))


# 47) <b> Write a Python program to find out the number of CPUS using </b>

# In[32]:


import multiprocessing
print(multiprocessing.cpu_count())


# 48) <b> Write a Python program to parse a string to float or integer </b>

# In[34]:


n = "268.249"
print(float(n))
print(int(float(n)))


# 49) <b> Write a Python program to list all files in a directory in Python </b>

# In[41]:


"""
import glob, os
os.chdir("C:/Python")
for file in glob.glob("*.*"):
    print(file)
"""


# 50) <b> Write a Python program to print without newline or space </b>

# In[43]:


for i in range(0,10):
    print("*", end="")
print("\n")


# 51) <b> Write a Python program to determine profiling of Python programs </b>

# In[44]:


import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')


# 52) <b> Write a Python program to print to stderr </b>

# In[46]:


from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
eprint("abc", "efg", "xyz", sep="--")


# 53) <b> Write a Python program to access environment variables </b>

# In[49]:


import os

# Access all environment variables
print('*-----------------------*')
print(os.environ)
print('*------------------------*')

'''
# Access a particular environment variable
print(os.environ['HOME'])
print('*------------------------*')
print(os.environ['PATH'])
print('*-------------------------*')
'''


# 54) <b> Write a Python program to get the current username </b>

# In[50]:


import getpass
print(getpass.getuser())


# 55) <b> Write a Python program to find the local IP address using Python's stdlib </b>

# In[52]:


import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
s.close()


# 56) <b> Write a Python program to get height and width of the console window </b>

# In[54]:


'''
def terminal_size():
    import fcntl,termios,struct
    th,tw,hp,wp = struct.unpack('HHHH',
                               fcntl.ioctl(0,termios.TIOCGWINSZ,
                               struct.pack('HHH', 0,0,0,0)))
    return tw,th

print('Number of columns and rows:', terminal_size())
'''


# 57) <b> Write a Python to get execution time for a Python method </b>

# In[56]:


import time
def sum_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s+i
    end_time = time.time()
    return s,end_time-start_time

n=5
print("\n Time to sum of 1 to",n," and required time to calculate is:", sum_numbers(n))


# 58) <b> Write a Python program to find the sum of the first n positive integers </b>

# In[59]:


def Sum_n(n):
    sum_num = int((n*(n+1))/2)
    return sum_num
print(Sum_n(5))


# 59) <b> Write a Python program to convert height (in feet and inches) to centimeters </b>

# In[60]:


print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))
 
h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
 
print("Your height is : %d cm." % h_cm)


# 60) <b> Write a Python program to calculate the hypotenuse of a right angled triangle </b>

# In[62]:


from math import sqrt
print("Input the shorter sides of the triangle:")
a = float(input("a:"))
b = float(input("b:"))

c=sqrt(a**2 + b**2)
print("The length of the hypotenuse is",c)


# 61) <b> Write a Python program to convert the distance (in feet) to inches, yards, and miles </b>

# In[63]:


dist_feet = int(input("Input distance in feet: "))
dist_inches = dist_feet * 12
dist_yards = dist_feet/3.0
dist_miles = dist_feet/5280.0

print("The distance in inches is %i inches." % dist_inches)
print("The distance in yards is %.2f yards." % dist_yards)
print("The distance in miles is %.2f miles." % dist_miles)


# 62) <b> Write a Python program to convert all units of time into seconds </b>

# In[64]:


days = int(input("Input days: "))*3600*24
hours = int(input("Input hours: "))*3600
minutes = int(input("Input minutes: "))*60
seconds = int(input("Input seconds: "))

time = days+hours+minutes+seconds

print("The amount of seconds", time)


# 63) <b> Write a Python program to get an absolute filepath </b>

# In[65]:


def absolute_file_path(path_fname):
    import os
    return os.path.abspath('path_fname')
print("Absolute file path:", absolute_file_path("test.txt"))


# 64) <b> Write a Python program to get file creation and modification date/times </b>

# In[67]:


import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("abc.txt")))
print("Created: %s" % time.ctime(os.path.getctime("abc.txt")))


# 65) <b> Write a python program to convert seconds to day, hour, minutes and seconds </b>

# In[70]:


time = float(input("Input time in seconds:"))
day = time // (24*3600)
time = time % (24*3600)
hour = time //3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s -> %d:%d:%d:%d" % (day,hour,minutes,seconds))


# 66) <b> Write a Python program to calculate body mass index </b>

# In[72]:


ht = float(input("Height in meters please: "))
wt = float(input("Weight in kilogram please: "))
print("Your body mass index is: ", round(wt / (ht+wt),2))


# 67) <b> Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure </b>

# In[76]:


KiloPascals = float(input("Input pressure in Kilopascals: "))
psi = KiloPascals/6.89475729
mmhg = KiloPascals *760 /101.325
atm = KiloPascals/101.325

print("The pressure in pounds per square inch: %0.2f psi" %(psi))
print("The pressure in millimeters of mercury: %0.2f mmHg " %(mmhg))
print("Atmospheric pressure: %0.2f atm." %(atm))


# 68) <b> Write a Python program to calculate the sum of the digits in an integer </b>

# In[77]:


def getsum(n):
    sum = 0
    while(n!=0):
        sum = sum + int(n%10)
        n = int(n/10)
    return sum

print(getsum(687))


# 69) <b> Write a Python program to sort three integers without using conditional statements and loops </b>

# In[78]:


x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x,y,z)
a3 = max(x,y,z)
a2 = (x+y+z)-a1-a3

print("The numbers in sorted order: ", a1,a2,a3)


# 70) <b> Write a Python program to sort files by date </b>

# In[86]:


import glob
import os

files = glob.glob(".txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))


# 71) <b> Write a Python program to get a directory listing, sorted by creation date </b>

# In[88]:


# !/usr/bin/env python
from stat import S_IREG, ST_CTIME, ST_MODE
import os,sys,time

#path to the directory (relative or absolute)
dirpath = sys.argv[1] if len(sys.argv) == 2 else r'.'

#get all entries in the directory w/stats
entries = (os.path.join(dirpath,fn) for fn in os.listdir(dirpath))
entries = ((os.stat(path), path) for path in entries)

#leave only regular files, insert creation date
entries = ((stat[ST_CTIME], path)
          for stat, path in entries if S_ISREG (stat[ST_MODE]))

#Note: on windows 'ST_CTIME' is a creation date
#but on Unix it could be something else
#NOTE: use 'ST_MTIME' to sort by a modification date

for cdate, path in sorted(entries):
    print(time.ctime(cdate), os.path.basename(path))


# 72) <b> Write a Python program to get the details of math module </b>

# In[1]:


import math
math_ls = dir(math)      #sets everything to a list of math module.
print(math_ls)


# 73). <b> Write a Python program to calculate midpoints of a line </b>

# In[6]:


x1 = float(input('Please enter the first X_co-ordinate'))
y1 = float(input('Please enter the first Y_co-ordinate'))

x2 = float(input('Please enter the second X_co-ordinate'))
y2 = float(input('Please enter the second Y_co-ordinate'))

X_mid = (x1+x2)/2
Y_mid = (y1+y2)/2

print("Midpoint is: " ,(X_mid,Y_mid))


# 74) <b> Write a Python program to hash a word </b>

# In[7]:


a = 4
str_val = 'Cricket'
flt = 20.56

print("The integer hash value is: " + str(hash(a)))
print("The string hash value is: " + str(hash(str_val)))
print("The float hash value is: " + str(hash(flt)))


# 75) <b> Write a Python program to get the copyright information </b>

# In[8]:


import sys
copyright = sys.copyright
print('The Copyright information is:', copyright)


# 76) <b> Write a Python program to get the command-line arguments passed to a script </b>

# In[17]:


# importing the sys module
import sys
arglist = sys.argv   #command line arguments are stored in the form of list in sys.argv
print(arglist)

print(sys.argv[0])   #print the file name
print(sys.argv[1])


# 77) <b> Write a Python program to test whether the system is a big-endian platform or little-endian platform </b>

# In[18]:


import sys
if(sys.byteorder) == "little":
    print("Little-endian platform.")
else:
    print("Bin-endian platform.")


# 78) <b> Write a Python program to find the available built-in modules </b>

# In[19]:


import sys
import textwrap
module_name = ','.join(sorted(sys.builtin_module_names))
print(textwrap.fill(module_name, width =70))


# 79) <b> Write a Python program to get the size of an object in bytes </b>

# In[22]:


import sys
x = 2
print(sys.getsizeof(x))
print(sys.getsizeof(sys.getsizeof))
print(sys.getsizeof('Cricket'))


# 80) <b> Write a Python program to get the current value of the recursion limit </b>

# In[23]:


import sys
print("Current value of the recursion limit:", sys.getrecursionlimit())


# 81) <b> Write a Python program to concatenate N strings </b>

# In[36]:


list = ['Sachin', 'Ramesh', 'Tendulkar']
concat = ""
for i in list:
    concat = concat + i

print(concat)


# 82) <b> Write a Python program to calculate the sum over a container </b>

# In[38]:


s = sum([10,20,30])
print("Sum of the container: ", s)


# 83) <b> Write a Python program to test whether all numbers of a list is greater than a certain number </b>

# In[40]:


num_list = [65,78,57,45]
print(all(i>1 for i in num_list))
print(all(i>66 for i in num_list))


# 84) <b> Write a Python program to count the number of occurence of a specific character in a string </b>

# In[42]:


string = "Sachin Ramesh Tendulkar"
print(string.count("a"))


# 85) <b> Write a Python program to check whether a file path is a file or directory </b>

# In[43]:


import os
path = 'abc.txt'
if os.path.isdir(path):
    print("\nIt is a directory")
elif os.path.isfile(path):
    print("\nIt is a file")
else:
    print("It is not both")


# 86) <b> Write a Python program to get the ASCII value of a charcter </b>

# In[44]:


c = 'S'
print("The ASCII value of '" +c + "' is", ord(c))


# 87) <b> Write a Python program to get the size of a file </b>

# In[46]:


import os
file_size = os.path.getsize("abc.txt")
print("The file size is: ", file_size)


# 88) <b> Given variables x=30 and y=20, write a Python program to print "30+20=50" </b>

# In[50]:


x = 30
y = 20
print("%d+%d=%d" % (x, y,x+y))


# 89) <b> Write a Python program to perform an action if a condition is true </b>
# 
#  - Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal

# In[51]:


n = 1
if (n == 1):
    print("\nFirst day of a Month")
print()


# 90) <b> Write a Python program to create a copy of its own source code </b>

# In[53]:


print((lambda str = 'print(lambda str=%r: (str %% str))()': (str % str))())


# 91) <b> Write a Python program to swap two variables </b>

# In[54]:


def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b

swap(20,30)


# 92) <b> Write a Python program to define a string containing special characters in various forms. </b>

# In[55]:



print("\#{'}${\"}@/")
print("\#{'}${"'"'"}@/")
print(r"""\#{'}${"}@/""")
print('\#{\'}${"}@/')
print('\#{'"'"'}${"}@/')
print(r'''\#{'}${"}@/''')


# 93) <b> Write a Python program to get the identity of an object </b>

# In[56]:


# id() function is used to get the identity of any object

input = object()
obj_add = id(input)
print(obj_add)


# 94) <b> Write a Python program to convert a byte string to a list of integers </b>

# In[65]:


string = "Python is interesting."
arr = bytes(string, 'utf-8')
print(arr)


# 95) <b> Write a python program to check whether a string is numeric </b>

# In[66]:


string = 'a123'
try:
    i = float(string)
except (ValueError, TypeError):
    print("\nNot Numeric")


# 96) <b> Write a Python program to print the current call stack </b>

# In[67]:


import traceback
def f1():return abc()
def abc():traceback.print_stack()
f1()


# 97) <b> Write a Python program to list the special variables used within the language </b>

# In[68]:


s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))
print( '\n'.join(' '.join(s_var_names[i:i+8]) for i in range(0, len(s_var_names), 8)) )


# 98) <b> Write a Python program to get the system time </b>

# In[69]:


import time
print(time.ctime())


# 99) <b> Write a Python program to clear the screen or terminal </b>

# In[70]:


import os
import time
os.system('cls')


# 100) <b> Write a Python program to get the name of the host on which the routine is running </b>

# In[72]:


import socket
host_name = socket.gethostname()
#print("Host name: ", host_name)

