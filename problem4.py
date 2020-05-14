n=int(input("Enter no of elements of the list :-   "));st=[];nondup=[]
for i in range(n):
    ele=input()
    st.append(ele)
for x in st:
    if (x not in nondup):
        nondup.append(x)
print(nondup)
