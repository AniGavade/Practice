x = []
a = int(input("Enter the size: "))
for i in range(a):
    y = int(input("Enter the value: "))
    x.append(y)
print(x)

for j in range(1, a):
    x[j]=x[j]*(j+1)

print(x)