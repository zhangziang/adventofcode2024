#coding: utf-8

def get_sub_checksum(start_pos, end_pos, id):
    return id*(start_pos + end_pos)*(end_pos-start_pos+1)//2

def solve_one():
    data = open("input").read().strip() # data len = 19999
    reverse_index = len(data) - 1
    reverse_id = len(data)//2
    if len(data) % 2 == 0:
        reverse_index = reverse_index - 1
    reverse_left = int(data[reverse_index])
    cursor_index = 0
    cursor_id = 0

    compacted_index = 0
    
    checksum = 0

    while True:
        if cursor_index > reverse_index:
            break
        if cursor_index % 2 == 0:
            cursor_val = int(data[cursor_index]) # cursor_val would not be zero
            if cursor_id == reverse_id:
                cursor_val = reverse_left
            # checksum cursor
            checksum += get_sub_checksum(compacted_index, compacted_index+cursor_val-1, cursor_id)
            compacted_index += cursor_val
            if cursor_id == reverse_id:
                break
            cursor_index += 1
            cursor_id += 1
        else:
            cursor_val = int(data[cursor_index])
            while cursor_val != 0:
                if cursor_index > reverse_index:
                    break
                if cursor_val >= reverse_left:
                    cursor_val -= reverse_left
                    checksum += get_sub_checksum(compacted_index, compacted_index+reverse_left-1,reverse_id)
                    compacted_index += reverse_left
                    # move to before data
                    reverse_index -= 2
                    reverse_id -= 1
                    reverse_left = int(data[reverse_index])
                else:
                    reverse_left -= cursor_val
                    checksum += get_sub_checksum(compacted_index, compacted_index+cursor_val-1,reverse_id)
                    compacted_index += cursor_val
                    cursor_val = 0
                    break
            cursor_index += 1
    return checksum


def solve_two():
    data = open("input").read().strip() # data len = 19999
    reverse_index = len(data) - 1
    reverse_id = len(data)//2
    if len(data) % 2 == 0:
        reverse_index = reverse_index - 1



    empty_blocks = [] #(start_index, cap, used)
    caled_index = []
    # fill all empty_bolcks
    cursor = 0
    for i,v in enumerate(data):
        _v = int(v)
        caled_index.append(cursor)
        if i%2 == 1:
            empty_blocks.append((cursor, _v))
        cursor += _v
        
    checksum = 0
    
    while reverse_id >= 0:
        reverse_val = int(data[reverse_index])
        moved = False
        _index = caled_index[reverse_index]
        for i, empty_block in enumerate(empty_blocks): # first check empty val is fit
            start_index, cap = empty_block
            if moved or start_index > _index:
                break
            if cap >= reverse_val:
                new_start_index = start_index
                new_cap = cap - reverse_val
                new_start_index = start_index + reverse_val
                moved = True
                checksum += get_sub_checksum(start_index, start_index+reverse_val-1, reverse_id)
                empty_blocks[i] = (new_start_index, new_cap)
                break
        if not moved: # cal checksum in original place
            checksum += get_sub_checksum(_index, _index+reverse_val-1, reverse_id)
        # move to next
        reverse_id -= 1
        reverse_index -= 2
    


    return checksum

if __name__ == "__main__":
    print(solve_one())
    print(solve_two())