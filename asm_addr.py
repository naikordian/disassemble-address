#!/usr/bin/python3
import sys
import re
from os import path


def isASM(code):
    code_list=["dadd","dadd.b","addc.b"]
    if any( code in s for s in code_list):
        return True
    else:
        return False

def countMachineCode(line):
    r=re.compile("[0-9a-fA-F]{4}")
    nlist = list(filter(r.match,line.split()))
    return len([x for x in nlist if not isASM(x)])

def main():
    argv=sys.argv
    if(len(argv)<3):
        print("useage: <flilename> <address>")
        exit()
    file_name=argv[1]
    address = int(argv[2],16)
    if not path.exists(file_name):
        print("File don't exist!")
        exit()
    lines=open(file_name).readlines()
    for line in lines:
        line=line.replace("\n","")
        nline=hex(address)[2:]+":  "+line
        print(nline)
        address+=0x2*countMachineCode(line)



if __name__=="__main__":
    main()
