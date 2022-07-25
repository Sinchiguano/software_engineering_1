iteration=0
count=0


n=0
letterSample="hello, world"


while iteration<5:
    for letter in letterSample:
        count+=1
    print(iteration,"-",count)
    iteration+=1



countChar=0

for count in range(5):
    while(1):
        for tmp in letterSample:
            countChar+=1
        if iteration<5:
            break

    iteration+=1
    print(iteration," ",countChar)
