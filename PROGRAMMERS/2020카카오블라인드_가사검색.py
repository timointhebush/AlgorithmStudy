def solution(words, queries):
    answer = []
    hist = {}
    for query in queries:
        num = 0
        tmp = []
        hist_queries = createHistQueries(query)
        for hist_query in hist_queries:
            if hist_query in hist:
                search_list = hist[hist_query]
                break
            else:
                search_list = words
            
        for word in search_list:
            if check(query, word):
                num += 1
                tmp.append(word)
        answer.append(num)
        hist[query] = tmp
    return answer

def check(query, word):
    q, w = len(query), len(word)
    if q != w :
        return False
    idx = 0
    while idx <= q-1:
        if query[idx] != word[idx] and query[idx] != "?":
            return False
        idx += 1
    return True

def createHistQueries(query):
    hist_queries = []
    n = len(query)
    q_find_idx = query.index("?")
    idx = 0
    if query[0] != "?": # 앞쪽이 알파벳으로 시작
        for find_idx in range(q_find_idx, 0, -1):
            hist_query = ""
            for i, v in enumerate(query):
                if i == find_idx-1:
                    hist_query += "?"
                else:
                    hist_query += v
            hist_queries.append(hist_query)
    else: # 뒷쪾이 알파벳으로 시작
        while True:
            hist_query = ""
            met = False
            for i, v in enumerate(query):
                if v != "?" and met == False:
                    hist_query += "?"
                    met = True
                else:
                    hist_query += v
            hist_queries.append(hist_query)
            if hist_query[-1] == "?":
                break
            query = hist_query
    return hist_queries
                
print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
    