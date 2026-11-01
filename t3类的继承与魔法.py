class Person:
    def __init__(self,name,age,gender):
        self.name=name 
        self.age=age 
        self.gender=gender

    def personinfo(self):
        print(self.name)
        print(self.age)
        print(self.gender)

class Student(Person):
    def __init__(self,name,age,gender,college,class_):
        super().__init__(name,age,gender)
        self.college=college
        self.class_=class_
    def personinfo(self):
        super().personinfo()
        print(self.college)
        print(self.class_)

    def __str__(self):
        return(
            f"姓名：{self.name}\n"
            f"年龄：{self.age}\n"
            f"性别：{self.gender}\n"
            f"学院：{self.college}\n"
            f"班级：{self.class_}"
        )

person = Person("张三", 20, "男")

print("Person 的信息：")
person.personinfo()

print("\nStudent 的信息：")

student = Student(
    "李四",
    19,
    "男",
    "aiar学院",
    "aiar2601班"
)

student.personinfo()

print("\n使用 __str__ 方法输出：")

print(student)


