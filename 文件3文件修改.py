with open("test.txt","r",encoding="ascii") as f:
    content=f.read()

new_content="python"+content+"python"
with open("t3文件修改","w",encoding="ascii") as new_f:
    new_f.write(new_content)     