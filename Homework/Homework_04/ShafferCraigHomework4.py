# -*- coding: utf-8 -*-
####################################################
# Homework 2.2: Chapter 2
# author: Craig Shaffer
# date revision: 2/1/22
# course: CPSC 300
#
# Question 3 - Binary to Decimal and Decimal to Binary
#
# Question 4 - Hexadecimal to Binary and Binary to Hexadecimal
#
# test code is commented out, uncomment what you
# need to. I also included a user input test to try
# other values for the functions.
#
####################################################

#### Question 3 - Binary to Decimal and Decimal to Binary ####
# Q3 part 1: binary to decimal function
# input the binary number as an int or string
def bin_to_dec(num):
    num = str(num)
    decNum = 0 #used to store decimal value
    for bit in num: #iterate through the bits of the binary string
        decNum = decNum*2       
        if bit == '1': #checks if bit is a 1 and adds one if it is
            decNum = decNum + 1
    return decNum #returns the decimal conversion of the binary number

### test code for binary to decimal ###
# input decimal number as a string or an integer
# number1 = '1010'
# number2 = '11100110'
# number3 = 1111

# print(number1,"converted to decimal is:",bin_to_dec(number1))
# print(number2,"converted to decimal is:",bin_to_dec(number2))
# print(number3,"converted to decimal is:",bin_to_dec(number3))

##test with user input   
# userInp = input("Enter a binary number to convert to decimal:")
# print(userInp,"in decimal is", bin_to_dec(userInp))

# Q3 part 2: decimal to binary function
# input the decimal number as an int or string
def dec_to_bin(num):
    num = int(num)
    a = 1 #variable to store placement (1 is the 1s, 10 would be the 2s, 100 would be 4s, etc)
    binNum = 0 #store binary value
    while (num != 0): # loop until the number is not equal to zero from repeated divisions
        remainder = num % 2 #store and calculate the remainder of dividing by 2
        num = num // 2 #divide by 2
        binNum = binNum + (a*remainder) #add a*remainder to binNum
        a = a * 10 #multiply by 10 to 
    return binNum #return the binary conversion

### test code for decimal to binary ###
# decNum1 = 15
# decNum2 = "9"
# decNum3 = 100

# print(decNum1,"converted to binary is:",dec_to_bin(decNum1))
# print(decNum2,"converted to binary is:",dec_to_bin(decNum2))
# print(decNum3,"converted to binary is:",dec_to_bin(decNum3))

##test with user input   
# userInp2 = input("Enter a decimal number to convert to binary:")
# print(userInp2,"in binary is", dec_to_bin(userInp2))

#### Question 4 - Hexadecimal to Binary and Binary to Hexadecimal ####
# Q4 part 1: Hexadecimal to Binary
# input hexadecimal number as a string
def hex_to_bin(num):
    binNum='' #empty string to store binary string converted from hex
    i=0 #index counter
    while i<(len(num)): #iterates through each hex digit
        #checks hex digit and converts it to 4 bit binary conversion and adds it to binNum
        if num[i] == '0':
            binNum=binNum+'0000'
        elif num[i] == '1':
            binNum=binNum+'0001'
        elif num[i] == '2':
            binNum=binNum+'0010'
        elif num[i] == 3:
            binNum=binNum+'0011'
        elif num[i] == '4':
            binNum=binNum+'0100'
        elif num[i] == '5':
            binNum=binNum+'0101'
        elif num[i] == '6':
            binNum=binNum+'0110'
        elif num[i] == '7':
            binNum=binNum+'0111'
        elif num[i] == '8':
            binNum=binNum+'1000'
        elif num[i] == '9':
            binNum=binNum+'1001'
        elif num[i] == 'A' or num[i] == 'a':
            binNum=binNum+'1010'
        elif num[i] == 'B' or num[i] == 'b':
            binNum=binNum+'1011'
        elif num[i] == 'C' or num[i] == 'c':
            binNum=binNum+'1100'
        elif num[i] == 'D' or num[i] == 'd':
            binNum=binNum+'1101'
        elif num[i] == 'E' or num[i] == 'e':
            binNum=binNum+'1110'
        elif num[i] == 'F' or num[i] == 'f':
            binNum=binNum+'1111'
        i=i+1 #updates index counter
    return binNum #returns the converted binary number

### test code for hexadecimal to binary ###
# hexNum1 = "f90"
# hexNum2 = "1E7"
# hexNum3 = "F0F1"

# print(hexNum1,"converted to binary is:",hex_to_bin(hexNum1))
# print(hexNum2,"converted to binary is:",hex_to_bin(hexNum2))
# print(hexNum3,"converted to binary is:",hex_to_bin(hexNum3))

##test with user input   
# userInp3 = input("Enter a hexadecimal number to convert to binary:")
# print(userInp3,"in binary is", hex_to_bin(userInp3))

# Q4 part 2: Binary to Hexadecimal
# input binary number as a string or an integer
def bin_to_hex(num):
    num=str(num)
    check4=False #flag to see if binary number can be broken into 4 bit strings
    hexNum='' #will store bin
    temp='' #will store 4 bit strings for conversion
    count=0 #will be used to keep track of number of bits
    while check4==False: #while loop to determine if string is a multiple of 4 
        if len(num)%4==0:
            check4=True
        else:
            num='0'+num #adds leading 0s until string is a multiple of 4 long
    for bit in num: #iterates through each bit
        temp=temp+bit #stores bit into a temp variable
        count=count+1 #updates counter by 1
        if count==4: #if the string is 4 bits long, convert to hex and add to hexNum string
            if temp == '0000':
               hexNum=hexNum+'0'
            elif temp == '0001':
                hexNum=hexNum+'1'
            elif temp == '0010':
                hexNum=hexNum+'2'
            elif temp == '0011':
                hexNum=hexNum+'3'
            elif temp == '0100':
                hexNum=hexNum+'4'
            elif temp == '0101':
                hexNum=hexNum+'5'
            elif temp == '0110':
                hexNum=hexNum+'6'
            elif temp == '0111':
                hexNum=hexNum+'7'
            elif temp == '1000':
                hexNum=hexNum+'8'
            elif temp == '1001':
                hexNum=hexNum+'9'
            elif temp == '1010':
                hexNum=hexNum+'A'
            elif temp == '1011':
                hexNum=hexNum+'B'
            elif temp == '1100':
                hexNum=hexNum+'C'
            elif temp == '1101':
                hexNum=hexNum+'D'
            elif temp == '1110':
                hexNum=hexNum+'E'
            elif temp == '1111':
                hexNum=hexNum+'F'
            count=0 #reset counter
            temp='' #reset temp string
    return hexNum #return the hexadecimal conversion

### test code for binary to hexadecimal ###
# binNum1="1010"
# binNum2=100101
# binNum3=101100101110

# print(binNum1,"converted to hexadecimal is:",bin_to_hex(binNum1))
# print(binNum2,"converted to hexadecimal is:",bin_to_hex(binNum2))
# print(binNum3,"converted to hexadecimal is:",bin_to_hex(binNum3))

## test with user input         
# userInp4 = input("Enter a binary number to convert to hexadecimal:")
# print(userInp4,"in hexadecimal is", bin_to_hex(userInp4))




