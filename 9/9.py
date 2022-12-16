def print_state(state):
    for i in state:
        print(i)
def update_state(state,move)

if __name__ == '__main__':
    import os

    inp_path = os.path.join(
        os.path.dirname(__file__),
        "input1"
    )

    with open(inp_path,"r") as inp_f:
        moves = [(raw.split(' ')[0],int(raw.split(' ')[1])) for raw in inp_f.read().split('\n') if raw != '']
        print(moves)