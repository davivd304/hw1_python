#列表一边遍历一遍删除，如果能成立，最终numbers列表剩下500个元素，但它访问的下标是999，亦即最后一个奇数，但这显然超出number下标最大值
#修改方案
number=list(range(1000))
for idx in range(len(number)-1,-1,-1):    #range(起点，终点，步长)，倒着遍历访问
    if number[idx]%2==1:
        number.pop(idx)
print(number)