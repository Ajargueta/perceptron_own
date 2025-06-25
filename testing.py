def loadData(matrixToLoad: list[list[int]], path):
    file = open(path, 'r')
    row = []
    for line in file:
        cleanLine = line.strip().split(',')
        cleanLine.pop()
        row = [int(x) for x in cleanLine]
        matrixToLoad.append(row.copy())

def runRNA(matrixWeights : list[list[int]], matrixInputs : list[list[int]], numNeurons : int, posibleOutputs: str,theta : int = 0):
    for numRowCurrInput in range(len(matrixInputs)):
        vectorCurrentInputs = matrixInputs[numRowCurrInput]
        y = ''
        for numCurrentNeuron in range(numNeurons):
            yIn = 0
            Weight = matrixWeights[numCurrentNeuron]
            for individualEntry in vectorCurrentInputs:
                yIn += (vectorCurrentInputs[individualEntry] * Weight[individualEntry])
            y += activationFunction(yIn, theta)
        print(posibleOutputs[int(y , 2)])

def activationFunction(yIn, theta):
    if yIn > theta:
        return '1'
    else:
        return '0'

def main():
    matrixWeights = []
    matrixInputs = []
    pathWeights = 'Weights.txt'
    pathInputs = 'inputs.txt'
    numNeurons = 3
    theta = 0
    posibleOuputs = 'ABCDEJKN'
    loadData(matrixWeights, pathWeights)
    loadData(matrixInputs, pathInputs)
    runRNA(matrixWeights, matrixInputs, numNeurons, posibleOuputs, theta)
    
if __name__ == '__main__':
    main()
