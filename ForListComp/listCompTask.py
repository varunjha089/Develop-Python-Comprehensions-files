def process_incoming_data(data_list):
    temp = []
    for datum in data_list:
        temp.append(datum // 2 * 67 - 5)
    return temp


# sol
def new_process_incoming_data(data_list):
    return [(datum // 2 * 67 - 5) for datum in data_list]


if __name__ == "__main__":
    dlist = [5, 10, 15, 20]
    print(process_incoming_data(dlist) == new_process_incoming_data(dlist))
