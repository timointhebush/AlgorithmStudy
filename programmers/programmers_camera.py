def solution(routes):
    routes.sort(key=lambda x:x[1])
    Q = {i for i in range(len(routes))} #아직 카메라가 찍히지 않은 루트
    answer = 0
    while len(Q) != 0:
        camera = min(Q)
        cameraPoint = routes[camera][1]
        removeList = []
        for route in Q:
            if cameraPoint >= routes[route][0] and cameraPoint <= routes[route][1]:
                removeList.append(route)
        for item in removeList:
            Q.remove(item)
        answer += 1
    return answer


print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))