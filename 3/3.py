def eval_item_priority(letter):
    return ord(letter) - 96 if letter.islower() else ord(letter) - 64 + 26

def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

if __name__ == '__main__':
    import os

    inp_path = os.path.join(
        os.path.dirname(__file__),
        "input"
    )
    with open(inp_path,"r") as inp_f:
        raw_data = [match for match in inp_f.read().split("\n") if match != ""]
        data = [[match[:len(match)//2],match[len(match)//2:]]  for match in raw_data]
        intersections = [list(set(i).intersection(set(j))) for i,j in data]
        print("First solution:",sum([sum(map(eval_item_priority,i)) for i in intersections]))
        print("Second solution:",sum(map(eval_item_priority,[list(set(a).intersection(set(b).intersection(set(c))))[0] for a,b,c in chunks(raw_data,3)])))

