s = "ababa"

T = '#'.join('^{}$'.format(s))
n = len(T)
P = [0] * n
C = R = 0

for i in range(1, n - 1):
    # i'는 i의 미러 위치
    i_mirror = 2 * C - i

    if R > i:
        P[i] = min(R - i, P[i_mirror])
    else:
        P[i] = 0

    # 중심을 i로 하는 팰린드롬 확장
    while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
        P[i] += 1

    # 만약 팰린드롬이 오른쪽 경계를 넘어서면 중심과 오른쪽 경계 갱신
    if i + P[i] > R:
        C, R = i, i + P[i]

# 최대 팰린드롬 길이와 중심 찾기
max_len, center = max((n, i) for i, n in enumerate(P))
start = (center - max_len) // 2
print(s[start: start + max_len])

