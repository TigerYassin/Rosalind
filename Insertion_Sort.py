String = [6, 10, 4, 5, 1, 2]
t = 0
for x in String:
    if(t + 1 <= len(String) -1):
        if String[t] > String[t + 1]:
            String[t] = String[t + 1]
        t +=1

print String