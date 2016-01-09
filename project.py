#!/usr/bin/python
# python project.py

from sys import argv
from os.path import exists

script, bmi_file = argv

def bmicalc(height, weight):
	bmi = weight / (height * height) * 703.0
	return bmi

def writebmi(age, height, height_cm, weight, weight_kg, bmi):
	bmistore = open(bmifile, 'w')
	bmistore.write("%s \t %s \t %s \t %s \t %s \t %s") % (age, height, height_cm, weight, weight_kg, bmi)
	
print "What is your age in years?"
age = int(raw_input())

print "What is your height in inches?"
height = float(raw_input())
height_cm = height * 2.54

print "What is your weight in pounds?"
weight = float(raw_input())
weight_kg = weight / 2.2

print "Your age in years is %s." % age
print "Your height in inches is %s." % height
print "Your height in centimeters is %s." % height_cm
print "Your weight in pounds is %s." % weight
print "Your mass in kilograms is %s." % weight_kg

print "Your bmi is %s." % bmicalc(height,weight)
print "You're fantastic."

writebmi(age, height, height_cm, weight, weight_kg, bmi)
print "Data Stored"