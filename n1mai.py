a = input()
b = {}

for i in a:
    if i in b:b[i]+=1
    else:
        b[i]=1

print(b)

'''
for i in a:
    b = {i : a.count(i)}
    print(b)
'''