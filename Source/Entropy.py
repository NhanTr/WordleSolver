import math;
def calc_entropy(countArr, totalCount):
    result = 0
    for count in countArr:
        if(count > 0): 
            p = count / totalCount
            result -= p * math.log2(p)
    return result

# p_arr = [0.1, 0.2, 0.7]
# print(calc_entropy(p_arr))

def calc_output(wordTest, wordResult):
    output = 0
    for i in range(5):
        if(wordTest[i] == wordResult[i]): output += 2 * 3 ** (4 - i)
        elif(wordTest[i] in wordResult): output += 1 * 3 ** (4 - i)
        else: output += 0
    return output

def entropySolver(words, candidateArray):
    currentEntropyValue = -1
    currentWord = ""
    totalCount = len(candidateArray)
    print(totalCount)
    if(totalCount == 1): return candidateArray[0]
    # print(candidateArray)
    for word in words:
        # print(word)
        countArr = [0] * (3 ** 5)
        for candidate in candidateArray:
            output = calc_output(word, candidate)
            countArr[output] += 1

        entropyValue = calc_entropy(countArr, totalCount)
        if(entropyValue >= currentEntropyValue):
            currentEntropyValue = entropyValue
            currentWord = word
    return currentWord

