def lcs(str1, str2):
    m = len(str1)
    n = len(str2)

    # DP 테이블 초기화
    # dp[i][j]는 i
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # DP 테이블 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:  # 문자가 일치하면
                dp[i][j] = dp[i - 1][j - 1] + 1  # LCS 길이 증가
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # 최대 LCS 길이 선택

    # 최장 공통 부분 수열의 길이 반환
    return dp[m][n]

# 사용 예시
str1 = input("첫 번째 문자열을 입력하세요: ")
str2 = input("두 번째 문자열을 입력하세요: ")
result = lcs(str1, str2)
print(f"최장 공통 부분 수열의 길이는: {result}")
