list =[19,3,5,9,6,29]
n=9
m=list.index(n)

for i in list:
    if i==n:

        print("Found at", m +1)
        i+=1
        break
else:
    print("Not Found")