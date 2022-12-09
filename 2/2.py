def outcome1(opponent,to_be_played):
    opp = ord(opponent) - 64
    played = ord(to_be_played) - 87
    winner = (opp % 3) + 1
    outcome = 6
    if played == opp:
        outcome = 3
    elif winner != played:
        outcome = 0
    else:
        outcome = 6
    return (played + outcome)

def outcome2(opponent,n_outcome):
    opp = ord(opponent) - 65
    ocome = (((ord(n_outcome) - 89) + opp) % 3) + 1
    return ocome + ((ord(n_outcome) - 88) * 3)
    
if __name__ == '__main__':
    import os
    inp_path = os.path.join(
        os.path.dirname(__file__),
        "input"
    )
    with open(inp_path,"r") as inp_f:
        data = [match.split(" ") for match in inp_f.read().split("\n") if match != ""]
        print("First solution:",(sum([outcome1(a,b) for [a,b] in data])))
        print("Second solution:",(sum([outcome2(a,b) for [a,b] in data])))

