#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:26:43 2022

@author: dylancai
"""

def create_patient_entry(patient_first_name, patient_last_name, patient_id, patient_age):
    new_patient = {'firstname':patient_first_name, 'lastname':patient_last_name, 
                        'pid':patient_id, 'age':patient_age, 'tests':[]}
    return new_patient

def main():
    db = []
    db.append(create_patient_entry("Ann", "Ables", 1, 30))
    db.append(create_patient_entry("Bob", "Boyles", 2, 34))
    db.append(create_patient_entry("Chris", "Chou", 3, 25))
    db_print(db)
    test_add(db,3,"HDL", 100)
    db_print(db)
    print("Patient {} is a {}".format(get_full_name(db[2]), adult_or_minor(db[2])))
    # print(db)
    # print(db[0:2])
    return db
    
def db_print(db):
    for x in db:
        print("Name: {}, ID: {}, Age: {}, Tests: {}".format(get_full_name(x),
                                                            x["pid"],
                                                            x["age"],
                                                            x['tests']))


def adult_or_minor(patient):
    if patient['age']>=18:
        return "adult"
    else:
        return "minor"
        

def get_full_name(patient):
    return("{} {}".format(patient["firstname"], patient["lastname"]))
        
def find_patient(db, id):
    for p in db:
        if p.get('pid') == id:
            return p
    return False

def test_add(db, id, test_name, test_val):
    patient = find_patient(db, id)
    patient['tests'].append((test_name, test_val))
    
if __name__ == "__main__":
    main()
