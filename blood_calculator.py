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
def HDL():
    num = input("Enter the HDL value: ")
    return int(num)
    
interface()
HDL()