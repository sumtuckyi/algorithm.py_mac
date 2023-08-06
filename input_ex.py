'''
3
123
456
789
'''

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]  # 한 줄에 입력되는 데이터 사이에 공백이 없으므로 split()사용할 필요가 없음