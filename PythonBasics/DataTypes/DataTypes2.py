values = [1, 2, "kanchana", 4, 5]

# List is a data type that allow multiple values and can be different data types
print(values[0]) #1
print(values[2]) #Kanchana
print(values[4]) #5
print(values[-1]) #5
print(values[1:3]) #1, Kanchana
values.insert(3,"Shetty")
print(values)
values.append("End")
print(values)

values[2] = "Kanchana"
print(values)

del values[0]
print(values)