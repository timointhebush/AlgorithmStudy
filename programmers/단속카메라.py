def solution(routes):
    # routes 정렬
    routes = sorted(routes, key=lambda x: x[1])
    answer = 0
    left_routes = []
    while True:
        last_camera = routes[0][1]
        answer += 1
        for route in routes:
            if last_camera > route[1] or last_camera < route[0]:
                left_routes.append(route)
        if len(left_routes) == 0:
            break
        routes = left_routes
        left_routes = []
    return answer


if __name__ == "__main__":
    print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
