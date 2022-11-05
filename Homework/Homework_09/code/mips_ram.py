# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:17:31 2022

@author: swamy ponpandi
course : cpsc 300 spring 2022

IMPORTANT : The code is provided as is. This code is for personal use in 
cpsc 300 spring 2022 course only. 
Do not post the code in public forums, or other unauthorized use is prohibited. The code 
author is not responsible for any such unauthorized use. 

System RAM definition

"""
#RAM for MIPS
#RAM is a python List of instrs/data

#this is the global RAM array
RAMArray = [] #initially empty

#function to read/write to RAM
#addr - address from which to read/write 
#data - if read, set data = None and RAM contents will be returned by the function; 
#       if write, set data to the value to be written at address
# rd_wr = 1 for read data from RAM
# rd_wr = 0 for write data to RAM 
def ram_mips(addr, rd_wr, data):
    
    global RAMArray
    
    if(rd_wr):
       # print(RAMArray[addr])
        return RAMArray[addr]  #read data from RAM
    else:
        RAMArray[addr] = data #write data to RAM
        return None

#function to configure RAM 
#prompts user to input the RAM size
def ram_configure():
    
    global RAMArray
    
    ramsz = int(input('enter the size of RAM (in words) : '))
    
    RAMArray = [0] * ramsz
 
    #print(RAMArray)

#function to initialize RAM with instr/data
# Must provide a text file - ramcontents.txt with instructions and data
# Text file MUST be in the same directory as this code file
# Format of text file (need a space between each of the below)
# ram_addr opcode <operand1> <operand2> ...
# Example
# 10 lui $t0 0x0
# 11 ori $t0 $t0 0x40
# 12 add $t0 $t0 $t1
def ram_init():
    
    global RAMArray
    #open the ram text file
    ramfile = open("ramcontents.txt", "r")
    #read until empty
    while(True):
	    #read next line
        line = ramfile.readline()
        #strip begin/end spaces/newlines
        line = line.strip()
    
        #line is empty, done with file
        if not line or line == '':
            break
        
        #unpack into line number(addr), instr/data
        line_num, *instr_data = line.split()
        #load into RAM list
        RAMArray[int(line_num)] = instr_data
        #print('DEBUG >>>>>>>> ', line_num, instr_data)
        
    #close file
    ramfile.close

########################################################
# Main driver code
########################################################


# ram_configure() #specify size
# ram_init() #read file and fill array aka "ram"

# #test RAM
# pc = 10
# print(ram_mips(addr = pc, rd_wr = 1, data = None))
# pc=11
# print(ram_mips(addr = pc, rd_wr = 1, data = None))
# pc = 13
# ram_mips(addr = pc, rd_wr = 0, data = '0x45ABC')
# pc = 13
# print(ram_mips(addr = pc, rd_wr = 1, data = None))



