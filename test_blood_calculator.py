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
def test_check_HDL(HDL_val, expected):
    from blood_calculator import check_HDL
    answer = check_HDL(HDL_val)
    assert answer == expected


@pytest.mark.parametrize("LDL_val, expected", [(195, "very high"),
                                               (160, "high"),
                                               (130, "borderline high"),
                                               (129, "normal")
                                               ])
def test_check_LDL(LDL_val, expected):
    from blood_calculator import check_LDL
    answer = check_LDL(LDL_val)
    assert answer == expected
