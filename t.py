def even_elements(any_list):
    n = 0
    sub_list = [0]
    result = []
    for _ in range(len(any_list) + 1):
        if any_list[0] % 2 == 1:
            any_list.pop(0)
            any_list.extend(sub_list)
        elif any_list[0] % 2 == 0:
            if any_list[0] == 0:
                break
            result.append(any_list[0])
            any_list.pop(0)
            any_list.extend(sub_list)
    return result


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)