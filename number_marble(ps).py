N, M = map(int, input().split()) # 구슬의 개수, 그룹의 수

marbles = list(map(int, input().split()))

MAX_SUM = sum(marbles) # 모든 구슬에 쓰여진 숫자의 합

if M == N: # 가능한 경우는 1가지뿐
    print(max(marbles))
    for i in range(M):
        print(1, end=' ')
    exit()

# 답이 될 수 있는 값 중 최솟값은 숫자 중 가장 큰 값 -> M=N인 경우, 각 숫자 중 가장 큰 값이 답이 된다.
# 5 4 2 6 9 3 8 7
# 예를 들어 M = 6, (5,4), (2,6), (9), (3), (8), (7) 이므로 최댓값은 9가 된다.
# cnt_marbles = [0 for _ in range(300)] # M보다 작거나 같은 경우 그룹의 길이 저장
# mid를 키값으로 딕셔너리에 cnt_marbles를 저장
group_count_dict = {}
sum_count_dict = {}
# mid보다 작거나 같도록 하나의 그룹을 만들 때, M개의 그룹이 나오는지 판별 -> 총 몇 개의 그룹인지 반환
# 그룹의 개수를 세면서 각 그룹의 길이와 합까지 모두 저장하기
def isPossible(mid):
    cnt_marbles = [0 for _ in range(300)]
    sum_marbles = [0 for _ in range(300)]
    # print("mid=", mid)
    sum = 0  # 한 그룹의 숫자의 합
    group_cnt = 0 # 형성된 그룹의 개수
    i = 0 # 한 그룹의 구슬의 수
    for num in marbles:
        sum += num
        i += 1
        if sum > mid: # num을 더했을 때 그룹의 합이 기준보다 커지면
            group_cnt += 1  # 그룹의 개수 카운트
            sum_marbles[group_cnt - 1] = sum - num
            sum = num # num부터 새로운 그룹으로 넘기고
            cnt_marbles[group_cnt - 1] =  i - 1  # 해당 그룹의 구슬의 수 저장
            i = 1
            # print("그룹의 개수", group_cnt, "다음 그룹의 sum", num)
    if sum > 0:
        group_cnt += 1
        cnt_marbles[group_cnt - 1] = i
        sum_marbles[group_cnt - 1] = sum
    group_count_dict[mid] = cnt_marbles
    sum_count_dict[mid] = sum_marbles
    # print("그룹의 개수", group_cnt, "그룹별 구슬의 개수", cnt_marbles[:group_cnt-1])
    return group_cnt


# parametric search
left = max(marbles)
right = MAX_SUM
ans = float('inf')
# 이분탐색 시작
while left <= right:
    # print("left:", left, "right:", right)
    mid = (left + right) // 2
    # print("mid", mid)
    if isPossible(mid) > M :  # 그룹의 개수가 M보다 많은 경우 -> mid를 키운다(그룹의 수를 줄여야 하니까)
        # print("그룹의 개수가 더 많은 경우")
        left = mid + 1
    else: # 그룹의 개수가 작거나 같은 경우 -> mid를 줄인다(그룹의 수를 늘려야 하니까)
        # print("그룹의 개수가 작거나 같은 경우")
        right = mid - 1 # 더 작은 값으로 시도
        if mid < ans:
            ans = mid # 최솟값 갱신

# 그룹의 개수가 M보다 작은 경우 쪼개기
while group_count_dict[ans][:M][-1] == 0: # 그룹의 개수가 M보다 작다면
    tof = False # 최댓값이 등장하였는지 그 여부
    for i in range(300):
        # print(tof)
        if sum_count_dict[ans][i] == ans and tof == False: # i가 최댓값인 경우, 쪼개면 안 됨, pass(유일한 최댓값이 아니면?)
            tof = True
            continue
        # 최댓값이 아닌 경우 구슬의 개수가 2개 이상이라면 해당 그룹을 쪼개기
        if group_count_dict[ans][i] > 1:
            group_count_dict[ans][i] -= 1 # 원래 그룹의 길이에서 1을 뺀 값으로 갱신
            group_count_dict[ans].insert(i + 1, 1) # 길이 1짜리 그룹을 추가
            sum_count_dict[ans].insert(i + 1, 0) # 구슬의 합도 한 칸씩 밀기
            # print(group_count_dict[ans][:M])
            # print(sum_count_dict[ans][:M])
        if group_count_dict[ans][:M][-1] != 0: ## M-1번째 그룹의 구슬 수가 0이 아니면 반복문 중단
            break

# print("반복문 탈출")

# total = 0  # 구슬에 적힌 숫자의 합
#
# cnt = 0  # 하나의 그룹에 속한 구슬의 개수
# remain = M
# 그룹별 구슬의 개수 구하기
# for i in range(len(marbles)):
#     total += marbles[i]
#     print("total:", total, "cnt:", cnt)
#     if total > ans:
#         cnt_marbles.append(cnt)
#         print("이 그룹의 구슬 개수", cnt)
#         remain -= 1  # 만들어야하는 그룹의 수 1감소
#         total = marbles[i]
#         cnt = 0 # 그룹에 속한 구슬 개수 초기화
#     cnt += 1
#     if remain == (N - i): # 만들어야하는 그룹 수와 남은 구슬의 수가 같다면
#         cnt_marbles.append(cnt) # 현재까지 만든 그룹의 구슬 개수를 추가하고
#         cnt_marbles + [1 for _ in range(remain)] # 나머지 구슬은 1개씩 그룹으로 만들기
#         break
# if total > 0:
#     cnt_marbles.append(cnt)


print(ans)
print(*group_count_dict[ans][:M])

