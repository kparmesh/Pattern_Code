# Program of full pyramid 
n= int(input("Please Enter the number of rows: "))
for i in range(1,2*n):
    if i<=n:
        for spaces in range(1,n-i+1):
            print(" ",end='')
        
        for j in range(1,i+1):
            print('*',end=' ')
    else:
        for spaces in range(1,i-n+1):
            print(" ",end='')
        for j in range(n,i-n,-1):
            print("*",end=" ")
    print()