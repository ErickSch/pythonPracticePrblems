
# Print()
#Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are
def twinkle():
    print("Twinkle, twinkle, little star, \n\tHow I  wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")



# Python version
def pyVersion():
    import sys
    print(sys.version)



# Display date and time
def dateTime():
    import datetime
    x = datetime.datetime.now()
    print(x)



#Accepts radius and gives area
def circleArea():
    r = float(input('Radius: '))
    area = 3.1416 * r**2
    print(area)



# First and Last name in reverse order
def reverseName():
    fName = input("First Name: ")
    lName = input("Last name: ")
    print(lName, fName)



# Sequence of numbers into list & tuple
def seqNum():
    x = input("Sequence of numbers: ")
    li = list(x.split(","))
    tup = tuple((li))
    print("List: ", li)
    print("Tuple: ", tup)



# Separate filename and extension
def fileName():
    f = input("Filename: ")
    sep = f.split(".")
    print("Filename: ", sep[0])
    print("Extension: ", sep[-1])



# Firs and last color of the list: color_list = ["Red","Green","White" ,"Black"]
def colorsAcc():
    color_list = ["Red","Green","White" ,"Black"]
    print(color_list[0], color_list[-1])



# Display the date of examination: exam_st_date = (11, 12, 2014) = 11 / 12 / 2014
def date():
    exam_st_date = (11, 12, 2014)
    print("The examination will start from: %i / %i / %i"%(exam_st_date))



#Input a number(n) and print(n+nn+nnn)
def numberN(): 
    x = int(input("Integer: "))
    num1 = "%i"%(x)
    num2 = "%i%i"%(x,x)
    num3 = "%i%i%i"%(x,x,x)
    num = int(num1) + int(num2) + int(num3)
    print(type(num))



# Print the documents of Python built-in functions
def absVal():
    print(abs.__doc__)



# Print calendar of given month and year
def calendar():
    import calendar
    month = input("Month: ")
    year = input("Year: ")
    print(calendar.month(int(year), int(month)))



