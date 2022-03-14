from collections import deque
t =int(input())
    # 선입선출이기 때문에
    # 맨 앞으로 오는 문서 우선도가 젤 높으면 출력 (제거)하고 cnt +=1
    # m번째 문서를 찾을 때까지 반복
    # 우선도가 max값이 아니면 뒤로 다시 보낸다.
    # max값부터 없애줌

def print_Q():
    cnt = 1
    while True:
        # 맨 왼쪽의 값이 max값이 아니면
        # 맨 앞에꺼 맨 뒤로 보내주기(2번 재배치조건)
        if queue[0] != max(queue):
            queue.append(queue.popleft())
            idx.append(idx.pop(0))

        # 배치가 다 됐을 때
        else:
            # Target 인덱스값 찾기
            if idx[0] == 1:
                break
            # idx와 queue pop하면서
            else:
                queue.popleft()
                idx.pop(0)
                cnt += 1
                # 위치 저장 (1부터 카운트)
    print(cnt)

for _ in range(t):
    n, m = map(int,input().split())
    queue = deque(list(map(int,input().split())))
    # 중요도가 동일한 숫자가 있어서 인덱스로 구분
    idx = [0]*n
    # m번째 숫자는 target 표시
    idx[m] = 1
    print_Q()
