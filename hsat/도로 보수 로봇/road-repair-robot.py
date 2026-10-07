# Please write your code here.

def is_possible(l, x, n, k): # 길이 l 짜리 패치로 가능한지 검사 
    cnt, last_x = 1, x[0] # 첫번쨰 구멍 == x[0], last_x = 현재 패치가 시작한 위치
    for i in range(1,n):
        if x[i] - last_x + 1 <= l : # 그다음 구멍 - 현재 패치 + 1 이 패치 length 보다 작거나 같으면 커버 가능 --> continue
            continue
        
        cnt +=1 # 아니면 패치 하나더 
        last_x = x[i] # 여기서부터 새로운 패치로 시작
    
    return cnt <= k # k 개 이하로 가능하면 return 

def parametric_search(s,e,x,n,k): # 가능한 최소 l 을 이분탐색으로 찾기
    # s = 가능한 패치 길이의 최소 후보
    # e = 최대 후보
    if s > e: # 더 볼 숫자가 없을때
        return float('inf') # 걍 젤 큰 숫자 돌려드릴테니 이전  m 쓰시길
    m = (s+e) // 2 # 가운데 값부터 시작

    if is_possible(m, x, n, k):
        return min(m, parametric_search(s, m-1, x, n, k))
    
    else:
        return parametric_search(m+1, e, x, n, k)
    
def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))

    x.sort()

    print(parametric_search(1, x[-1]- x[0] + 1, x, n, k))

if __name__ == "__main__":
    main()