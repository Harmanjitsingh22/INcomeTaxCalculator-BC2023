# Comp 150 
# Assignment 3
# Harmanjit Singh
# December 03, 2023

from taxUtilities import *
from nstatistics import *
from skeleton import generateJSON, extractEmployeeInfo, extractGrossIncomes

#Testing the computeProvTaxes(...) operation
def q1() :
	
    test = []
    
    #testing the first bracket
    income = 29590
    taxes = computeProvTaxes( income )
    result = round(  abs( taxes - 1657.04 ) )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    #testing the first bracket
    income = 42000
    taxes = computeProvTaxes( income )
    result = round( abs( taxes - 2352.0 ), 2 )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    income = 92468.79
    taxes = computeProvTaxes( income )
    result = round( abs( taxes - 6193.81 ) )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    income = 120000.79
    taxes = computeProvTaxes( income )
    result = round( abs( taxes - 9356.13 ) )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    income = 200000.79
    taxes = computeProvTaxes( income )
    result = round( abs( taxes - 21515.62 ) )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    income = 1000000.28
    taxes = computeProvTaxes( income )
    result = round( abs( taxes - 184009.05 ) )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    return test
    
#Testing the computeFedTaxes(...) operation
def q2() :
	
    test = []
    
    #testing the first bracket
    income = 29590
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 4438.50 ) )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    income = 52000.98
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 7800.15 ) )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    income = 135000.01
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 26295.82 ) )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    income = 92468.79
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 16021.35 ) )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    income = 182456.99
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 39145.44 ) )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    income = 1000000
    taxes = computeFedTaxes( income )
    result = round(  abs( taxes - 306805.91 ) )
    test.append( result <= 0.01 )
    #print(taxes)
    #print(result <= 0.01)
    
    return test
    
#Testing the computeCPP(...) operation
def q3() :
	
    test = []
    
    #testing the first bracket
    income = 35000
    cpp = computeCPP( income )
    result = round(  abs( cpp - 2082.50 ) )
    test.append( result <= 0.01 )
    
    income = 92000
    cpp = computeCPP( income )
    result = round(  abs( cpp - 3754.45 ) )
    test.append( result <= 0.01 )
    
    return test    

#Testing the computeEI(...) operation
def q4() :
	
    test = []
    
    #testing the first bracket
    income = 35000
    ei = computeEI( income )
    result = round(  abs(ei - 570.50 ) )
    test.append( result <= 0.01 )
    
    income = 92000
    ei = computeEI( income )
    result = round(  abs( ei - 1002.45 ) )
    test.append( result <= 0.01 )
    
    return test 
    
#Testing the computeHealthPremium(...) operation
def q5() :
	
    test = []
    
    #testing the first bracket
    income = 10000
    hp = computeHealthPremium( income )
    result = round(  abs(hp - 0.0 ) )
    answer = result <= 0.01
    test.append( answer )
    #print( hp )
    #print(answer)
    
    income = 23000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 60 ) )
    test.append( result <= 0.01 )
    answer = result <= 0.01
    test.append( answer )
    #print( hp )
    #print(answer)
    
    income = 35000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 300 ) )
    answer = result <= 0.01
    test.append( answer )
    #print( hp )
    #print(answer)
    
    income = 38000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 300 ) )
    answer = result <= 0.01
    test.append( answer )
    #print( hp )
    #print(answer)
    
    income = 48500
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 450 ) )
    answer = result <= 0.01
    test.append( answer )
    #print( hp )
    #print(answer)
    
    income = 70000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 600 ) )
    answer = result <= 0.01
    test.append( answer )
    #print( hp )
    #print(answer)
    
    income = 72500
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 600 ) )
    answer = result <= 0.01
    test.append( answer )
    #print(answer)
    
    income = 200000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 750 ) )
    answer = result <= 0.01
    test.append( answer )
    #print(answer)
    
    income = 200500
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 750 ) )
    answer = result <= 0.01
    test.append( answer )
    #print(answer)
    
    income = 300000
    hp = computeHealthPremium( income )
    result = round(  abs( hp - 900 ) )
    answer = result <= 0.01
    test.append( answer )
    #print(answer)
    
    return test 

#Testing the computeNetIncomes(...) and mean(...) operations
def q6():

    test = []
    
    incomes = []
    x = mean( incomes )
    result = (x == 0)
    test.append( result )
    
    
    incomes = [1000000, 150000, 25000, 92468.79]
    nIncomes = computeNetIncomes( incomes )
    x = mean( nIncomes )
    #print(nIncomes)
    
    result = round( abs( x - 171689.28 ) ) <= 0.01
    test.append( result )
    #print( x )
    #print(result)

    return test

#Testing the standardDeviation(...) and mean(...) operations
def q7():

    test = []
    
    incomes = []
    sdev = standardDeviation( incomes )
    result = (sdev == 0)
    test.append( result )
    
    incomes = [1000000, 150000, 25000, 92468.79]
    sdev = standardDeviation( incomes )
    result = round( abs( sdev - 396880.40 ) <= 0.01 )
    test.append( result )
    
    return test
    
