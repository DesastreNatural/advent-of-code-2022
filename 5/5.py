def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def single_move_crane(stacks_dummy,bfrom,bto):
    tmp = stacks_dummy[bfrom-1].pop()
    stacks_dummy[bto-1].append(tmp)
    return stacks_dummy

def move_crane(stacks_dummy,qty,bfrom,bto):
    for i in range(qty):
        stacks_dummy = single_move_crane(stacks_dummy,bfrom,bto)
    return stacks_dummy

def move_crane9001(stacks_dummy,qty,bfrom,bto):
    tmp = stacks_dummy[bfrom-1][-qty:]
    stacks_dummy[bfrom-1] = stacks_dummy[bfrom-1][:-qty]
    stacks_dummy[bto-1] += tmp
    return stacks_dummy

if __name__ == '__main__':
    import os

    inp_path = os.path.join(
        os.path.dirname(__file__),
        "input"
    )

    with open(inp_path,"r") as inp_f:
        r_stack, r_moves = inp_f.read().split('\n\n')
        r_stack = list(reversed(r_stack.split("\n")))
        stacks = [[brick for brick in stack if brick != ' '] for stack in zip(*[[j[1] for j in chunks(level,4)] for level in r_stack[1:]])]
        stacks_part2 = [[brick for brick in stack if brick != ' '] for stack in zip(*[[j[1] for j in chunks(level,4)] for level in r_stack[1:]])]
        moves = [list(map(int,r_move.replace("move ","").replace("from ","").replace("to ","").split(" "))) for r_move in r_moves.split("\n") if r_move != ""]
        for qty,bfrom,bto in moves:
            stacks = move_crane(stacks.copy(),qty,bfrom,bto)
            stacks_part2 = move_crane9001(stacks_part2.copy(),qty,bfrom,bto)
        print("First solution:","".join([i[-1] for i in stacks]))
        print("Second solution:","".join([i[-1] for i in stacks_part2]))