with open("test.txt","r",encoding="ascii") as f:
    with open("t3文件修改","r",encoding="ascii") as new_f:
        count=0
        for line in f:
            count+=1
            new_line=new_f.readline()
            if line!=new_line:
                print(f"第{count}行内容不相同")

