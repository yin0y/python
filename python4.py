total_a = {}
while True:
    type = input("Enter a fruit type (q to quit): ")

    if type == "q":
        break
    else:
        weight = input("Enter the weight in kg: ")
        total_a[type] = weight
print(total_a)