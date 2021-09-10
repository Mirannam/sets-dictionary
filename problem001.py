farm_1 = {"dog", "cat", "mouse", "sheep"}
farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
b = farm_1.intersection_update(farm_2)
a = farm_1.intersection(farm_2)
print(a)
print(b)
