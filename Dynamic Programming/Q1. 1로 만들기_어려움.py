n = int(input())

# 계산된 결과를 저장하기 위한 테이블
d = [0] * 30001

 # 2는 1을 1번 빼면 1이 됨. d[2] = 1
 # 3은 1을 2번 빼면 1이 됨. d[3] = 2

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    
    if i%2 == 0:
        # 1을 빼서 계산한 것과 (2로 나눈 것의 계산 횟수 + 2로 한번 나눈 횟수) 중 작은 것 저장. 
        d[i] = min(d[i],d[i//2]+1)
    if i%3==0:
        d[i] = min(d[i],d[i//3]+1)
    if i%5==0:
        d[i] = min(d[i],d[i//5]+1)

print(d[n])