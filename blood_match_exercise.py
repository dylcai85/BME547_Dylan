#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:58:29 2022

@author: dylancai
"""
import requests

# r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/dc306")
# print(r.status_code)
# print(r.text)

# r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/M7")
# print(r.status_code)
# print(r.text)

# r = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/F6")
# print(r.status_code)
# print(r.text)

out_data = {"Name": "dc306", "Match": "No"}
r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check",
                  json=out_data)
print(r.status_code)
print(r.text)