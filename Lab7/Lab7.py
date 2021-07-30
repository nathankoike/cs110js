# Lab7.py (Campbell)

def main():
    #print(twice([4, 3, 2, 5]))

    #triangle(7)

    #print(min_grid([[4, 5, 6],[7, 9, 3]]))
    
    print(has_most([[1, 2, 2],[3, 1, 3]], 3))
    #print(has_most([[1, 2, 2],[3, 1, 3]], 2))

    #print(is_descending([]))
    #print(is_descending([4]))
    #print(is_descending([4, 3]))
    #print(is_descending([4, 4]))

    # print(all_same([]))    # t
    # print(all_same([[1]])) # t
    # print(all_same([[1,2,1,1],[1,1,1,1]])) # f
    # print(all_same([[1,1,1,1],[1,1,1,1]])) # t

    # print(all_different([])) # t
    # print(all_different([[1]])) # t
    # print(all_different([[1,2,1,1],[1,1,1,1]])) # f
    # print(all_different([[1,1,1,1],[1,1,1,1]])) # f
    # print(all_different([[1,2,3,4],[5,6,7,8]])) # t

    # grid1 = [[1,2,2,4],
    #          [5,2,2,8]]
    # print(find_box(grid1, 2))

    # print(find_rectangle(grid1, 1, 1, 8))
    # print(find_rectangle(grid1, 2, 2, 2))
    # print(find_rectangle(grid1, 2, 3, 2))
    pass

def get_dimensions(grid):
    """ return the number of rows and columns in a grid """
    return (len(grid), 0 if len(grid)==0 else len(grid[0]))

def twice(lst):
    new_lst = []
    for i in lst:
        for _ in range(2):
            new_lst.append(i)
    return new_lst

def triangle(n):
    '''if n == 0:
        return
    if n == 1:
        print('*')
    if n > 1:
        before = n-1
        for _ in range(before):
            print(end=' ')
        for _ in range(n - before):
            print
            '''
    for x in range(n):
        for _ in range(n - 1 - x):
            print(end=' ')
        if x == 0:
            for _ in range(x + 1):
                print('*', end='')
        else:
            for _ in range(2 * x + 1):
                print('*', end='')
        print()


def min_grid(grid):
    smallest = grid[0][0]
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] < smallest:
                smallest = grid[r][c]
    return smallest


def has_most(grid, target):

    if grid == [[]]:
        return -1
    if len(grid) == 1:
        for i in grid:
            for char in grid[i]:
                if target == r:
                    return 0
        return -1
    for x in range(len(grid)):
        i = has_most(grid[1:], target)
        if i == -1:
            return -1
        index_num = i + x
        return index_num




def is_descending(lst):
    pass

def all_same(grid):
    pass

def all_different(grid):
    pass

def find_box(grid, target):
    pass

def find_rectangle(grid, H, W, target):
    pass


if __name__ == "__main__":
    main()
