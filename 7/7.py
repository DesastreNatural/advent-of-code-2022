from functools import reduce
import operator

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

def part1(dfs,data=[]):
    for key in dfs.fs.keys():
        if type(dfs.fs[key]) is dict:
            total_folder += part1(dfs.fs[key])
        else:
            total_folder += dfs.fs[key]

if __name__ == '__main__':
    import os

    inp_path = os.path.join(
        os.path.dirname(__file__),
        "input1"
    )

    with open(inp_path,"r") as inp_f:
        terminal = [raw for raw in inp_f.read().split('\n') if raw != '']
        dfs = dummyFs()
        i = 0
        state = 'normal'
        while(i != len(terminal)):
            if state == 'normal':
                if terminal[i].startswith('$'):
                    print(terminal[i])
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
        print(dfs.fs)
