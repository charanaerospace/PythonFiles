# Write a python statement that calculates and prints the number of feet in  on 13 miles
# 1 mile = 5280 feet
# miles = int(input("Enter no of miles"))
# conversion_miles = miles * 5280
# print(conversion_miles)

# Write a program tht calculates that prints
# number of seconds in 7 hours 21 minutes 37 seconds
from cmath import pi
print((7 * 60 + 21) * 60 +37)
# perimeter of retangle is 2w+2h w,h lengths of its sides sides 
# write a python statement  tht caluclates and prints length in inches 
# of perimeter of the rectangle whose sides of length 4 and 7 inches
# w = int(input("Enter the length in inches"))
# h = int(input("Enter height in inches"))
# perimeter = (w+h) * 2
# print(perimeter)
# calculate area of rectangle
# w = int(input("Enter the w"))
# h = int(input("Enter the h"))
# area = w * h
# print(area)
# Write a python statement that calculates the  and prints circumference in inches of a circle whose radius is 8 inches
# radius = 8
# circumfernece = 2 * pi
# circle_circumfernece = circumfernece * radius 
# print(circle_circumfernece)
# Write a python program that prints the area of the circle in inches whse radius is 8 inches
r = 8 
area_circle = pi * r**2
print(area_circle)
# Given p dollars, the future value of this money when compounded yearly at a rate of r percent interest for y years is  
# p (1 + 0.01 r)^y.
# Write a Python statement that calculates and prints the value of 1000 dollars compounded at 7 percent interest for 10
# years.
p = 1000
r = 7
y = 1000
a = p * (1+0.01 * 7)**10
print(a) 

#Write a python statement that combinesthree strings "My Name is", "Joe", "Waren"
first_name = "Joe"
last_name  = "Warren"
full_name = "My Name is "+ first_name +" "+last_name+"."
print(full_name)