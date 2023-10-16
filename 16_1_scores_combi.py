# this is program is able to calculate to allscore combinations
# using matrix calculations


scores = [2,3,7]

def possible (scr, target):
    matrix = [[1]+[0]*target for s in scr]
    for i,s in enumerate(scr):
                
            if i == 0 :
                 for j in range(1,target+1):
                     if j>=s:
                        matrix[i][j]=matrix[i][j-s]

            if i>0:           
                for j in range(1, target+1):
                    if j>=s :
                        matrix[i][j] = matrix[i-1][j] + matrix[i][j-s] 
                    else:
                        matrix[i][j] = matrix[i-1][j]

    return matrix


x =possible(scores,10)
for c in x:
    print(c)




