# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 20:33:00 2022

@author: swamy ponpandi
course : cpsc 300 spring 2022

IMPORTANT : The code is provided as is. This code is for personal use in 
cpsc 300 spring 2022 course only. 
Do not post the code in public forums, or other unauthorized use is prohibited. The code 
author is not responsible for any such unauthorized use. 

Register file
"""
#Register file
#List of 32 integers
RegFileArray = [0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0]

#dictionary containing map between register name(strings) and register number
Register2Num = {'$zero':0, '$at':1, '$v0': 2, '$v1':3, '$a0':4, '$a1':5, '$a2':6,
                '$a3':7, '$t0':8, '$t1':9, '$t2':10, '$t3':11,'$t4':12, '$t5':13,
                '$t6':14, '$t7':15,'$s0':16, '$s1':17,'$s2':18, '$s3':19, 
                '$s4':20, '$s5':21,'$s6':22, '$s7':23,'$t8':24, '$t9':25,
                '$k0':26, '$k1':27, '$gp':28, '$sp':29, '$fp':30, '$ra':31}
#dictionary containing map between register number and register name
Num2Register = {0:'$zero', 1:'$at', 2:'$v0', 3:'$v1', 4:'$a0', 5:'$a1', 6:'$a2',
                7:'$a3', 8:'$t0', 9:'$t1', 10:'$t2', 11:'$t3', 12:'$t4', 13:'$t5',
                14:'$t6', 15:'$t7', 16:'$s0', 17:'$s1', 18:'$s2', 19:'$s3', 
                20:'$s4', 21:'$s5', 22:'$s6', 23:'$s7', 24:'$t8', 25:'$t9',
                26:'$k0', 27:'$k1', 28:'$gp', 29:'$sp', 30:'$fp', 31:'$ra'}
#function to convert register name to register number 
def Reg2Num(reg):
    global Register2Num
    
    return Register2Num[reg]

#function to convert register number to register name
def Num2Reg(num):
    global Num2Register
    
    return Num2Register[num]

#Function for MIPS 32-bit register file
#reg_s1 - 5-bit (0 to 31) : indicates which source 1 register is read (default = 0)
#reg_s2 - 5-bit (0 to 31) : indicates which source 2 register is read (default = 0)
#reg_d - 5-bit (0 to 31) : indicates which destination register is written to (default = 13)
# wr = 1 writes datain value to reg_d register
def RegFileAccess( datain, reg_s1 = 0, reg_s2 = 0, reg_d = 0, wr = 0,):
    
    #Register file
    global RegFileArray
    #read data from reg_s1, reg_s2 
    dataout_s1 = RegFileArray[reg_s1]
    dataout_s2 = RegFileArray[reg_s2]
    #if write signal = 1, only then write into reg_d
    if(wr):
        #as long as destination(regd is not 0 ($zero), datain is written into RegFileArray[reg_d]
        if reg_d != 0:    
            RegFileArray[reg_d] = datain
    #print reg file contents for debugging
    print_reg_file()
    #return data in reg_s1, reg_s2 as a tuple
    return (dataout_s1, dataout_s2)

def print_reg_file():
    #Register file
    global RegFileArray
    
    print('<<<<<<<<<<<<<RegFile>>>>>>>>>>>>>>>')
    for r in range(32):
        print('Reg[',r,'] = ', RegFileArray[r], end=' ')
    print('')  

# ################# MIPS - 32 BIT Implementation ###########################
# #initial data in register file    
# RegFileAccess(datain = 0, reg_s1 = 0, reg_s2 = 0, reg_d = 0, wr = 0)
# #write 23 to regster 13
# RegFileAccess(datain = 23, reg_s1 = 0, reg_s2 = 0, reg_d = 13, wr = 1)
# #write 35 to regster 12
# RegFileAccess(datain = 35, reg_s1 = 0, reg_s2 = 0, reg_d = 12, wr = 1)
# #read register 12, 13 and print contents
# #note : datain and reg_d values does not matter
# r1 = 12
# r2 = 13
# (d1, d2 ) = RegFileAccess(datain = 23, reg_s1 = r1, reg_s2 = r2, 
#                           reg_d = 13, wr = 0)
# print('reg[', r1,'] = ', d1)
# print('reg[', r2,'] = ', d2)


####### test code for HW8 modifications #######
## testing Num2Reg
# print(Num2Reg(18)) #will print $s2 in console
# print(Num2Reg(0)) #will print $zero in console

## testing the ability to write into $zero
#initial data in register file (all registers are empty)
# RegFileAccess(datain = 0, reg_s1 = 0, reg_s2 = 0, reg_d = 0, wr = 0) 
#attempting to write 8 into register 0 ($zero) 
#Note: $zero should still have 0 and not 8 because of our modifications
# RegFileAccess(datain = 8, reg_s1 = 0, reg_s2 = 0, reg_d = 0, wr = 1)
#showing that it still writes if reg_d is not 0
#register 6 should contain 8
# RegFileAccess(datain = 8, reg_s1 = 0, reg_s2 = 0, reg_d = 6, wr = 1)
