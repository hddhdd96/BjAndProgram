n = int(input())
li = []
for i in range(n):
    temp = int(input())
    if temp != 0:
        li.append(temp)
    else:
        li.pop()
print(sum(li))
    