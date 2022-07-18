while True:
    try:
        print(input())
    except EOFError: # 예외처리 들어올때까지 try
        break