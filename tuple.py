t=("apple","orange","banana")
print(t)

y=list(t)

y[1]="new"
print(y)

t=tuple(y)
print(t)

for i in t:
    print(i)

if "pine" in t:
 print("yes")
else:
 print("sry")

 print(len(t))

t2=(1,2,3,4,5,1,2,2,3,4,3,1)
# t3=t+t2
# print(t3)

print(t2.count(2))

