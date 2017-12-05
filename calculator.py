#!/usr/bin/env python

"""A calculator program, as well as my first attempt
at working with python in years."""

__author__	= "Reed Posehn"
__copyright__	= "Written in 2017"

import sys
import math

def add(num1, num2):
    res = float(num1) + float(num2)
    return res

def sub(num1, num2):
    res = float(num1) - float(num2)
    return res

def mul(num1, num2):
    res = float(num1) * float(num2)
    return res

def div(num1, num2):
    res = float(num1) / float(num2)
    return res

def main():
    while True:
	op =  raw_input("Which operation would you like to do? ")
        if op == 'add':
            num1 = raw_input("Num one: ")
            num2 = raw_input("Num two: ")
            res = add(num1, num2)
            print res
            break
	if op == 'sub':
            num1 = raw_input("Num one: ")
            num2 = raw_input("Num two: ")
            res = sub(num1, num2)
            print res
            break
	if op == 'mul':
            num1 = raw_input("Num one: ")
            num2 = raw_input("Num two: ")
            res = mul(num1, num2)
            print res
            break
	if op == 'div':
            num1 = raw_input("Num one: ")
            num2 = raw_input("Num two: ")
            res = div(num1, num2)
            print res
            break

if __name__ == '__main__':
    main()
