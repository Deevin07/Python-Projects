# -*- coding: utf-8 -*-
"""
Calculating Income Tax

@author: Vineet
"""


"""
Here I am considering Indian Rupee (Rs) as the currency and taken conditions are:

If amount <= Rs. 2,50,000 then zero tax.
If amount <= Rs. 5,00,000 then 5% of total income exceeding Rs. 2,50,000
If amount <= Rs. 7,50,000 then Rs. 12500 + 10% of total income exceeding Rs. 5,00,000
If amount <= Rs. 10,00,000 then Rs. 37500 + 15% of total income exceeding Rs. 7,50,000
If amount <= Rs. 12,50,000 then Rs. 75000 + 20% of total income exceeding Rs. 10,00,000
If amount <= Rs. 15,00,000 then Rs. 125000 + 25% of total income exceeding Rs. 12,50,000
If amount > Rs. 15,00,000 then Rs. 187500 + 30% of total income exceeding Rs. 15,00,000
"""
while True:
    try:
        
        income = int(input("Plese enter your taxable income in India: "))
    except ValueError:
        print(" Sorry we didn't Understand that plase enter a taxable amount")
        continue

    else:
        break
    
"""
If income is less than or equals to Rs. 2,50,000 then tax will be zero.
If income is less than or equals to Rs. 5,00,000 then tax will be 5% of total income exceeding Rs. 2,50,000
If income is less than or equals to Rs. 7,50,000 then tax will be 10% of total income exceeding Rs. 5,00,000 with an additional cost of Rs. 12,500.
If income is less than or equals to Rs. 10,00,000 then tax will be 15% of total income exceeding Rs. 7,50,000 with an additional cost of Rs. 37,500.
If income is less than or equals to Rs. 12,50,000 then tax will be 20% of total income exceeding Rs. 10,00,000 with an additional cost of Rs. 75,000.
If income is less than or equals to Rs. 15,00,000 then tax will be 25% of total income exceeding Rs. 12,50,000 with an additional cost of Rs. 1,25,000.
If income is more than Rs. 15,00,000 then tax will be 30% of total income exceeding Rs. 15,00,000 with an additional cost of Rs. 1,87,500.
"""      

if income <= 250000:       # 2lakh 50 thousand
    tax = 0

elif income <= 500000:     # 5 lakh
    tax = (income - 250000) * 0.05

elif income <= 750000:     # 7 lakh 50 thousand
    tax = (income - 500000) * 0.10 + 12500
    
elif income <= 1000000:    #10 lakh
    tax = (income - 750000) * 0.15 + 375000
    
elif income <= 1250000:    #12 lakh 50 thousand 
    tax = (income - 1000000) * 0.20 + 750000

elif income <= 1500000:     #15 lakh
    tax = (income - 1500000) * 0.25 + 125000
    
else:
    tax = (income - 1500000) * 0.30 + 187500
    
    
print ('You owe',tax,'Rupees in Tax')