#Testing the normalize(...) and mean(...) operations
def q8():

    test = []
    
    incomes = [1000000, 150000, 25000, 92468.79]
    nIncomes = computeNetIncomes( incomes )
    normalized = normalize( nIncomes )
    x = sum( normalized )
    result = round( abs( x + 0.01 ) <= 0.01 )
    test.append( result )
    #print(x)
    #print(result)
    
    incomes = [92468.79]
    nIncomes = computeNetIncomes( incomes )
    normalized = normalize( nIncomes )
    x = sum( normalized )
    result = round( abs( x - 64746.73 ) <= 0.01 )
    test.append( result )
    #print(x)
    #print(result)
    
    return test

#Testing the modes of net incomes of all employees
def q9():

    test = []
    
    fileName = 'E:\Smester 1\Comp 150\Assignments/Harmanjit_singh_A3/Harmanjit_singh_A3/data/salaries'
    grossIncomeList = extractGrossIncomes( fileName, 'json' )
    netIncomeList = computeNetIncomes( grossIncomeList )
    averageNetIncomes = mean( netIncomeList )
    lst = computeModes( netIncomeList )
    #lst = sorted( lst )
    #print(lst)
    
    avgModes = float( format( mean( computeModes( netIncomeList ) ), '.2f' ) )
    result = round( abs( avgModes - 81462.06 ) ) <= 0.01
    test.append( result )
    #print(avgModes)
    #print(result)
    
    return test    

#Testing the variance method
def q10():

    test = []
    
    fileName = 'E:\Smester 1\Comp 150\Assignments/Harmanjit_singh_A3/Harmanjit_singh_A3/data/salaries'
    grossIncomeList = extractGrossIncomes ( fileName, 'json' )
    netIncomeList = computeNetIncomes( grossIncomeList )
    #print(netIncomeList)
    averageNetIncomes = mean( netIncomeList )
    x = float(format(standardDeviation( netIncomeList ), '.2f'))
    variance = float( format( x ** 2, '.2f' ) )
    
    result = round( abs( variance - 1461038245.66 ) ) <= 800
    test.append( result )
    #print(variance)
    #print(result)
    
    return test 
    
#Testing the median method
def q11():

    test = []
    
    fileName = 'E:\Smester 1\Comp 150\Assignments/Harmanjit_singh_A3/Harmanjit_singh_A3/data/salaries'
    grossIncomeList = extractGrossIncomes ( fileName, 'json' )
    netIncomeList = computeNetIncomes( grossIncomeList )
    averageNetIncomes = mean( netIncomeList )
    med = float( format( median( netIncomeList ), '.2f' ) )
    
    result = round( abs( med - 82439.49 ) ) <= 0.01
    test.append( result )
    #print(med)
    #print(result)
    
    
    return test 
    
#BONUS POINTS - Testing the generalized function for provinces of BC and Alberta
def q12():

    test = []
    
    #Alberta Province
    taxRangeList = [131220, 157464, 209952, 314928, None]
    taxRates = [0.1, 0.12, 0.13, 0.14, 0.15]
    
    #Testing with a beginning tail value
    tax = computeTax( 120486.79, taxRangeList, taxRates )
    result = round( abs( tax - 12048.68 ) ) <= 0.01
    test.append( result )
    
    #Testing intermediate range
    tax = computeTax( 140486.79, taxRangeList, taxRates )
    result = round( abs( tax - 14234.01 ) ) <= 0.01
    test.append( result )
    
    tax = computeTax( 230486.79, taxRangeList, taxRates )
    result = round( abs( tax - 25969.59 ) ) <= 0.01
    test.append( result )
    
    #Testing with an end tail value
    tax = computeTax( 530486.79, taxRangeList, taxRates )
    result = round( abs( tax - 70125.17 ) ) <= 0.01
    test.append( result )
    
    
    
    #British Columbia Province
    taxRangeList = [43070, 86141, 98901, 120094, 162832, 227091, None]
    taxRates = [0.0506, 0.077, 0.105, 0.1229, 0.147, 0.168, 0.205]
    
    #Testing with a beginning tail value
    tax = computeTax( 30486.79, taxRangeList, taxRates )
    result = round( abs( tax - 1542.63 ) ) <= 0.01
    test.append( result )
    
    #Testing intermediate range
    tax = computeTax( 80486.79, taxRangeList, taxRates )
    result = round( abs( tax - 5060.43 ) ) <= 0.01
    test.append( result )
    
    tax = computeTax( 220486.79, taxRangeList, taxRates )
    result = round( abs( tax - 25408.71 ) ) <= 0.01
    test.append( result )
    
    #Testing with an end tail value
    tax = computeTax( 530486.79, taxRangeList, taxRates )
    result = round( abs( tax - 88714.36 ) ) <= 0.01
    test.append( result )
    
    return test

#A helper operation
def evaluateQuestion( questions ) :

    answer = questions[0]
    for question in questions : 
        answer = ( answer and question )
    
    return answer