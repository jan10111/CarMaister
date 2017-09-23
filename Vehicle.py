#!/usr/bin/env python
# -*- coding: utf-8 -*-

class vehicle(object):
    brand = ""
    model = ""
    km_driven = ""
    servis = ""

    def __init__(self, brand, model, km_driven, servis):
        self.brand = brand
        self.model = model
        self.km_driven = km_driven
        self.servis = servis

    def get_full_name(self):
        return self.brand + " " + self.model


    def print_full_list(vehicle_list):
        for i in range(len(vehicle_list)):
            print "Znamka in model: " + self.brand + " " + self.model
            print "Št. prevoženih km: " + self.km_driven
            print "Zadnji servis: " + self.servis
            print ""

