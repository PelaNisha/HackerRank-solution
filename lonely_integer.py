# que one

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    li = []
    fi = []
    n = len(a)
    for i in range(0, n):
        if a[i] not in li:
            li.append(a[i])
        else:
            fi.append(a[i])
    print(li)
    print(fi)
    for i in range(0, len(li)):
        # print(li[i])
        if li[i] not in fi:
            return li[i]
        else:
            pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
