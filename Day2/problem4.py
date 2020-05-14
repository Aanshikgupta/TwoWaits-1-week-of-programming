n=5
for i in range(n):
    print("*"*(n-1-i),end="")
    print("  "*i,end="")
    if(i<=5):
        print("*"*(n-1-i))
for j in range(n):
    print("*"*j,end="")
    print("  "*(n-1-j),end="")
    print("*"*j)
