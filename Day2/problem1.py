n=int(input("Enter number to be checked"))
def oddeve(n):
    if(n%2==0):
        print("Nmber is Even")
    else:
        print("Number is Odd")

def prime(n):
    temp=1
    for i in range(2,((n//2)+1)):
        if(n%i==0):
            temp=0
            break
    if(temp==1):
        print("Number is Prime")
    else:
        print("Number is not Prime")

def palindrome(n):
    dup=n;rev=0
    while(dup>0):
        d=dup%10
        rev=rev*10+d
        dup=dup//10
    if(rev==n):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")

def armstrong(n):
    dup=n;sum=0
    while(dup>0):
        d=dup%10
        sum+=(d**3)
        dup=dup//10
    if(sum==n):
        print("Number is Armstrong")
    else:
        print("Number is not Armstrong")

oddeve(n)
prime(n)
palindrome(n)
armstrong(n)