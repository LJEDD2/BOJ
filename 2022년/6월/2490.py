dict = {4:"E",3:"A",2:"B",1:"C",0:"D"}
for i in range(3):
    sumv = sum([*map(int,input().split())])
    print(dict[sumv])
