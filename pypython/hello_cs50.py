
import time



inUserName=input("What is your name?\n")
#print(inUserName)



def main ():
    #print(inUserName)
    #print(f"hello, {inUseName}")
    counter=0
    while(counter<10):
        print(inUserName)
        time.sleep(1)
        counter+=1
        #print(counter)

if __name__=="__main__":
    main()



"""
while True:
localtime = time.localtime()
result = time.strftime("%I:%M:%S %p", localtime)
print(result)
time.sleep(1)
"""