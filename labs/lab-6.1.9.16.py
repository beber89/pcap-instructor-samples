# In this version Output is sorted according to frequencies unlike last example
inp = "Several carachters to be counted and put in a dictionary as a histogram"
inp = inp.replace(" ", "").lower()
dic = {k:0 for k in sorted(set(inp))}

for c in inp:
    dic[c]+=1

## explain this on a list of tuples
## then show how to build dictionary from list of tuples
dic = dict(sorted(dic.items(), key=lambda x: x[1], reverse=True))
###

[print(h + ' -> ' + str(v)) for h, v in dic.items()]