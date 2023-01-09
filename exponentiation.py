#------------------------------------------------------------------------
# You are offered a choice of either $1000000 or $0.01 (one penny)
# double every day for 30 days (the result amount is doubled every day.)
#------------------------------------------------------------------------


#-------------------------------------------------------------------------
# Write a program to calculate then amount that will result from doubling
# to understand which choice result in a larger amount.
#-------------------------------------------------------------------------



def double_penny(days):
    penny = 0.01
    for i in range(days):
        penny *= 2 
    return penny
print(double_penny(30))