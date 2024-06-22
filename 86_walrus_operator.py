a = True
# print(a = False)  # will give error
print(a := False) # will print false {simple use of (:) walrus operator}

print()

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())


# without walrus
foods = list()
while True:
    food = input("What food do you like?: ")
    if food == "quit":
        break
    foods.append(food)


# with walrus
cars = list()
while (car := input("Name a car you like: ")) != "quit":
    cars.append(car)



