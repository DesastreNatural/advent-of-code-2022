def is_marker(lst):
    for j in lst:
        if lst.count(j) > 1:
            return False
    return True

if __name__ == '__main__':
    import os

    inp_path = os.path.join(
        os.path.dirname(__file__),
        "input"
    )

    with open(inp_path,"r") as inp_f:
        raw = inp_f.read().replace("\n","")
        for i in range(0,len(raw)):
            if is_marker(raw[i:i+4]):
                print("First solution:",i+4)
                break
        for i in range(0,len(raw)):
            if is_marker(raw[i:i+14]):
                print("Second solution:",i+14)
                break

