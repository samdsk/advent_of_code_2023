CUBES = {
    "red":12,
    "green":13,
    "blue":14
}

sum = 0

for line in open("resources/input_02.txt"):
    data = line.split(':')
    sets = data[1].split(';')
    gameID = data[0].split()[1]
    
    flag = True
    
    for extracts in sets:
        oneExtract = extracts.split(',')
        for cubes in oneExtract:
            n, color = cubes.strip().split()
            if int(n) > CUBES.get(color):
                flag = False
                break
            
        if not flag: break
        
    if flag :
        sum += int(gameID)
        
print(sum)