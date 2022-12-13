def is_a_fully_overlapped_couple(r,t):
    [rs,re] = r
    [ts,te] = t
    return (((rs <= ts) and (re >= te)) or ((ts <= rs) and (te >= re)))

def is_side_overlapped(r,t):
    [rs,re] = r
    [ts,te] = t
    return (((rs <= ts) and (re >= ts)) or ((ts <= rs) and (te >= rs)))

def is_overlapped(r,t):
    return is_side_overlapped(r,t) or is_side_overlapped(t,r)

if __name__ == '__main__':
    import os

    inp_path = os.path.join(
        os.path.dirname(__file__),
        "input"
    )

    with open(inp_path,"r") as inp_f:
        raw_data = [match for match in inp_f.read().split("\n") if match != ""]
        ranges = [[list(map(int,r.split('-'))) for r in couple.split(',')] for couple in raw_data]
        print("First solution:",sum([is_a_fully_overlapped_couple(i,j) for i,j in ranges]))
        print("Second solution:",sum([is_overlapped(i,j) for i,j in ranges]))