# Print()
#a string that you "don't" have to escape
# This
# is a ....... multi-line
# heredoc string --------> example
def aString():
    print('a string that you "don\'t" have to escape \nThis \nis a ....... multi-line \nheredoc string --------> example')
    print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""") 



#Calculate the number of days between two dates : (2014, 7, 2), (2014, 7, 11)
def twoDates():
    from datetime import date
    fDate = date(2014, 7, 2)
    lDate = date(2014, 7, 11)
    diffDays = lDate - fDate
    print(diffDays.days)



# calculate the volume of a sphere
def sphere():
    r = float(input("Radius: "))
    vol = (3.1416)*4/3 * r**3
    print(vol)



# Get the difference between n and 17, if greater than 17 return double the absolute difference
def diffSeventeen(x):
    if x < 17:
        return(17 - x)
    elif x > 17:
        return abs((17 - x) * 2)



# Test whether a number is within 100 of 1000 or 2000
def numWithin(i):
    for n in range(900,1101):
        if i == n:
            return "Your number is within 1000"
    for nn in range(1900,2101):
        if i == nn:
            return "Your number is within 2000"
    else:
        return("Wrong number")



# Calculate the sum of three numbers, if values are equal return three times of their sum
def threeSum(n0, n1, n2):
    print("The sum is: ", n0 + n1 + n2)
    if n0 == n1 == n2:
        return n0 * 3
    else:
        return "Numbers not equal"



# Get a new string from a given string where "Is" in beginning. If string already begins 
#   with "Is" return the string unchanged.
def isString(s):
    i = "Is"
    if s[:2] == "Is":
        return s
    else:
        return "Is " + s
        # newS = "Is {}"
        # return newS.format(s)


    
# Get a string which is n (non-negative integer) copies of a given string
def n_nCopy(sr, n):
    result = ""
    for i in range(n):
        result += sr
    return result



# Find whether a given number (accept from the user) is even or odd
def fNumber ():
    num = float(input("Number: "))
    if num % 2 == 0:
        print("Your number is evenly even :)")
    elif num % 2 == 1:
        print("Your number is oddly odd :)")



# Write a Python program to count how many number 4 in a given list.
def num_4s():
    l = input("List of numbers: ")
    l = l.split(",")
    howM = len(l)
    for n in l:
        if n != ' 4':
            howM -= 1
        else:
            howM = howM
    print(howM)
            
            #
def num_4s0(nums):
    howM = 0
    for n in nums:
        if n == "4" or n == " 4" or n == 4:
            howM += 1
        else:
            howM = howM
    return howM



# Get the n (non-negative integer) copies of the first 2 characters of a given string. 
#   Return the n copies of the whole string if the length is less than 2
def nStr(st, nn):
    cSrt = ""
    fTwo = st[0:2]
    if len(st) <= 2:
        cSrt += st
    for i in range(nn):
        cSrt += fTwo
    return cSrt



# Test whether a passed letter is a vowel or not.
def vowels(vowel):
    lVowels = ['a', 'e', 'i', 'o', 'u']
    uVowels = ['A', 'E', 'I', 'O', 'U']
    for l in lVowels:
        if l == vowel:
            return "Yes, it's a vowel"
    for l in uVowels:
        if l == vowel:
            return "Yes, it's a vowel"
    else:
        return "Nope, not a vowel"
            
            #
def isVowel(vowel):
    vowels = "aeiou"
    return vowel in vowels



# Check whether a specified value is contained in a list of values
def values(vList, vFind):
    return vFind in vList



# Create a histogram from a given list of integers
def histogram(lInt):
    for n in lInt:
        print("*" * n)

# histogram([1,10,3,6,35,33,11])


# Concatenate all elements in a list into a string and return it
def conc(eList):
    nStr = ""
    for e in eList:
        nStr += str(e)
    return nStr



# Print all even numbers from a given number-list in the same order and stop the printing 
#   if any numbers that come after 237 in the sequence.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
def allEven():
    eList = []
    for e in numbers:
        if e % 2 == 0:
            eList.append(e)
        elif e == 237:
            eList.append(e)
            print(eList)
            break



# Print out a set containing all the colors from color_list_1 which are 
#   not present in color_list_2
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
def lColors():
    print(color_list_1.difference(color_list_2))



# A program that will accept the base and height of a triangle and compute the area
def aTriangle(b, h):
    area = (b * h)/2
    return area



# A program to compute the greatest common divisor (GCD) of two positive integers
def commonDiv(int1, int2):
    mini = 0
    gcdList = []
    if int1 <= int2:
        mini = int1
    else:
        mini = int2
    for m in range(mini + 1):
        if m == 0:
            continue
        if int1 % m == 0 and int2 % m == 0:
            gcdList.append(m)
    return gcdList[-1]



# A program to get the least common multiple (LCM) of two positive integers
def commonMult(int1, int2 ): 
    mulList = []
    maxMult = int(int1 * int2)
    for mul in range(maxMult):
        if mul == 0:
            continue
        if mul % int1 == 0 and mul % int2 == 0:
            mulList.append(mul)
            return mulList[-1]
    if len(mulList) == 0:
        mulList = int1 * int2
    return mulList

        #
def lcm(x1, x2):
    if x1 > x2:
        x = x1
    else:
        x = x2
    while True:
        if x % x1 == 0 and x % x2 == 0:
            return x
        x += 1



# A program to sum of three given integers. However, if two values are equal sum will be zero
def sumOfThree(i1, i2, i3):
    if i1 == i2 or i1 == i3 or i3 == i2:
        ans = 0
    else:
        ans = i1 + i2 + i3
    return ans



# A program to sum two given integers. However, if the sum is between 15 to 20 it will return 20
def twoSum(in1, in2):
    result = in1 + in2
    if result in range(15, 20):
        result = 20
    return result



# Return true if the two given integer values are equal or their sum or difference is 5.
def sumInt(int1, int2):
    if int1 == int2 or int1 + int2 == 5 or abs(int1 - int2) == 5:
        return True
    else:
        return False



# Display your details like name, age, address in three different lines.
def perData(name, age, country):
    pData = "Name: {}\nAge: {}\nCountry: {}"
    return pData.format(name, age, country)



# Write a Python program to add two objects if both objects are an integer type.
def intType(ob1, ob2):
    if type(ob1) == int and type(ob2) == int:
        return ob1 + ob2
    else: 
        return False

        #
        
def isIns(o1, o2):
    if isinstance(o1, int) and isinstance(o2, int):
        return o1 + o2
    else:
        return False
        
        #

def isInst(int1, int2):
    if not isinstance(int1, int) and isinstance(int2, int):
        raise TypeError("Must be integers")
    return int1 + int2



# Write a Python program to solve (x + y) * (x + y)
def multip(x, y):
    eq = "({} + {}) ^ 2) = {}"
    res = (x + y) ** 2
    return eq.format(x, y, res)



# A compute the future value of a specified principal amount, rate of interest, 
# and a number of years

# Test Data : amt = 10000, int = 3.5, years = 7
# Expected Output : 12722.79

def interests(pAm, int, years):
    total = pAm
    for i in range(years):
        toAdd = (int * 0.01) * total
        total += toAdd
    result = "Amount: ${}\nInterest: {}%\nYears: {}\nTotal: ${}"
    return result.format(pAm, int, years, round(total, 2))

# print(interests(950, 7, 3))

# 58. A program to find the sum of the first n positive integers. (Mejorado)
def firstPos(min, max):
    nums = range(min, max)
    answ = ((len(nums)+1) * (max + min))
    answ = float(answ) / 2 
    return answ



# Write a Python program to convert height (in feet and inches) to centimeters
def height():
    hFeet = float(input("Feet: "))
    hInches = float(input("Inches: "))
    fcm = hFeet * 30.48
    icm = hInches / 0.393701
    print("Height: ", round(fcm + icm))



# Write a Python program to convert the distance (in feet) to inches, yards, and miles.
def disInft():
    disFt = float(input("Input distance in feet: "))
    toIn = round(disFt * 12, 2)
    toYd = round(disFt / 3, 2)
    toMi = round(disFt / 5280, 2)
    result = "Distance: {} ft\nInches: {} in\nYards: {} yd\nMiles: {} mi"
    print(result.format(disFt, toIn, toYd, toMi))



# Write a Python program to convert all units of time into seconds
def toSec():
    time = input("Inset time: ")
    timeL = time.split(" ")
    if len(timeL) == 2:
        if "hour" in timeL or "hours" in timeL or "h" in timeL:
            seconds = float(timeL[0]) * 3600
        elif "minute" in timeL or "minutes" in timeL or "min" in timeL or "mins" in timeL:
            seconds = timeL[0] * 60
    elif len(timeL) > 2:
        seconds = (float(timeL[0]) * 3600) + (float(timeL[-2]) * 60)
    print("Time: ", seconds, " sec")



# How many times a letter repeats on a sentence
def howM(sent, lett):
    lettTimes = 0
    for l in sent:
        if l == lett:
            lettTimes += 1
    return lettTimes



# 



# 



# 



# 







#https://www.w3resource.com/python-exercises/python-basic-exercises.php
