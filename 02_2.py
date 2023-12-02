import functools

CUBES = {
    "red":12,
    "green":13,
    "blue":14
}

def find(extracted: str,m: dict) -> dict:
        
    for cubes in extracted:
        n, color = cubes.strip().split()
        m.update({color:max(m.get(color,1),int(n))})
        
    return m

sum = 0

for line in open("resources/input_02.txt"):
    data = line.split(':')
    sets = data[1].split(';')
    gameID = data[0].split()[1]    
    
    minNeeded = {}
    
    for extracts in sets:
        oneExtract = extracts.split(',')
        minNeeded = find(oneExtract,minNeeded)
        
    sum += functools.reduce(lambda x,y : x*y,minNeeded.values())    
        
print(sum)

