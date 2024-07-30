file = open("input.txt", "r")
lines = file.readlines()

class Caves:

    def __init__(self) -> None:
        self.caves = list()

    def addCave(self, cave):
        self.caves.append(cave)

    def getCave(self, name):
        for cave in self.caves:
            if cave.getName() == name: return cave
        return None

    def alreadyExist(self, name):
        return name in [c.getName() for c in self.caves]

    def getCaves(self): return self.caves

    def getCavesNames(self): return [c.getName() for c in self.caves]

    

class Cave:

    def __init__(self, name) -> None:
        self.name = name
        self.notPassed = True
        self.cnxs = list()

    def addCnx(self, cnx):
        self.cnxs.append(cnx)

    def getName(self): return self.name

    #debug
    def getCnxs(self): return self.cnxs


class LittleCave(Cave):

    def __init__(self, name):
        super().__init__(name)


class BigCave(Cave):

    def __init__(self, name):
        super().__init__(name)

    
allCaves = list()
caves = Caves()
for line in lines:
    c1, c2 = line.replace('\n', '').split('-') 
    if c1 not in caves.getCavesNames(): 
        if c1.islower(): caves.addCave(LittleCave(c1))
        else: caves.addCave(BigCave(c1))
    if c2 not in caves.getCavesNames():
        if c2.islower(): caves.addCave(LittleCave(c2))
        else: caves.addCave(BigCave(c2))


for line in lines:
    key, value = line.replace('\n', '').split('-')

    if key != 'end':
        if value != 'start': caves.getCave(key).addCnx(caves.getCave(value))
    if value != 'end':
        if key != 'start': caves.getCave(value).addCnx(caves.getCave(key))

allPaths = list()

#debug
for cave in caves.getCaves():
    print(cave.getName())

    print([c.getName() for c in cave.getCnxs()])

## Part1
"""
def getPath(cave, paths):
    if type(cave) is LittleCave and cave in paths: return None
    if len(cave.getCnxs()) == 0 and cave.getName() != "end": return None
    elif cave.getName() == "end": 
         path = paths.copy()
         path.append(cave)
         allPaths.append(path)
         return path
    path = paths.copy()
    path.append(cave)
    newPath = list()
    for c in cave.getCnxs():
        #print([d.getName() for d in paths]) #debug
        get_path = getPath(c, path)
        if get_path is not None:
            newPath.append(get_path)
    return newPath
        
getPath(caves.getCave("start"), list())
print(len(allPaths))
"""
##Part 2
def getPath(cave, paths, double_small=True):
    #print(paths.count(cave))
    dsml = double_small
    if len(cave.getCnxs()) == 0 and cave.getName() != "end": return None
    elif cave.getName() == "end": 
         path = paths.copy()
         path.append(cave)
         allPaths.append(path)
         return path
    if type(cave) is LittleCave and cave in paths and not double_small: return None
    elif type(cave) is LittleCave and cave in paths and double_small: dsml = False
    path = paths.copy()
    path.append(cave)
    newPath = list()
    for c in cave.getCnxs():
        #print([d.getName() for d in paths]) #debug
        get_path = getPath(c, path, dsml)
        if get_path is not None:
            newPath.append(get_path)
    return newPath
        
getPath(caves.getCave("start"), list())
print(len(allPaths))


    