a = raw_input('enter something my dog').split()

b = {}

for x in range(len(a)):
    if a[x] not in b:
        b[a[x]] = a.count(a[x])
for key in b:
    print key, b[key]
