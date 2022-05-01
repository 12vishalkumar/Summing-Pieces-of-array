import math
import os
import random
import re
import sys

# Complete the 'summingPieces' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.

def summingPieces(arr):
    # Write your code here
    mod = 10**9+7
    if(len(arr) == 1):
        return arr[0]
    else:   
        sum_arr = [0 for i in range(len(arr))]    
        sum_arr[0] = arr[0]
        for i in range(1, len(arr)):
            sum_arr[i] = (sum_arr[i-1] + (pow(2, i, mod)*arr[i])%mod)%mod
        sum_1 = arr[0]
        for n in range(1, len(arr)):
            sum_1 = ( 2*sum_1 + ( (pow(2, n+1, mod)-1)*arr[n] )%mod + sum_arr[n-1] )%mod
    return sum_1  
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = summingPieces(arr)
    fptr.write(str(result) + '\n')
    fptr.close()