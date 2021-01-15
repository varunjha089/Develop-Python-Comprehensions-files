# for loop
float_dict = {}
for i in range(10):
    float_dict[i] = i ** 100.0


# Dictionary Comprehensions
float_dict2 = {i:i**100.0 for i in range(10)}
print(float_dict2 == float_dict)