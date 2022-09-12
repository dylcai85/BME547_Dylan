#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 12:03:04 2022

@author: dylancai
"""

weight = round(20 / 2.205, 1)
dosage = round(weight * 30, 1)


print("CORRECT DOSAGE")
print("For a patient weighing {} kg,".format(weight))
print("  the correct dosage is {} mg the first day".format(dosage))
