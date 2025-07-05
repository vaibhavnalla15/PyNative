""" Calculate income tax for the given income by adhering to the rules below """
# Taxable Income	    Rate (in %)
# First Rs. 10,000	            0
# Next Rs. 10,000	            10
# The remaining	            20

# Expected Output:
# For example, suppose the income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = Rs. 6000

income = 45000
tax_payable = 0
print("Given income Rs.", income)

# If income is Rs. 10,000 or less → no tax
if income <= 10000: # no tax on first 10,000
    tax_payable = 0

# If income is between Rs. 10,001 and Rs. 20,000:
# First Rs. 10,000 → no tax
# Remaining → taxed at 10%

elif income <= 20000:
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100

# If income is more than Rs. 20,000:
# First Rs. 10,000 → 0% tax
# Next Rs. 10,000 → 10% tax = Rs. 1,000
# Remaining (Rs. income - Rs. 20,000) → 20% tax

else:
    # first 10,000 = 0% tax
    tax_payable = 0

    # next 10,000 = 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining (above 20,000) = 20% tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is Rs.", tax_payable)