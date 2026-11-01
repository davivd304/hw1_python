list=list(range(1,234,1))
while len(list)>1:
    for idx in range(len(list)-1,-1,-1):
        if idx%3==0:
            del list[idx]
print(list)

