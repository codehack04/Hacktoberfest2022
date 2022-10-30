for i in range(10):
    for j in range(10):
        if((i==j) or (j==9-i)):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
