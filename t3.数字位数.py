num=int(input("Please enter a number"))
if num <0:
    print ("请输入正整数.")
else:
    digits=str(num)
    print(f"这个数位数为{len(digits)}")

    #[::-1]表示把字符串从后往前排列
    for digit in digits[::-1]:
        print(digit,end='')
