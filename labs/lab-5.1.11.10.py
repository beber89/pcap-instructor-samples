def includes(word, comb):
  for c in word:
    if c not in comb:
      return False
  return True

print(includes("donor", "Nabucodonosor"))
print(includes("donut", "Nabucodonosor"))
