from problem import *
from optimizer import *

def main():
    p, pType = selectProblem()
    alg = selectAlgorithm(pType)
    alg.run(p)
    p.describe()
    alg.displaySetting()
    p.report()  #Report results

def selectProblem():
    print("Select the problem type: ")
    print("1. Numeric")
    print("2. Tsp")
    pType = int(input("Enter the number: "))
    if pType == 1:
        p = Numeric()
    elif pType == 2:
        p = Tsp()
    else:
        print("Wrong Input")

    p.setVariables()
    return p, pType

def selectAlgorithm(pType):
    print()
    print("Select the Algorithm type: ")
    print("1. Steepest Ascent")
    print("2. First Choice")
    print("3. Gradient Descent")
    aType = int(input("Enter the number: "))
    ##if가 길어지면 코드가 복잡해지니 dictionary를 사용해보기
    optimizers = {1:'SteepestAscent()', 2:'FirstChoice()', 3:'GradientDescent()'}
    ##eval을 써서 String으로 들어오는것을 객체생성하는것으로 바꿔주기
    alg = eval(optimizers[aType])
    alg.setVariables(pType)
    

    return alg

main()