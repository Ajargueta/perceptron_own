import os

def extractData(matrixInputs: list[list[int]], path: str,vectorTargets: list[int], cols: int, rows: int):
    rowCounter = 0
    entriesFile = open(path, 'r')
    row = []
    for line in entriesFile:
        for i in range(cols):
            row.append(1) if line[i] == '#' else row.append(-1)
        rowCounter += 1
        if ((rowCounter % rows) == 0):
            matrixInputs.append(row.copy())
            row.clear()
    entriesFile.close
    fileTargets = open('targets.txt', 'r')
    for line in fileTargets:
        vectorTargets.append(line.strip())
    saveinFile(matrixInputs, 'inputs.txt')
            
def initializeWeights(matrixWeights: list[list[int]] , numNeurons:int, sizeMatrixEntries:int, initialValueWeights : int = 0, defualtValueBias: int = 1):
    for i in range(numNeurons):
        row = []
        for j in range(sizeMatrixEntries):
            row.append(initialValueWeights)
        row.append(defualtValueBias)
        matrixWeights.append(row)

def computeWeights(matrixInputs: list[list[int]], vectorTargets: list[int], matrixWeights : list[list[int]], numNeurons:int ,theta: int = 0, alpha: int = 1):
    for numRowCurrInput in range(len(matrixInputs)):
        vectorCurrentTargets = [int(x) for x in vectorTargets[numRowCurrInput].split(',')]
        vectorCurrentInputs = matrixInputs[numRowCurrInput]
        for numCurrentNeuron in range(numNeurons):
            yIn = 0
            Weight = matrixWeights[numCurrentNeuron]
            for individualEntry in vectorCurrentInputs:
                yIn += (vectorCurrentInputs[individualEntry] * Weight[individualEntry])
            y = int(activationFunction(yIn, theta))
            if y != vectorCurrentTargets[numCurrentNeuron]:
                weightsCorrection(Weight, vectorCurrentInputs ,vectorCurrentTargets[numCurrentNeuron], alpha)

def activationFunction(yIn : int, theta : int):
    if (yIn > theta):
        return '1'
    if (yIn < -theta):
        return '-1'
    else:
        return '0'

def weightsCorrection(vectorWeight : list[int], vectorInput : list[int], expectedTarget : int,alpha : int =1):
    for i in range(len(vectorInput)):
        w = vectorWeight[i] + ( alpha * expectedTarget * vectorInput[i])
        vectorWeight[i] = w
    biasPos = len(vectorWeight) - 1
    b = vectorWeight[biasPos] + (alpha * expectedTarget)
    vectorWeight[biasPos] = b
    
def saveinFile(matrixToSave : list[list[int]], path : str):
    file = open(path, 'w', encoding='utf-8')
    for i in range(len(matrixToSave)):
        row=''
        for j in range(len(matrixToSave[i])):
            row+= str(matrixToSave[i][j]) + ','
        row+='\n'
        file.write(row)
        
def main():
    matrixInputs = []
    vectorTargets = []
    matrixWeights = []
    theta = 0
    alpha = 1
    cols = 7
    rows = 9
    numNeurons = 3
    initialWeight = 0
    initialBias = 1
    results = 'ABCDEFJK'
    extractData(matrixInputs, 'entries.txt',vectorTargets, cols, rows)
    initializeWeights(matrixWeights, numNeurons, cols*rows, initialWeight, initialBias)
    computeWeights(matrixInputs, vectorTargets, matrixWeights, numNeurons, theta, alpha)
    saveinFile(matrixWeights, 'Weights.txt')
        
if __name__ == '__main__':
    main()    