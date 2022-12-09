def eval_item_priority(letter):
    return ord(letter) - 96 if letter.islower() else ord(letter) - 64 + 26
        
if __name__ == '__main__':
    import os

    inp_path = os.path.join(
        os.path.dirname(__file__),
        "input"
    )
    with open(inp_path,"r") as inp_f:
        data = [match. for match in inp_f.read().split("\n") if match != ""]
        #print("First solution:",(sum([outcome1(a,b) for [a,b] in data])))

