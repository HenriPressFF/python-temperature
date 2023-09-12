#! /usr/bin/python

TEMP_PATH="/sys/class/thermal/thermal_zone0/"

#fo = open(TEMP_PATH + "temp", "r")
#temp =fo.read()
#print(temp)

def readTemp():
    fo = open(TEMP_PATH+ "temp" , "r")
    temp = fo.read()
    return int(temp) *0.001

def averageTemp(n):
    allvalues = 0
    for x in range(n):
            allvalues = readTemp() + allvalues
    return allvalues/n

