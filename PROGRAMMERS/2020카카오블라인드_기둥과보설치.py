def solution(n, build_frame):
    coord_plane = [ [ {"pillar":False, "ceiling":False} for _ in range(n+2) ] for _ in range(n+2) ]
    answer = []
    for build in build_frame:
        x, y = build[0], build[1]
        ceiling, install = build[2], build[3]
        if install == 1:
            if ceiling == 1:
                if checkCeilingInstall(x, y, coord_plane):
                    coord_plane[x][y]['ceiling'] = True
            else:
                if checkPillarInstall(x, y, coord_plane):
                    coord_plane[x][y]['pillar'] = True
        else:
            if ceiling == 1:
                if checkDel(x, y, coord_plane, "ceiling"):
                    coord_plane[x][y]['ceiling'] = False
            else:
                if checkDel(x, y, coord_plane, "pillar"):
                    coord_plane[x][y]['pillar'] = False
    for x in range(n+1):
        for y in range(n+1):
            if coord_plane[x][y]['pillar'] == True:
                answer.append( [x, y, 0] )
            if coord_plane[x][y]['ceiling'] == True:
                answer.append( [x, y, 1] )
    return answer

def checkPillarInstall(x, y, coord_plane):
    if y == 0:
        return True
    if coord_plane[x-1][y]["ceiling"] == True or coord_plane[x][y]["ceiling"] == True:
        return True
    if coord_plane[x][y-1]["pillar"] == True:
        return True
    return False

def checkCeilingInstall(x, y, coord_plane):
    if coord_plane[x][y-1]['pillar'] == True or coord_plane[x+1][y-1]['pillar'] == True:
        return True
    if coord_plane[x-1][y]['ceiling'] == True and coord_plane[x+1][y]['ceiling'] == True:
        return True
    return False

def checkDel(x, y, coord_plane, delType):
    if delType == "ceiling":
        coord_list = [ (x-1, y, "ceiling"), (x, y, "pillar"), (x, y-1, "pillar"), 
        (x+1, y, "pillar"), (x+1, y, "ceiling"), (x+1, y-1, "pillar") ]
    else:
        coord_list = [ (x-1, y+1, "ceiling"), (x, y+1, "ceiling"), (x, y+1, 'pillar') ]
    original = coord_plane[x][y][delType]
    coord_plane[x][y][delType] = False
    result = True
    for cx, cy, category in coord_list:
        if coord_plane[cx][cy][category]:
            if category == "ceiling":
                if checkCeilingInstall(cx, cy, coord_plane) == False:
                    result = False
                    break
            else: # pillar
                if checkPillarInstall(cx, cy, coord_plane) == False:
                    result = False
                    break
    coord_plane[x][y][delType] = original
    return result


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))