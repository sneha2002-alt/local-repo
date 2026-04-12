# practice question
countries = ["France", "China", "Canada", "Germany", "Chile"]

for c in countries:
  if c.startswith("C"):
    countries.remove(c)
    
print(countries)    