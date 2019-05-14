for value in range(1,6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_nums = list(range(2,11,2))
print(even_nums)

squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehension allows creating the list for squares as example into one line of code
squares = [value**2 for value in range(1,11)]
print(squares)

for value in range(1,6):
    print(value)

nums = list(range(1,1000001))
print(min(nums))
print(max(nums))
print(sum(nums))

odds = list(range(1,10,2))
print(odds)

cubes=[]
for value in range(1,10):
    cubes.append(value**3)

print(cubes)

cubes = [value**3 for value in range(1,10)]
print(cubes)