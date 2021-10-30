def solution(tickets):
    answer = []
    tick = []
    K = len(tickets)
    used = [0] * K
    for start ,end in tickets:
        tick.append([end, start])
    tick.sort()

    def dfs(now, visit, K, result):
        if len(result) != 0:
            return result
        
        if 0 not in used:
            answer = visit
            return visit
        
        for x in range(K):
            if used[x] == 0:
                if tick[x][1] == now:
                    used[x] = 1
                    result = dfs(tick[x][0], visit + [tick[x][0]], K, result)
                    used[x] = 0
        return result
                    
    answer = dfs('ICN', ['ICN'], K, [])
    
    return answer