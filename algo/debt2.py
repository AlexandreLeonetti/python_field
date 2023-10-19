# here we are going to simulate
# the ratio and liquidation price as a function of pending orders
# 2023-10-19


def simu (equity, debt, entryPrice):
    qty = equity/entryPrice 
    ratio = (equity+debt)/debt
    liquidationPrice = 1

    #1.1 = qty*price/debt 
    price= debt*1.1/qty

    return ratio,price 


#print(simu(5000, 1000, 70))


def liquidation(debt, qty):
    return   debt*1.2/qty
    
#print(liquidation(534, 80.8))

"""
in the litecoin scenario
both the quantity AND the debt moves
at the same time
"""
pending = [ (0.01, 60),
            #(2.66, 52.55),
            #(1.44, 48.55), 
            (3.46,43.38),
            (3.5,36.66),
            (6.6,33.33),
            (4.29,32.66)]
            #(1.42,49.55),
            #(1.44,48.55),
            #(1.47, 47.55)]

def pendingLiquidation(A, initDebt, initQty):

    #calculate array of sum of qty and debt first
    qtySum  = []
    debtSum = []
    for i, x in enumerate(A):
        arr = ([x[0] for x in A])
        arrDebt = [x[1]*x[0] for x in A]
        debtSum.append(sum(arrDebt[:i+1]))
        qtySum.append( sum(arr[:i+1]))
    #print(qtySum)
    #print(debtSum)

    res = []
    for i, x in enumerate(A):
        #print(initDebt + debtSum[i], initQty + qtySum[i])
        res.append( liquidation(initDebt + debtSum[i], initQty + qtySum[i] ))# add qty and debt for each new order 
    return res

# (array of pending orders, total debt in USD, total position in LTC
l = pendingLiquidation(pending,740,85.2)

#for i in l print(i)
[print("{:.2f}".format(i)) for i in l]


