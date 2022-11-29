#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:18:36 2022

@author: dylancai
"""


def increment_by_five(x):
    a = x + 5
    if x<0:
        return "This function cannot accept answers less than zero"
    return a


answer = increment_by_five(-11)
print("The answer is {}".format(answer))
