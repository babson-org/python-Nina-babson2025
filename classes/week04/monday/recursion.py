def myPrint(n):
    
    print("hello", n)       
    myPrint(n + 1)

print(myPrint(1))

def recur_sum(n):
    if n == 0:
        return 0
    else: n + recur_sum(n-1)
    
