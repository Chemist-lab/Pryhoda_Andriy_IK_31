import datetime
import sys
import logging
import numpy
import random

def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform
    
def filter_numbers(filter):
    numbers=range(0,101)
    if filter=="True":
    	msg = "Парні елементи: " 
    elif filter=="False":
    	msg = "Непарні елементи: "
    
    for index in range(0, len(numbers)):
    	if (filter == "True") & (numbers[index]%2 == 0):
    	    msg += str(numbers[index]) + " "
    	elif (filter == "False") & (numbers[index]%2 != 0):
    	    msg += str(numbers[index]) + " "
    return msg

def show_array():
    x=[random.randint(0, 15) for i in range(10)]      
    print("Масив X[]:", x)
    index = int(input("Введіть номер елемента масиву який хочете вивести: "))
    try:
    	print(f"X[{index}] = {x[index]}")
    except IndexError:
        logging.error("Ви ввели число за межами проміжку 0-3")
    else:
    	logging.info("Ви ввели коректні дані")
    	
    
