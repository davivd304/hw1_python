with open("D:/py learn/data.txt","w",encoding="UTF-8") as f:
    for line in range(100000):
        import random
        number=random.randint(1,100)
        f.write(str(number)+'\n')
    
