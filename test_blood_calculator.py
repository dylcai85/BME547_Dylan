#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 12:10:41 2022

@author: dylancai
"""
import pytest
@pytest.mark.parametrize("HDL_val, expected", [(85, "Normal"), 
                                               (40, "Borderline Low"), 
                                               (20, "Low")
                                               ])


def test_check_HDL_Normal(HDL_val, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_val)
    assert answer == expected


"""    
def test_check_HDL_BorderlineLow():
    from blood_calculator import check_HDL
    answer= check_HDL(40)
    expected = "Borderline Low"
    assert answer == expected
    
def test_check_HDL_Low():
    from blood_calculator import check_HDL
    answer= check_HDL(20)
    expected = "Low"
    assert answer == expected
"""