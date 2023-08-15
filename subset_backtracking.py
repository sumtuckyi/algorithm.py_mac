def subset(index, total, arr):
    global cnt
    if total > 10:
        return
    if index == len(my_set)-1:
        if total == 10:
            cnt += 1
            cases.append(arr.copy())
        return
    total += my_set[index]
    arr.append(my_set[index])
    subset(index + 1, total, arr)
    total -= my_set[index]
    arr.pop()
    subset(index+1, total, arr)

my_set = [i for i in range(1, 10+1)]
cnt = 0
cases = []
subset(0, 0, [])
print(cnt, *cases, sep='\n')