'''
range(begin, end, step);
range(10) -> 0;1;2;3;4;5;6;7;8;9
range(1,10) -> 1;2;3;4;5;6;7;8;9
range(1,10,2) -> 1;3;5;7;9
range(10,0,-1) -> 10;9;8;7;6;5;4;3;2;1
range(10,0,-2) -> 10;8;6;4;2
range(2,11,2) -> 2;4;6;8;10
'''


n = int(input("Moi nhap so: "))
s=0
if n%2 == 0:
    for x in range(2,n+1,2):
        print(x)
        s+=x
elif n%2!=0:
    for x in range(1,n+2,2):
        print(x)
        s+=x
print("Tong s = ",s)


for y in "banana":
  print(y)

fruits = ["apple", "banana", "cherry"]
for z in fruits:
  print(z)