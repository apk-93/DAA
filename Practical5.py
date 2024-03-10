def knapsack(c,wt,val,n):
    if n == 0 or c == 0:
        return 0
    if wt[n-1]>c:
        return knapsack(c,wt,val,n-1)
    else:
        return max(val[n-1] + knapsack(c - wt[n-1],wt ,val, n-1),
                   knapsack(c,wt,val,n-1))
if __name__== '__main__':
    value=[10, 20, 50, 60]
    weight=[2, 3, 4, 5]
    c=8
    n=len(value)
    print(knapsack(c,weight,value,n))




