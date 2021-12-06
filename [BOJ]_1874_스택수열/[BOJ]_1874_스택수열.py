import sys

N = int(sys.stdin.readline())
stack = []
result = []
now_num = 1
check_point = 1
for x in range(N):
    input_num = int(sys.stdin.readline())
    while input_num >= now_num:
        stack.append(now_num)
        now_num += 1
        result.append('+')
    
    if stack[-1] == input_num:
        stack.pop()
        result.append('-')
    else:
        check_point = 0
        break
if check_point == 0:
    print('NO')
else:
    for x in range(len(result)):
        print(result[x])