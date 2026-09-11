#sets method in python.
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

#example:

cities = {"Tokey" , "japan"}
cities2 = {"Tokey" , "south america","austrila","Madrid"}

cities3 = cities.difference(cities2)
print(cities3)

print(cities.issuperset(cities3))
print(cities.symmetric_difference_update(cities3))
print(cities2.remove("japan"))
print(cities2.discard("Tokey"))
