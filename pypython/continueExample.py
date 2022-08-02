numberstTaken=[1,2,3,4,5]



for n in range(10):
    if n in numberstTaken:
        continue
    print(n)



def beefFunction(tmp):
    print("we are here")
    print(tmp*3)

    #pass


def allowedDatingAge(age):
    message=""
    if age>=18:
        message="yes, you are allowed to get a partner"
    else:
        message="not, you are not allowed to get a partner"
    return message



def getGender(sex="Unknown"):
    if sex is "m":
        sex="Male"
    elif sex is "f":
        sex="female"
    return sex


def main():
    print("testing the real variable name")


    for n in range(10):
        if n in numberstTaken:
            continue
        print(n)
    beefFunction(3.4)
    print(allowedDatingAge(18))
    print(getGender("m"))
    print(getGender("f"))
    print(getGender())



if __name__=="__main__":
    main()
