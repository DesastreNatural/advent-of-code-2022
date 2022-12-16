def tmax(l):
    if len(l) != 0:
        return max(l)
    else:
        return -1

def is_visible(a,b,trees,r_trees):
    return ((trees[a][b] > tmax(trees[a][:b])) or (trees[a][b] > tmax(trees[a][b+1:]))) or ((r_trees[b][a] > tmax(r_trees[b][:a])) or (r_trees[b][a] > tmax(r_trees[b][a+1:])))

def get_score_for_line(th,line):
    if len(line) == 0:
        return 0
    score = 1
    for i in line:
        if i >= th:
            return score
        score += 1
    return score - 1

def get_scenic_score(a,b,trees,r_trees):
    th = trees[a][b]
    return get_score_for_line(th,list(reversed(trees[a][:b]))) * get_score_for_line(th,trees[a][b+1:]) * get_score_for_line(th,list(reversed(r_trees[b][:a]))) * get_score_for_line(th,r_trees[b][a+1:]) 

if __name__ == '__main__':
    import os

    inp_path = os.path.join(
        os.path.dirname(__file__),
        "input"
    )

    with open(inp_path,"r") as inp_f:
        trees = [tuple(map(int,raw)) for raw in inp_f.read().split('\n') if raw != '']
        r_trees = list(zip(*trees))
        visible_trees = 0
        for i in range(len(trees)):
            for j in range(len(r_trees)):
                if is_visible(i,j,trees,r_trees):
                    visible_trees += 1
        print("First solution:",visible_trees)
        scores = []
        for i in range(len(trees)):
            for j in range(len(r_trees)):
                scores.append(get_scenic_score(i,j,trees,r_trees))
        print("Second solution:",max(scores))
