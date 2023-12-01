import sys

sum = 0
DIGITS = {
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

with open("resources/input_01.txt","r") as f:    
    while True:
        line = f.readline()
        
        if not line:
            break
        
        first_digit = None
        prev_index = sys.maxsize
        
        for key in DIGITS:
            index = line.find(key)
            if index != -1 and index < prev_index :
                first_digit = key
                prev_index = index  
                
        x = None
        n = prev_index if first_digit != None else len(line)
        
        for i in range(n):
            if line[i].isdigit():
                x = line[i]
                break 
            
        if x != None :             
            sum += int(x)*10
        else:
            sum += DIGITS.get(first_digit)*10
        
        
        prev_index = sys.maxsize       
        second_digit = None
        
        line_r = line[::-1]
        
        for key in DIGITS:
            index = line_r.find(key[::-1])
            if index != -1 and index < prev_index :
                second_digit = key
                prev_index = index
                
        y = None
        n = prev_index if second_digit != None else len(line)
        
        for i in range(n):
            if line_r[i].isdigit():
                y = line_r[i]
                break     
            
        if y != None :             
            sum += int(y)
        else:
            sum += DIGITS.get(second_digit)

        print(line,"first digit:",first_digit,x,"second digit:",second_digit,y)
        
    f.close()

print(sum)