#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:26:43 2022

@author: dylancai
"""

def create_patient_entry(patient_name, patient_id, patient_age):
    new_patient = [patient_name, patient_id, patient_age,[]]
    return new_patient

def main():
    db = []
    db.append(create_patient_entry("Ann Ables", 1, 30))
    db.append(create_patient_entry("Bob Boyles", 2, 34))
    db.append(create_patient_entry("Chris Chou", 3, 25))
    test_add(db,3,"HDL", 100)
    # print(db)
    # print(db[0:2])
    return db
    
def db_print(db):
    for x in db:
        print("Name: {}, ID: {}, Age: {}".format(x[0], x[1], x[2]))
        
def find_patient(db, id):
    for p in db:
        if p[1] == id:
            return p
    return False

def test_add(db, id, test_name, test_val):
    patient = find_patient(db, id)
    patient[3].append((test_name, test_val))
    
if __name__ == "__main__":
    db_print(main())
    print(find_patient(main(), 3))
