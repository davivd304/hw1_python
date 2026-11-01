import pathlib
print("pathlib可以正常使用")
from pathlib import Path

#获取当前所在文件夹：
#current_dir=Path(__file__).resolve().parent


#拼接文件（夹）路径：
#e.g. current_dir=Path("D:/py作业")
#file_path=current_dir/"data.txt"  #注意这里是/,这种写法是pathlib提供的路径拼接写法
#img_dir=current_dir/"img"
#img_file=img_dir/"A1B2.png"


#创建文件夹
#folder=Path("img")
#folder.mkdir()
#如果文件夹已存在，则写：
#folder.mkdir(exist_ok=True)
#创建多层文件夹:
#folder.mkdir(Parents=True,exist_ok=True)

#创建空文件：touch()
#file_path=Path("text.txt")
#file_path.touch()

#write_text()写入
#file_path=Path("hello.txt")
#file_path.write_text("你好，python!\n",encoding="UTF-8")

#read_text()读取
#content=file_path.read_text(encoding="UTF-8")
#print(content)
#写入多行内容,使用\n

#追加内容：
#write_test(默认覆盖原内容),想追加用open()
#with file_path.open("a",encoding="utf-8") as file:
   # file.write("新增的一行\n")

#判断路径是否存在：
#e.g.  path=Path("img")
# print(path.exsists())   #存在输出True,否则输出False

#查找文件  iterdir()会列出文件夹下的项目，包括文件夹和子文件夹
#e.g.  folder=Path("img")
#for item in folder.iterdir():
#   print(item)

#查找png文件：glob()
#语法：png_files=list(folder.glob("*.png"))

#修改文件名：rename()
#修改文件后缀：with_suffix()

#删除文件（夹）：unlink()--删文件，rmdir()--删空文件夹





#第四题：
import random
print("random可正常使用")
import string
print("string可正常使用")
current_dir=Path(__file__).resolve().parent

img_dir=current_dir/"img"
img_dir.mkdir(parents=True,exist_ok=True)

#大写字母和数字
characters=string.ascii_uppercase+string.digits

#集合保存文件名，元素不重复
file_names=set()

while len(file_names)<100:
    random_name="".join(random.choices(characters,k=4))
    file_names.add(random_name+".png")

for file_name in file_names:
    file_path=img_dir/file_name
    file_path.touch()

print("img文件夹创建成功")
print("创建文件夹的数量是：",len(file_names))





#第五题
png_files=list(img_dir.glob("*.png"))
select_files=random.sample(png_files,50)

for old_file in select_files:
    new_file=old_file.with_suffix(".jpg")
    old_file.rename(new_file)

print("已经将50个png文件改为jpg文件")













