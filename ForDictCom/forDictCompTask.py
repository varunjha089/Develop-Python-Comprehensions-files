def old_saturation_level(data_dict):
    temp = {}
    for key, value in data_dict.items():
        temp[key] = (value ** 3) / (2 ** value)
    return temp


def saturation_level(data_dict):
    return {k: v ** 3 / 2 ** v for k, v in data_dict.items()}


if __name__ == "__main__":
    hydration_level = {"arc1":5, "arc2":6, "arc3":3}
    print(old_saturation_level(hydration_level) == saturation_level(hydration_level))
