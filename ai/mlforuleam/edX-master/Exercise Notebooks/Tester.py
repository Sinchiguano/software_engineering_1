def findMax(someList):
    return max(someList)
    
def ex1(studentFunc):
    x = [0,2,4,6,205,6,67,2,546]
    try: assert(studentFunc(x)== findMax(x) )
    except AssertionError as e:
        print("Error on blah")
        raise AssertionError('Assert failure') #or raise e

    x= [-3,-24,-54,-0]
    assert(studentFunc(x)== findMax(x) )