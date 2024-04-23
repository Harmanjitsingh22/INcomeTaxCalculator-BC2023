# Comp 150 
# Assignment 3
# Harmanjit Singh
# December 03, 2023

#BONUS! BONUS!! BONUS!!! - Earns you 30 additional points (only if you can develop the solution and its flowchart)
#A generalized function that can compute tax for employee irrespective of their province
#and even can compute federal tax (to reduce the complexity you may introduce a helper function)        
#Example input (for British Columbia) 
# taxRangeList = [45654, 91310, 104835, 127299, 172602, 240716, None]
# taxRates = [0.056, 0.077, 0.105, 0.1229, 0.147, 0.168, 0.205]
#   If grossIncome = 120486.79 then computeTax(...) will return 9971.25

def computeTax( grossIncome, taxRangeList, taxRates ) :
    
    annual_prov_tax = 0.0
    i = 0  # Initialize index to 0

    while i < len(taxRangeList):
        if taxRangeList[i] is None:
            annual_prov_tax += taxRates[i] * (grossIncome - taxRangeList[i - 1])
            break
        elif i == 0 or grossIncome <= taxRangeList[i]:
            annual_prov_tax += taxRates[i] * grossIncome
            break
        else:
            annual_prov_tax += taxRates[i] * (taxRangeList[i] - taxRangeList[i - 1])
            grossIncome = grossIncome - (taxRangeList[i] - taxRangeList[i - 1])

        i += 1  # Move to the next tax bracket

    return round(annual_prov_tax, 2)

#operation computes provincial taxes for the input gross income... you can base your solution of computeTax(...)
def computeProvTaxes(annual_taxable_income):
    if annual_taxable_income <= 45654.00:
        annual_provincial_tax = 0.056*annual_taxable_income
    elif annual_taxable_income > 45654.00 and annual_taxable_income <= 91310.00:
        annual_provincial_tax = 2556.624+(0.0770*(annual_taxable_income-45654.00))
    elif annual_taxable_income > 91310.00 and annual_taxable_income <= 104835.00:
        annual_provincial_tax = 6072.136+(0.1050*(annual_taxable_income-91310.00))
    elif annual_taxable_income > 104835.00 and annual_taxable_income <= 127299.00:
        annual_provincial_tax = 7492.261+(0.1229*(annual_taxable_income-104835.00))
    elif annual_taxable_income > 127299.00 and annual_taxable_income <= 172602.00:
        annual_provincial_tax = 10253.0866+(0.1470*(annual_taxable_income-127299.00))
    elif annual_taxable_income > 172602.00 and annual_taxable_income <= 240716.00:
        annual_provincial_tax = 16912.6276+(0.1680*(annual_taxable_income-172602.00))
    else:
        annual_provincial_tax = 28355.7796+(0.2050*(annual_taxable_income-240716.00))

    return annual_provincial_tax


#operation computes federal taxes for the input gross income... you can base your solution of computeTax(...)
def computeFedTaxes(annual_taxable_income):
    
    if annual_taxable_income <= 53359.00:
        annual_federal_tax = 0.1500*annual_taxable_income
    elif annual_taxable_income > 53359.00 and annual_taxable_income <= 106717.00:
        annual_federal_tax = 8003.85+(0.2050*(annual_taxable_income-53359.00))
    elif annual_taxable_income > 106717.00 and annual_taxable_income <= 165430.00:
        annual_federal_tax = 18942.24+(0.26*(annual_taxable_income-106717.00))
    elif annual_taxable_income > 165430.00 and annual_taxable_income <= 235675.00:
        annual_federal_tax = 34207.62+(0.29*(annual_taxable_income-165430.00))
    else:
        annual_federal_tax = 54578.67+(0.33*(annual_taxable_income-235675.00))

    return annual_federal_tax
 

### Beginning of Step 3 - Computing employee's CPP
def computeCPP( grossIncome ) :
    
    CPP = 0.0595*grossIncome
    CPP = min(3754.45, CPP)
    return CPP

### Beginning of Step 4 - Computing employee's EI
def computeEI( grossIncome ) :
    
    EI = 0.0163*grossIncome
    EI = min(1002.45, EI)
    EI = round(EI,2)
    return EI

def computeHealthPremium( grossIncome ) :
    
    if grossIncome <= 22000.00:
        health_premium = 0
    elif grossIncome > 22000.00 and grossIncome <= 38000.00:
        health_premium = 0.06 * (grossIncome - 22000.00)
        health_premium = min(300.00, health_premium)
    elif grossIncome > 38000.00 and grossIncome <= 50000.00:
        health_premium = 300.00 + (0.06 * (grossIncome - 38000.00))
        health_premium = min(450.00, health_premium)
    elif grossIncome > 50000.00 and grossIncome <= 74000.00:
        health_premium = 450.00 + (0.25 * (grossIncome - 50000.00))
        health_premium = min(600.00, health_premium)
    elif grossIncome > 74000.00 and grossIncome <= 202000.00:
        health_premium = 600.00 + (0.25 * (grossIncome - 74000.00))
        health_premium = min(750.00, health_premium)
    else:
        health_premium = 750.00 + (0.25 * (grossIncome - 202000.00))
        health_premium = min(900.00, health_premium)

    return health_premium

#Function computes total deductions list by invoking 
def computeDeductions( grossIncomeList ) : #Step 2

    totalDeductionsList = [] #creating and initializing the total deductions list

    annual_prov_tax = computeProvTaxes(grossIncomeList)
    annual_fed_tax = computeFedTaxes(grossIncomeList)
    health_premium = computeHealthPremium(grossIncomeList)
    cpp = computeCPP(grossIncomeList)
    ei = computeEI(grossIncomeList)

    total_tax_deductions = annual_prov_tax + annual_fed_tax + health_premium + cpp + ei
        
    # create a list of total deductions
    totalDeductionsList.append(total_tax_deductions)

    return totalDeductionsList


#Function computes net incomes by invoking 
def computeNetIncomes( grossIncomeList) : #Step 2
    netIncomeList = []  # creating and initializing the net income list
    for grossIncome in grossIncomeList:
        deductions = computeDeductions(grossIncome)
        for deduction in deductions:
            netIncome = grossIncome - deduction
            netIncomeList.append(netIncome)

    return netIncomeList