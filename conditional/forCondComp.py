float_list = []
for i in range(10):
    if i % 2 == 0:
        float_list.append(i ** 100.0)
    else:
        float_list.append(-1)

float_list2 = [i ** 100.0 if i % 2 == 0 else -1 for i in range(10)]

print(float_list2 == float_list)