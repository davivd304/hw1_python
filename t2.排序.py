x=int(input())
y=int(input())
z=int(input())
if x>=y:
   temp=x
   x=y
   y=temp
if x>=z:
   temp=x
   x=z
   z=temp
if y>=z:
   temp=y
   y=z
   z=temp
print(f"{x} {y} {z}")
    
   