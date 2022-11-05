# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:39:03 2022

@author: swamy ponpandi
course : cpsc 300 spring 2022

IMPORTANT : The code is provided as is. This code is for personal use in 
cpsc 300 spring 2022 course only. 
Do not post the code in public forums, or other unauthorized use is prohibited. The code 
author is not responsible for any such unauthorized use. 

ALU
MIPS Instr decode and execution
"""
import mips_regfile

#read the instruction, decode it, and execute the instruction
#instr is a python list 
def mips_alu_id(instr):
    
    #if instruction is 'lui' 
    #example - lui $t0 0x00
    
    if(instr[0] == 'lui'):
        opr1 = instr[1] #get operand1, which is a register
        regnum = mips_regfile.Reg2Num(opr1) #convert operand1 to register number
        opr2 = instr[2] #get operand2, which is data to be loaded into register
        data = int(opr2[2:], 16) #convert operand2 from hex to integer
        
        #debug
        print('DEBUG >>>>>>>> ',instr[0], regnum, data)
        
        #write the data into appropriate register
        #shift data by 16 bits for LUI instr
        mips_regfile.RegFileAccess(datain = data << 16, reg_s1 = 0, reg_s2 = 0, 
                                   reg_d = regnum, wr = 1)
    #if instruction is 'ori' 
    #example - ori $t0, $t0, 0x56
    elif(instr[0] == 'ori'):
        
        opr1 = instr[1] #get operand1, which is a destination register
        dst_regnum = mips_regfile.Reg2Num(opr1)
        opr2 = instr[2]#get operand2, which is a source register
        src_regnum =  mips_regfile.Reg2Num(opr2)
        opr3 = instr[3] #get operand3, which is data
        data = int(opr3[2:], 16)
        
        #debug
        print("DEBUG >>>>>>>> ", instr[0], dst_regnum, src_regnum, data)
        
        #first read, the source register contents
        (d1, d2 ) = mips_regfile.RegFileAccess(datain = None, reg_s1 = src_regnum, reg_s2 = 0, 
                                   reg_d = 0, wr = 0)
        #debug
        print(d1, d2)
        
        #logical OR data with contents of source register
        result = d1 | data
        #write the result into destination register
        mips_regfile.RegFileAccess(datain = result, reg_s1 = 0, reg_s2 = 0, 
                                   reg_d = dst_regnum, wr = 1)
    #if instruction is 'addi'
    #example - addi $t0, $t0, 0x4A
    
    elif(instr[0] == 'addi'):
        
        opr1 = instr[1] #get operand1, which is a destination register
        dst_regnum = mips_regfile.Reg2Num(opr1)
        opr2 = instr[2]#get operand2, which is a source register
        src_regnum =  mips_regfile.Reg2Num(opr2)
        opr3 = instr[3] #get operand3, which is data
        data = int(opr3[2:], 16)
        
        #debug
        print("DEBUG >>>>>>>> ", instr[0], dst_regnum, src_regnum, data)
        
        #first read, the source register contents
        (d1, d2 ) = mips_regfile.RegFileAccess(datain = None, reg_s1 = src_regnum, reg_s2 = 0, 
                                   reg_d = 0, wr = 0)
        #debug
        print(d1, d2)
        
        #add data with contents of source register
        result = d1 + data
        #write the result into destination register
        mips_regfile.RegFileAccess(datain = result, reg_s1 = 0, reg_s2 = 0, 
                                   reg_d = dst_regnum, wr = 1)
    #if instruction is 'add'
    #example - add $s0, $t0, $t1
    elif(instr[0] == 'add'):
        
        opr1 = instr[1] #get operand1, which is a destination register
        dst_regnum = mips_regfile.Reg2Num(opr1)
        opr2 = instr[2]#get operand2, which is a source register
        src_regnum1 =  mips_regfile.Reg2Num(opr2)
        opr3 = instr[3] #get operand3, which is a source register
        src_regnum2 =  mips_regfile.Reg2Num(opr3)
        
        #debug
        print("DEBUG >>>>>>>> ", instr[0], dst_regnum, src_regnum1, src_regnum2)
        
        #first read, the source register contents
        (d1, d2 ) = mips_regfile.RegFileAccess(datain = None, reg_s1 = src_regnum1, reg_s2 = src_regnum2, 
                                   reg_d = 0, wr = 0)
        #debug
        print(d1, d2)
        
        #ADD data of contents of source registers
        result = d1 + d2
        #write the result into destination register
        mips_regfile.RegFileAccess(datain = result, reg_s1 = 0, reg_s2 = 0, 
                                   reg_d = dst_regnum, wr = 1)
    #if instruction is 'sub'
    #example - sub $s1, $s0, $t1
    elif(instr[0] == 'sub'):
        opr1 = instr[1] #get operand1, which is a destination register
        dst_regnum = mips_regfile.Reg2Num(opr1)
        opr2 = instr[2]#get operand2, which is a source register
        src_regnum1 =  mips_regfile.Reg2Num(opr2)
        opr3 = instr[3] #get operand3, which is a source register
        src_regnum2 =  mips_regfile.Reg2Num(opr3)
        
        #debug
        print("DEBUG >>>>>>>> ", instr[0], dst_regnum, src_regnum1, src_regnum2)
        
        #read the source register contents
        (d1, d2 ) = mips_regfile.RegFileAccess(datain = None, reg_s1 = src_regnum1, reg_s2 = src_regnum2, 
                                   reg_d = 0, wr = 0)
        #debug
        print(d1, d2)
        
        #subtract data of contents of source registers
        result = d1 - d2
        #write the result into destination register
        mips_regfile.RegFileAccess(datain = result, reg_s1 = 0, reg_s2 = 0, 
                                   reg_d = dst_regnum, wr = 1)
    #if instruction is 'and'
    #example - and $s2 $s0 $t1
    elif(instr[0] == 'and'):
        opr1 = instr[1] #get operand1, which is a destination register
        dst_regnum = mips_regfile.Reg2Num(opr1)
        opr2 = instr[2]#get operand2, which is a source register
        src_regnum1 =  mips_regfile.Reg2Num(opr2)
        opr3 = instr[3] #get operand3, which is a source register
        src_regnum2 =  mips_regfile.Reg2Num(opr3)
        
        #debug
        print("DEBUG >>>>>>>> ", instr[0], dst_regnum, src_regnum1, src_regnum2)
        
         #read the source register contents
        (d1, d2 ) = mips_regfile.RegFileAccess(datain = None, reg_s1 = src_regnum1, reg_s2 = src_regnum2, 
                                   reg_d = 0, wr = 0)
        #debug
        print(d1, d2)
        
        #logical AND of the source registers, store in result
        result = d1 & d2
        #write the result into destination register
        mips_regfile.RegFileAccess(datain = result, reg_s1 = 0, reg_s2 = 0, 
                             reg_d = dst_regnum, wr = 1)
    #if instruction is 'or'
    #example - or $s3 $t1 $t0
    elif(instr[0] == 'or'):
        opr1 = instr[1] #get operand1, which is a destination register
        dst_regnum = mips_regfile.Reg2Num(opr1)
        opr2 = instr[2]#get operand2, which is a source register
        src_regnum1 =  mips_regfile.Reg2Num(opr2)
        opr3 = instr[3] #get operand3, which is a source register
        src_regnum2 =  mips_regfile.Reg2Num(opr3)
        
        #debug
        print("DEBUG >>>>>>>> ", instr[0], dst_regnum, src_regnum1, src_regnum2)
        
         #read the source register contents
        (d1, d2 ) = mips_regfile.RegFileAccess(datain = None, reg_s1 = src_regnum1, reg_s2 = src_regnum2, 
                                   reg_d = 0, wr = 0)
        #debug
        print(d1, d2)
        
        #logical OR of the source registers, store in result
        result = d1 | d2
        #print(result)
        
        #write the result into destination register
        mips_regfile.RegFileAccess(datain = result, reg_s1 = 0, reg_s2 = 0, 
                                   reg_d = dst_regnum, wr = 1)
    #if instruction is 'andi'
    #example - andi $s4 $s3 0x87
    elif(instr[0] == 'andi'):
        opr1 = instr[1] #get operand1, which is a destination register
        dst_regnum = mips_regfile.Reg2Num(opr1)
        opr2 = instr[2]#get operand2, which is a source register
        src_regnum =  mips_regfile.Reg2Num(opr2)
        opr3 = instr[3] #get operand3, which is data
        data = int(opr3[2:], 16)
        
        print("DEBUG >>>>>>>> ", instr[0], dst_regnum, src_regnum, data)
        
        #read the source register contents
        (d1, d2 ) = mips_regfile.RegFileAccess(datain = None, reg_s1 = src_regnum, reg_s2 = 0, 
                                    reg_d = 0, wr = 0)
        #debug
        print(d1, d2)
        
        #logical AND data with contents of source register, store in result
        result = d1 & data
        #write the result into destination register
        mips_regfile.RegFileAccess(datain = result, reg_s1 = 0, reg_s2 = 0, 
                                    reg_d = dst_regnum, wr = 1)
    #if instruction is 'sll'
    #example - sll $t5 $t0 2
    elif(instr[0] == 'sll'):
        opr1 = instr[1] #get operand1, which is a destination register
        dst_regnum = mips_regfile.Reg2Num(opr1)
        opr2 = instr[2]#get operand2, which is a source register
        src_regnum =  mips_regfile.Reg2Num(opr2)
        opr3 = instr[3] #get operand3, which is data
        data = int(opr3) #power that 2 will be raised to to achieve shift left
        
        print("DEBUG >>>>>>>> ", instr[0], dst_regnum, src_regnum, data)
        
        #read the source register contents
        (d1, d2 ) = mips_regfile.RegFileAccess(datain = None, reg_s1 = src_regnum, reg_s2 = 0, 
                                    reg_d = 0, wr = 0)
        #debug
        print(d1, d2)
        
        #multiply contents of d1 by 2^data to achieve shift, store in result
        result = d1 * (2**data)
        #write the result into destination register
        mips_regfile.RegFileAccess(datain = result, reg_s1 = 0, reg_s2 = 0, 
                                    reg_d = dst_regnum, wr = 1)
    #if instruction is 'srl'
    #example - srl $t4 $s5 2
    elif(instr[0] == 'srl'):
        opr1 = instr[1] #get operand1, which is a destination register
        dst_regnum = mips_regfile.Reg2Num(opr1)
        opr2 = instr[2]#get operand2, which is a source register
        src_regnum =  mips_regfile.Reg2Num(opr2)
        opr3 = instr[3] #get operand3, which is data
        data = int(opr3) #power that 2 will be raised to to achieve shift right
        
        print("DEBUG >>>>>>>> ", instr[0], dst_regnum, src_regnum, data)
        
        #read the source register contents
        (d1, d2 ) = mips_regfile.RegFileAccess(datain = None, reg_s1 = src_regnum, reg_s2 = 0, 
                                    reg_d = 0, wr = 0)
        #debug
        print(d1, d2)
        
        #floor division of contents of d1 by 2^data to achieve shift, store in result
        result = d1 // (2**data)
        #write the result into destination register
        mips_regfile.RegFileAccess(datain = result, reg_s1 = 0, reg_s2 = 0, 
                                    reg_d = dst_regnum, wr = 1)
    #if instruction is 'slt'
    #example - slt $t6 $s0 $t5
    elif(instr[0] == 'slt'):
        opr1 = instr[1] #get operand1, which is a destination register
        dst_regnum = mips_regfile.Reg2Num(opr1)
        opr2 = instr[2]#get operand2, which is a source register
        src_regnum1 =  mips_regfile.Reg2Num(opr2)
        opr3 = instr[3] #get operand3, which is a source register
        src_regnum2 =  mips_regfile.Reg2Num(opr3)
        
        #debug
        print("DEBUG >>>>>>>> ", instr[0], dst_regnum, src_regnum1, src_regnum2)
        
         #read the source register contents
        (d1, d2 ) = mips_regfile.RegFileAccess(datain = None, reg_s1 = src_regnum1, reg_s2 = src_regnum2, 
                                   reg_d = 0, wr = 0)
        #debug
        print(d1, d2)
        
        #if source 1 contents are less than source 2 contents, result = 1
        if (d1 < d2):
            result = 1
        else:
            result = 0
        #write the result into destination register
        mips_regfile.RegFileAccess(datain = result, reg_s1 = 0, reg_s2 = 0, 
                                    reg_d = dst_regnum, wr = 1)
    #if instruction is 'slti'
    #example - slti $t7 $t0 0x46
    elif(instr[0] == 'slti'):
        opr1 = instr[1] #get operand1, which is a destination register
        dst_regnum = mips_regfile.Reg2Num(opr1)
        opr2 = instr[2]#get operand2, which is a source register
        src_regnum =  mips_regfile.Reg2Num(opr2)
        opr3 = instr[3] #get operand3, which is data
        data = int(opr3[2:], 16)
        
        #debug
        print("DEBUG >>>>>>>> ", instr[0], dst_regnum, src_regnum, data)
        
         #read the source register contents
        (d1, d2 ) = mips_regfile.RegFileAccess(datain = None, reg_s1 = src_regnum, reg_s2 = 0, 
                                   reg_d = 0, wr = 0)
        #debug
        print(d1, d2)
        
        #if source 1 contents are less than source 2 contents, result = 1
        if (d1 < data):
            result = 1
        else:
            result = 0
        #write the result into destination register
        mips_regfile.RegFileAccess(datain = result, reg_s1 = 0, reg_s2 = 0, 
                                    reg_d = dst_regnum, wr = 1)    
    elif(instr[0] == 'halt'):
        return 0
        
    return 1
   
        
        