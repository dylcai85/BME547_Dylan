#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:28:11 2022

@author: dylancai
"""

def interface():
    print("Blood Calculator")
    print("Options:")
    print("9-Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == "9":
            return
def input_HDL():
    num = input("Enter the HDL value: ")
    return int(num)
    
def check_HDL(hdl_val):
    if hdl_val >= 60:
        return "Normal"
    elif hdl_val >= 40 and hdl_val < 60:
        return "Borderline Low"
    else:
        return "Low"
    
def HDL_driver():
    hdl_val = input_HDL()
    answer = check_HDL(hdl_val)
    output_HDL_result(hdl_val, answer)

def output_HDL_result(hdl_value, charac):
    print("The results for an HDL value of {} is {}".format(hdl_value, charac))
interface()
