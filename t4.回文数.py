num=int(input("please enter a number:"))
if num<=0:
    print("请输入一个正整数")
else:
    digits=str(num)
    reverse_digits= digits[::-1]
    if digits==reverse_digits:
        print("回文数")
    else:
        print("不为回文数")

        

