for x in range(1,100000):
    y=x
    cubesum=0
    while x!= 0:
        a=x%10
        cubesum +=a*a*a
        x=int(x/10)
    if y==cubesum:
        print("Armstrong",y)
    """else:
         print("Not Armstrong")"""
