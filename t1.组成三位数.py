
count=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
                if( k!=j and k!=i and j!=i):
                    num=100*i+10*j+k
                    print(num,end=' ')
                    count+=1
print()
print(count)
            


