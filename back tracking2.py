N = int(input())
seq = list(map(int, input().split()))
operator = list(map(int, input().split()))
minAns = float('Inf')  # 양의 무한대를 나타내는 부동소수점 값
maxAns = float('-Inf')

def back_tracking(index, sum):
    global minAns  # 최솟값 정답을 저장하기 위한 변수를 전역변수로 생성
    global maxAns
    # 백트래킹 함수의 핵심(종료 조건)
    if index == N-1: # 수의 마지막 인덱스에 접근했을 때, 함수를 종료
        if minAns > sum:
            minAns = sum
        if maxAns < sum:
            maxAns = sum
        return

    for i in range(4):  # 연산자의 인덱스가 총 4가지
        temp = sum  # 임시변수에 sum의 값을 할당(나중에 중간에 호출된 재귀함수가 종료되고 나서 다시 초기값을 사용하기 위함)
        if operator[i] == 0: # 해당 연산자가 남아있지 않다면 다음 연산자에 대한 반복으로
            continue
        if i == 0:  # 연산자가 남아있는 경우이면서 해당 연산자가 덧셈인 경우
            sum += seq[index+1]
        elif i == 1:  # 마찬가지로 뺄셈인 경우
            sum -= seq[index+1]
        elif i == 2:  # 마찬가지로 곱셈인 경우
            sum *= seq[index+1]
        else:  # 마찬가지로 나눗셈인 경우
            if sum < 0:  # 음수를 나누는 경우
                sum = (abs(sum)//seq[index+1])*(-1)
            else:  # 양수를 나누는 경우
                sum //= seq[index+1]

        operator[i] -= 1  # 한 번의 연산이 끝나면 사용된 연산자는 삭제
        back_tracking(index+1, sum)  # 연산자 하나를 사용하고 나면 함수 재귀 호출, 이때 다음 피연산의 인덱스와 지금까지의 연산 결과를 인자로 전달
        operator[i] += 1  # 재귀함수가 종료되어 스택에서 제거되고 나면 다시 최상단의 함수의 동작이 재개되는데 바로 이전의 연산이 수행되지 않은 상태로 다시 돌아간다.
        sum = temp  # 임시변수에 저장해놓은 바로 이전의 연산이 이루어지기 전의 결과값을 다시 사용

back_tracking(0, seq[0])
print(maxAns)
print(minAns)