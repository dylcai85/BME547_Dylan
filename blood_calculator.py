#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:28:11 2022

@author: dylancai
"""


def interface():
    print("Blood Calculator")
    print("Options:")
    print("1 - Analyze HDL")
    print("2 - Analyze LDL")
    print("3 - Analyze Cholesterol")
    print("9 - Quit")
    keep_running = True
    while keep_running:
        choice = input("Enter choice: ")
        if choice == "9":
            return
        elif choice == "1":
            HDL_driver()
        elif choice == "2":
            LDL_driver()
        elif choice == "3":
            chol_driver()


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


def input_LDL():
    num = input("Enter the LDL value: ")
    return int(num)


def check_LDL(ldl_val):
    if ldl_val >= 190:
        return "very high"
    elif 160 <= ldl_val < 190:
        return "high"
    elif 130 <= ldl_val < 160:
        return "borderline high"
    else:
        return "normal"


def LDL_driver():
    ldl_val = input_LDL()
    answer = check_LDL(ldl_val)
    output_LDL_result(ldl_val, answer)


def output_LDL_result(ldl_value, charac):
    print("The results for an LDL value of {} is {}".format(ldl_value, charac))


def input_chol():
    num = input("Enter the Cholesterol value: ")
    return int(num)


def check_chol(chol_val):
    if chol_val < 200:
        return "Normal"
    elif 200 <= chol_val < 240:
        return "Borderline High"
    else:
        return "High"


def chol_driver():
    chol_val = input_chol()
    answer = check_chol(chol_val)
    output_chol_result(chol_val, answer)


def output_chol_result(chol_val, charac):
    print("The results for a cholesterol value of {} is {}"
          .format(chol_val, charac))


if __name__ == "__main__":
    interface()
