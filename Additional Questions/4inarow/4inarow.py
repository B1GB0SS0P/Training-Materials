def make_grid(rows, columns):
    return [[None for _ in range(rows)] for _ in range(columns)]

   







# # The below functions can be used for subsequent parts
def rows(grid):
    return len(grid)


def cols(grid):
    return len(grid[0])


def get_value(grid, row, col):
    row_length = rows(grid)
    col_length = cols(grid)
    if row_length < row or col_length < col or row < 0 or col < 0:
        return None
    else:
        return grid[row][col]


def set_value(m, rol, col, val):
    m[rol][col] = val
    return m


# Question 4b
class ColumnFullError(Exception):
    pass


def drop(grid, col, token):
    i = 0
    while i <= len(grid[col]):
        if i == len(grid[col]):
            raise ColumnFullError(col)
        if grid[i][col] == None:
            grid[i][col] = token
            break
        i += 1
        
    


# Question 4c
# Implement the following function such that check_rows can work
def check_row(row):
    temp = row[0]
    count = 1
    for i in range(1, len(row)):
        if row[i] != temp:
            temp = row[i]
            count = 1
        else:
            count += 1
        if count == 4:
            return True
    if count == 4:
        return True
    else:
        return False
    


# The following function should not be changed
def check_rows(grid):
    for row in grid:
        token = check_row(row) # check individual row
        if token:
            return token
    return False


# Question 4d
def diagonal(grid):
    col = len(grid)
    row = len(grid[0])
    lst = make_grid(row, col*2)
    start = grid[0][0]
    for i in range(col*2):
        for j in range(row):
            lst[i][j] = (start[0]+j, start[1]+j)
        start = (start[0]-1, start[1])
    return lst





# Question 4e
def deep_map(fn, l):
    if isinstance(item,list):
        return [deep_map(item) for item in l]
    else:
        return fn(l)

# Question 4f
# Insert variables into the check_winner function
def check_winner(grid, to_win=4):
    print(grid)
    def new_check(row, win):
        temp = row[0]
        count = 1
        for i in range(1, len(row)):
            if row[i] != temp:
                temp = row[i]
                count = 1
            else:
                count += 1
            if count == win:
                return True
        if count == win:
            return True
        else:
            return False
            


    
    cols = []
    for i in range(len(grid[0])):
        temp = []
        for j in range(len(grid)):
            temp.append(grid[j][i])
        cols.append(temp)
    
    for item in cols:
        if new_check(item, to_win):
            return True
    
    for item in grid:
        if new_check(item, to_win):
            return True

    l = 0
    r = 0
    while (l+to_win-1) <= len(grid):
        while (r+to_win-1) < len(grid[0]):
            temp = grid[l][r]
            if temp:
                count = 1
                for i in range(1, to_win):
                    if grid[l+i][r+i] == temp:
                        count += 1
                    else:
                        temp = grid[l+i][r+i]
                        count = 1
                    if count == to_win:
                        return True
                if count == to_win:
                    return True
            r += 1
        l += 1

    l = len(grid) - 1
    r = len(grid) - 1
    while (l-to_win+1) >= 0:
        while (r-to_win+1) >= 0:
            print(r)
            temp = grid[l][r]
            if temp:
                print(temp)
                count = 1
                for i in range(1, to_win):
                    if grid[l-i][r-i] == temp:
                        count += 1
                    else:
                        temp = grid[l-i][r-i]
                        count = 1
                    if count == to_win:
                        return True
                if count == to_win:
                    return True
            r -= 1
        l -= 1
    return False
        

    


lst = make_grid(4,4)
drop(lst, 0, 'a')
drop(lst, 1, 'a')
drop(lst, 1, 'b')
drop(lst, 1, 'a')
drop(lst, 2, 'b')
drop(lst, 2, 'a')
drop(lst, 3, 'a')

print(check_winner(lst))


