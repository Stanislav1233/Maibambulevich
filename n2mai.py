import ast
n = ast.literal_eval(input())

def f(n):
    if isinstance(n,list) == 1:
        h = [f(x) for x in n if x]
        return h
    elif isinstance(n,dict) == 1:
        ns = {}
        for j in a:
            l = n[j]
            if j and l:
                ns[j] = f(l)
        return ns
    elif isinstance(n,set) == 1:
        z = {f(x) for x in n if x}
        return z

    return n

print(f(n))

'''
первые попытки решения

def f(n):
    if isinstance(n, str) == True:
        if len(str(n)) == 0:
            return 0
        else:
            return 1
    else:
        if len(n) == 0:
            return 0
        else:
            return 1

for i in range(len(l1)):
    if isinstance(l1[i], dict) == True:
        if len(l1[i]) != 0:
            n = l1[i]
            n = {k: v for k,v in n.items() if k != " " and k != ""}
            ln.append(n)
    else:
        if isinstance(l1[i], list) == True:
            m = l1[i]
            if len(m) != 0:
                lk = []
                for i in range(len(m)):
                    if f(m[i]) != 0:
                        lk.append(m[i])
                ln.append(lk)
        if isinstance(l1[i], str) == True:
            if len(l1[i]) != 0 and l1[i] != " ":
                ln.append(l1[i])
print(ln)
'''