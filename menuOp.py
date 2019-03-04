#!/usr/bin/env python
# coding: utf-8
	
print("Welcome Omprakash Kumawat!!!")
print("\nWhat is your chice.")

while True:
    print("\n1.FaceBook\n2.Linkdin")
    
    n = input()

    if n == str(1):
        import Facebook #Python File Name
        break
    elif n==str(2):
        import Linkdin #Python file name
        break
    else:
        print("Please Enter a right choice!!!!")
 
