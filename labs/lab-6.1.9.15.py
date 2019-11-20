inp = "Several carachters to be counted and put in a dictionary as a histogram"
inp = inp.replace(" ", "").lower()
dic = {k:0 for k in sorted(set(inp))}

for c in inp:
    dic[c]+=1

[print(h + ' -> ' + str(v)) for h, v in dic.items()]