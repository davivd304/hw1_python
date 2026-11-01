import random
from statistics import mean,median
with open("t1.文件输入","w",encoding="utf-8") as f:
    for i in range(1,11):
        r=list()
        for j in range(1,4):
            number=random.randint(1,100)
            r.append(str(number))
        f.write(",".join(r)+'\n')


second_column=list()
with open("t1.文件输入","r",encoding="utf-8") as f:
    for line in f:
        values=line.strip().split(",")
        second_column.append(int(values[1]))


print("第二列数据：",second_column)
print()
print("max:",max(second_column))
print()
print("min:",min(second_column))
print()
print("median:",median(second_column))
print()
print("mean:",mean(second_column))






  

        


