# This program calculates the ratio of the negative, positives and zero values in an array
positives = []
negatives = []
zeros = []
def plusMinus(n:int, arr):
    for i in arr:
        if i > 0:
            positives.append(i)
        elif i < 0:
            negatives.append(i)
        else:
            zeros.append(i)
    print('{0:0.6f}'.format(len(positives)/n))
    print('{0:0.6f}'.format(len(negatives)/n))
    print('{0:0.6f}'.format(len(zeros)/n))

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int,input().rstrip().split()))
    plusMinus(n,arr)