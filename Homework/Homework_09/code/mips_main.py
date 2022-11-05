# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:47:49 2022

@author: swamy ponpandi
course : cpsc 300 spring 2022

IMPORTANT : The code is provided as is. This code is for personal use in 
cpsc 300 spring 2022 course only. 
Do not post the code in public forums, or other unauthorized use is prohibited. The code 
author is not responsible for any such unauthorized use. 

MIPS main code 

Fetch-Decode-Execute loop

"""

import mips_ram
import mips_alu_iddec

#prompt the user to enter the address of the first instruction
#in the code to be executed
start_address_RAM = int(input('start address in RAM : '))

#set up System RAM - prompt for size of RAM in words
mips_ram.ram_configure()
#load code into RAM
mips_ram.ram_init()
#initialize program counter with address of first instruction
pc = start_address_RAM

#continue until halt instruction
while(True):
    
    #read an instruction from RAM
    instr = mips_ram.ram_mips(pc, rd_wr = 1, data = None)
    print(instr)
    #decode the instruction and execute it
    is_halt = mips_alu_iddec.mips_alu_id(instr)
    #if instruction is halt - stop
    if(not is_halt):
        print('<<<<<<<< Halting execution >>>>>>>>')
        break
    #increase program counter to next instruction
    pc = pc + 1
    
    #only for debug, remove later on
    c = input('continue - "y" or "n" -- ')
    if(c == 'n'):
        break
    
    
    