from functools import reduce
import operator
import sys

sys.setrecursionlimit(2000)

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)
def setInDict(dataDict, mapList, value):
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value

class dummyFs:
    def __init__(self):
        self.whereami = ["/"]
        self.fs = {"/":{}}
    def cd(self,path):
        if path == '..':
            self.whereami = self.whereami[:-1]
        elif path == '/':
            self.whereami = ["/"]
        else:
            self.whereami.append(path)
            setInDict(self.fs,self.whereami,{})
    def ls(self,definer,name):
        if definer == 'dir':
            setInDict(self.fs,self.whereami + [name],{})
        else:
            setInDict(self.fs,self.whereami + [name],int(definer))

def resolve_folder_size(fs):
    total_folder = 0
    for key in fs.keys():
        if type(fs[key]) is dict:
            total_folder += resolve_folder_size(fs[key])
        else:
            total_folder += fs[key]
    return total_folder

def resolve_folders(fs):
    data = []
    for key in fs.keys():
        if type(fs[key]) is dict:
            data += [(key,resolve_folder_size(fs[key]))] + resolve_folders(fs[key])
    return data

def part1(fs):
    return sum([size for name,size in resolve_folders(fs) if size <= 100000])
def part2(fs):
    needed_space = 30000000 - (70000000 - resolve_folder_size(fs))
    return min([size for name,size in resolve_folders(fs) if size >= needed_space])

if __name__ == '__main__':
    import os

    inp_path = os.path.join(
        os.path.dirname(__file__),
        "input"
    )

    with open(inp_path,"r") as inp_f:
        terminal = [raw for raw in inp_f.read().split('\n') if raw != '']
        dfs = dummyFs()
        i = 0
        state = 'normal'
        while(i != len(terminal)):
            if state == 'normal':
                if terminal[i].startswith('$'):
                    if len(terminal[i].split(" ")) == 2:
                        [symbol, cmd] = terminal[i].split(" ")
                        state = "ls"
                    else:
                        [symbol, cmd, path] = terminal[i].split(" ")
                        dfs.cd(path)
                i += 1
            else:
                if terminal[i].startswith('$'):
                    state = 'normal'
                else:
                    [definer, name] = terminal[i].split(" ")
                    dfs.ls(definer,name)
                    i += 1
        print("First solution:",part1(dfs.fs))
        print("Second solution:",part2(dfs.fs))
