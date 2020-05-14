cost=int(input("Enter costing price"))
sell=int(input("Enter selling price"))

profit=sell-cost
prof_per=(profit/cost)*100

prof_per_inc=((5*prof_per)/100)+prof_per
new_sp=cost+(prof_per_inc/100)*cost

print(new_sp)
