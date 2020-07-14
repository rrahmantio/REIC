# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:56:05 2020

@author: riyan
"""
#real estate investment calculator

import numpy as np
import matplotlib.pyplot as plt

#input value

principal_amount=int(input('house price'))

refurbishment=int(input('cost of refurbishment'))

no_of_years=int(input('number of years to calculate investment'))

interest_rate=float(input('% property interest rate'))

rental_value=int(input('property rental value'))

rental_rate_increase=float(input('% rental rate increase'))

cost_value=int(input('annual cost of tax and maintenance'))

cost_increase=float(input('% increase in cost of tax and maintenance'))

compound_principal=list()
compound_rental=list()
compound_cost=list()
compound_cashflow=list()

zero = principal_amount + refurbishment
print('Year 0 Investment =', zero)

#Start loop for specified period of investment

i = 1
amount=0
rental=0
cost=0
cashflow=0
for i in range(i, no_of_years+1):
    amount+=principal_amount+principal_amount*(interest_rate/100)
    principal_amount=amount
    print('property value at year', i, ' = \n',  (principal_amount))
    compound_principal.append(amount)
    amount=0
    rental+=rental_value+rental_value*(rental_rate_increase/100)
    rental_value=rental
    print('rental value at year', i , ' = \n', (rental_value))
    compound_rental.append(rental)
    rental=0
    cost+=cost_value+cost_value*(cost_increase/100)
    cost_value=cost
    print('annual cost of tax and maintenance at year', i, ' = \n', (cost_value))
    compound_cost.append(cost)
    cost=0
    cashflow+=(rental_value+rental_value*(rental_rate_increase/100))-(cost_value+cost_value*(cost_increase/100))
    print('cash flow at year', i, ' = \n', (rental_value-cost_value))
    compound_cashflow.append(cashflow)
    cashflow=0
    
    #end loop
    
#Plot graph

years=np.arange(1,no_of_years+1)
plt.plot(years,compound_principal, marker = 'o')
plt. title('House Price')
plt.xticks(years)
plt.xlabel('Years')
plt.ylabel('Amount')
plt.show()

plt.plot(years,compound_rental, marker = 'o', color='green')
plt. title('Rent Price')
plt.xticks(years)
plt.xlabel('Years')
plt.ylabel('Rent Income')
plt.show()

plt.plot(years,compound_cost, marker= 'o', color='red')
plt.title('Tax and Maintenance Cost')
plt.xticks(years)
plt.xlabel('Years')
plt.ylabel('Cost')
plt.show()

plt.plot(years,compound_cashflow, marker= 'o', color='orange')
plt.title('Cash Flow')
plt.xticks(years)
plt.xlabel('Years')
plt.ylabel('Amount')
plt.show()

flow = np.sum(compound_cashflow)
print('Total expected cash flow during investment period =', flow)
gain = [ compound_principal[-1] - zero ]
print('Capital gain from property value increase =', gain)
profit=((gain+flow)/zero)*100
print('Total Gain in Percentage =', profit , '%' )
print('Annualized Gain =', profit/no_of_years, '%' )



