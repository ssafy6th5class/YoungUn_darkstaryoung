# [BOJ]_1969_DNA

### 문제

DNA란 어떤 유전물질을 구성하는 분자이다. 이 DNA는 서로 다른 4가지의 뉴클레오티드로 이루어져 있다(Adenine, Thymine, Guanine, Cytosine). 우리는 어떤 DNA의 물질을 표현할 때, 이 DNA를 이루는 뉴클레오티드의 첫글자를 따서 표현한다. 만약에 Thymine-Adenine-Adenine-Cytosine-Thymine-Guanine-Cytosine-Cytosine-Guanine-Adenine-Thymine로 이루어진 DNA가 있다고 하면, “TAACTGCCGAT”로 표현할 수 있다. 그리고 Hamming Distance란 길이가 같은 두 DNA가 있을 때, 각 위치의 뉴클오티드 문자가 다른 것의 개수이다. 만약에 “AGCAT"와 ”GGAAT"는 첫 번째 글자와 세 번째 글자가 다르므로 Hamming Distance는 2이다.

우리가 할 일은 다음과 같다. N개의 길이 M인 DNA s1, s2, ..., sn가 주어져 있을 때 Hamming Distance의 합이 가장 작은 DNA s를 구하는 것이다. 즉, s와 s1의 Hamming Distance + s와 s2의 Hamming Distance + s와 s3의 Hamming Distance ... 의 합이 최소가 된다는 의미이다.

### 입력

첫 줄에 DNA의 수 N과 문자열의 길이 M이 주어진다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 DNA가 주어진다. N은 1,000보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다.

### 출력

첫째 줄에 Hamming Distance의 합이 가장 작은 DNA 를 출력하고, 둘째 줄에는 그 Hamming Distance의 합을 출력하시오. 그러한 DNA가 여러 개 있을 때에는 사전순으로 가장 앞서는 것을 출력한다.

### 풀이

```python
import sys
#조금이라도 빠른 연산을 위한 딕셔너리화
DNA = { "A" : 0, "C" : 1, "G" : 2, "T" : 3}
#인덱스 접근을 이용하기 위한 리스트
DNA_T = ["A", "C", "G", "T"]

#입력받기
N, M =map(int, sys.stdin.readline().rstrip().split())
DNA_MAP = [sys.stdin.readline().rstrip() for _ in range(N)]
#결과용 리스트만들기
DNA_RESULT = [0] * M

#갯수만큼
for x in range(M):
    #제일 많은것 확인용
    DNA_CNT = [0] * 4
    #세로줄 돌면서 확인하자
    for y in range(N):
        #A,C,G,T 중에 어느것인가요?
        DNA_CNT[DNA[DNA_MAP[y][x]]] += 1
    #제일 많은 건 무엇인가요?
    maxx = max(DNA_CNT)
    for j in range(4):
        #제일 많은 것들로만 만들어 봅시다.
        if DNA_CNT[j] == maxx:
            DNA_RESULT[x] = DNA_T[j]
            break

result = 0
#가로줄 확인
for x in range(M):
    #해당 인덱스에 있는 문자는?
    ST = DNA_RESULT[x]
    for y in range(N):
        #이번 인덱스의 대표 문자가 아니면 갯수 추가해주자
        if ST != DNA_MAP[y][x]:
            result +=1
#출력!
print("".join(DNA_RESULT))
print(result)
```

