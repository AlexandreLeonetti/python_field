prices = [310,315,275,295,260,270,290,230,255,250]

# this function calculates the maximum delta between low and subsequent local high

# for each price take new low as low.
# for each new low take next local high only if it beats the previews delta.

def max_profit(P):
    lowSoFar = P[0]
    localHigh= P[0]
    maxProfit = 0
    for  p in P:
        if p < lowSoFar :
            localHigh = p
        lowSoFar = min(lowSoFar, p)
        localHigh= max(localHigh,p)
        maxProfit= max(maxProfit,(localHigh-lowSoFar))
    return maxProfit

print(max_profit(prices))

    
