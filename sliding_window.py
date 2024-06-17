s = "krpgjbjjznpzdfy"
t = "nxargkbydxmsgby"
maxCost = 14
max_len = 0
sum = abs(ord(s[0]) - ord(t[0]))  # 처음 한 칸
start = 0  # 윈도우 시작점
print(f"len:{len(s)}")

# 디버깅용
cost = [0 for _ in range(len(s))]
for i in range(len(s)):
    cost[i] = abs(ord(s[i]) - ord(t[i]))
print(cost)


if sum <= maxCost:
    max_len = 1

for i in range(1, len(s)):  # 윈도우 종료 인덱스 i
    print(f"현재 윈도우 합 : {sum}, {i}번째 비용을 더하기 전")
    if sum > maxCost:  # 윈도우 이동하기 - 길이는 그대로
        print(f"윈도우 이동하기 - 길이는 {max_len}")
        sum -= abs(ord(s[start]) - ord(t[start]))
        start += 1
        sum += abs(ord(s[i]) - ord(t[i]))
    else:  # 현재 윈도우 범위 내에서 조건을 충족하는 경우
        print(f"조건 충족 : from{start} to {i - 1}")
        max_len = max(i - start, max_len)
        sum += abs(ord(s[i]) - ord(t[i]))

if sum <= maxCost:
    max_len = max(max_len, i - start + 1)

print(max_len)



