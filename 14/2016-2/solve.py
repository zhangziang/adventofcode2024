#coding: utf-8

def solve_one():
    result = []
    site_map = [[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]]
    loc = [1,1]
    directs = {"U": [-1,0], "D": [1, 0], "L": [0, -1], "R": [0, 1]} # U D L R

    for line in open("input"):
        for d in line.strip():
            direct = directs[d]
            new_loc_i = loc[0] + direct[0]
            new_loc_j = loc[1] + direct[1]
            if 0<= new_loc_i <= 2:
                loc[0] = new_loc_i
            if 0<= new_loc_j <= 2:
                loc[1] = new_loc_j
        result.append(site_map[loc[0]][loc[1]])
    return result
    
    

if __name__ == "__main__":
    print(solve_one())