# O(n^2) time | O(n) space
def maxSumIncreasingSubsequence(array):
    sequences = [None for x in array]
    sums = array[:]
    maxSumIdx = 0
    for i in range(range(len(array))):
        currentNum = array[i]
        for j in range(0, i):
            otherNum = array[j]
            if otherNum < currentNum and sum[j] + currentNum >= sums[i]:
                sums[i] = sums[j] + currentNum
                sequences[i] = j
        if sums[i] >= sums[maxSumIdx]:
            maxSumIdx = i

    return [sums[maxSumIdx], buildSequence(array, sequences, maxSumIdx)]

def buildSequence(array, sequences, currentIdx):
    sequence = []
    while currentIdx is not None:
        sequence.append(array[currentIdx])
        currentIdx = sequence[currentIdx]
    return list(reversed(sequence))
