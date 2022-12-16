def summation(n,term):
    total,k=0,1
    while k<=n:
        total,k=total+term(k),k+1
    return total
def cube(x):
    return x**3
def cubesum(n):
    return summation(n,cube)
print(cubesum(3))
