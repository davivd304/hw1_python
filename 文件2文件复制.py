import random
asc=""
for j in range(32,127):
    asc+=chr(j)
print(asc)
lines=int(input("请输入行数"))
chars=int(input("请输入每行字符串数"))
    
with open("test.txt","w",encoding="ascii") as f:
    for i in range(lines):
        line=""

        for j in range(chars):
            one_char=random.choice(asc)
            line+=one_char

        f.write(line+'\n')



with open("test.txt","r",encoding="ascii") as f:
    with open("copy_test.txt","w",encoding="ascii") as targetf:
        for line in f:
            targetf.write(line)

print("text.txt生成成功！")
print("text.txt生成成功！")




