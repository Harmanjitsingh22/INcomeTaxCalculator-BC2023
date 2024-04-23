# Comp 150
# Assignment 3
# Harmanjit Singh
# December 03, 2023

from math import sqrt
from collections import Counter

#function computes mean or average of a set of numbers
def mean(inputList) : 
    
    Total_length = len(inputList)  # get length of list
    if Total_length == 0:
        mean = 0
    else:
        mean = sum(inputList)/Total_length  # calculate means by applying formula

    return mean
    
#function computes the standard deviation of a set of numbers
def standardDeviation( inputList ) : #Step 4

    Total_length = len(inputList)  # get length of list
    if Total_length == 0:
        std_dev = 0
    else:
        mean_value = mean(inputList)
        variance = sum((x - mean_value) ** 2 for x in inputList) / Total_length
        std_dev = sqrt(variance)
    
    return std_dev

#Function normalizes the set of input in the given list

def normalize( inputList ) :

    Mean = mean(inputList)
    std_deviation = standardDeviation(inputList)
    
    normalized_income_list = []

    for income in inputList:
        if std_deviation == 0.00 :
            # Handle the case where standard deviation is zero
            normalized_income = income
        else :
            normalized_income = (income - Mean)/std_deviation 
            normalized_income = round(normalized_income,2)   # round the value

        normalized_income_list.append(normalized_income)
    
    return normalized_income_list

#function computes medians of a set of numbers
def median( inputList ) :

    inputList = sorted(inputList)
    length = len(inputList)

    if length % 2 == 0:
        # If the length is even, take the average of the two middle elements
        middle1 = inputList[length // 2 - 1]
        middle2 = inputList[length // 2]
        median_value = (middle1 + middle2) / 2
    else:
        # If the length is odd, take the middle element
        median_value = inputList[length // 2]

    return median_value

#Modes computations for a set of items in a list
def computeModes( inputList ):
    # Count occurrences of each number
    counts = Counter(inputList)

    # Find the maximum frequency
    max_frequency = max(counts.values())

    # Find numbers with the maximum frequency (modes)
    modes = [number for number, frequency in counts.items() if frequency == max_frequency]

    return modes
