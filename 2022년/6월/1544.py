from collections import deque
n = int(input())
words = [input() for _ in range(n)]

for i in words:
    queue = deque(i)
    while True:
        queue.append(queue.popleft())
        word = "".join(queue)

        if word == i:
            break

        if word in words:
            words.pop(words.index(word))
        print(words)

print(len(set(words)))


