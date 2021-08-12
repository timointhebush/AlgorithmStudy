class Row:
    def __init__(self, name):
        self.name = name
        self.up = None
        self.down = None

class Table:
    def __init__(self):
        head = Row(None)
        head.up, head.down = head, head
        self.head = head
        self.stack = []

    def add(self, name):
        newRow = Row(name)
        lastRow = self.head.up
        self.head.up, lastRow.down = newRow, newRow
        newRow.up, newRow.down = lastRow, self.head
        
    def insertDownTo(self, row, newRow):
        downRow = row.down
        row.down, downRow.up = newRow, newRow
        newRow.up, newRow.down = row, downRow
        
    def search(self, name):
        down = self.head.down
        while down != self.head:
            if down.name == name:
                return down
            down = down.down
        return down

    def moveUp(self, row, X):
        for _ in range(X):
            row = row.up
        return row
    
    def moveDown(self, row, X):
        for _ in range(X):
            row = row.down
        return row
    
    def deleteRow(self, row):
        self.stack.append(row)
        upRow, downRow = row.up, row.down
        upRow.down, downRow.up = downRow, upRow
        if downRow == self.head:
            return upRow
        else:
            return downRow

    def restore(self):
        deletedRow = self.stack.pop()
        deletedUp, deletedDown = deletedRow.up, deletedRow.down
        deletedUp.down, deletedDown.up = deletedRow, deletedRow


    def toList(self):
        tmp = []
        down = self.head.down
        while down != self.head:
            tmp.append(down.name)
            down = down.down
        return tmp
    
    def getIdx(self, row):
        idx = 0
        down = self.head.down
        while down != self.head:
            if down.name == row.name:
                return idx
            down = down.down
            idx += 1
        return idx

    def getDiff(self, n):
        ans = ""
        down = self.head.down
        for ogN in range(n):
            if down == self.head:
                ans += "X"
            else:
                if ogN == down.name:
                    ans += "O"
                    down = down.down
                else:
                    ans += "X"
        return ans
            


def solution(n, k, cmd):
    table = Table()
    for name in range(n):
        table.add(name)
    curRow = table.search(k)
    for c in cmd:
        if c[0] == "U":
            curRow = table.moveUp(curRow, toNum(c))
        elif c[0] == "D":
            curRow = table.moveDown(curRow, toNum(c))
        elif c[0] == "C":
            curRow = table.deleteRow(curRow)
        else: # "Z"
            table.restore()
    return table.getDiff(n)

def toNum(c):
    tmp = c.split(" ")
    return int(tmp[1])

print(solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))