import copy

Dict1 = {'name': 'lee', 'age': 89, 'num': [1, 2, 8]}
Dict_copy = Dict1.copy()
Dict_dcopy = copy.deepcopy(Dict1)
Dict2 = Dict1
Dict1['num'][1] = 6
print('Dict1:' + str(Dict1) + "\n", 'Dict_copy:' + str(Dict_copy) + "\n",
      'Dict_dcopy:' + str(Dict_dcopy) + "\n", 'Dict2:' + str(Dict2))

# if statement
score = input("Please enter your score: ")
try:
    score = float(score)
    if 100 >= score >= 90:
        print("Excellent")
    elif 90 > score >= 80:
        print("good")
    elif 80 > score >= 60:
        print("medium")
    elif 60 > score >= 0:
        print("bad")
    else:
        raise ValueError
except Exception:
    print("Enter a correct score.")

# for loop: multiplication table
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d*%d=%2d" % (j, i, i * j), end="\t")
    print()

# while loop
i = 0
while i < 9:
    i += 1
    if i == 3:
        print("End the current loop.")
        continue
    if i == 5:
        print("End the current big loop.")
        break
    print(i)