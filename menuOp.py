#!/usr/bin/env python
# coding: utf-8
	
print("Welcome Omprakash Kumawat!!!")
print("What is your chice.")

while True:
    print("1.FaceBook\n2.Linkdin")
    
    n = input()

    if n == str(1):
        import OP.OpFb
        break
    elif n==str(2):
        import OP.OpLinkdin
        break
    else:
        print("Please Enter a right choice!!!!")
 
