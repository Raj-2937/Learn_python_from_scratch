#f-string in python variable ko convinently format kar ne ka tarika.

Letter= "I am from {} and my name is{} "
country = "India"
name = "Aman"

print(Letter.format(country,name))


#f string 
print(f"I am fromv{country} and my name is {name}")


price =90.9240894

txt = f"For only {price:.2f} dollars!"
print(txt)

#print(txt.format())
print(type(f"{2 *30}"))
