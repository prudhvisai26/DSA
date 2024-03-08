"""
Problem statement
You have a 32-bit unsigned integer called 'num' and another integer called 'i'.

You need to perform the following operations on the 'num' integer based on the value of 'i':
1. Get the bit value at the "i"th position of "num".
2. Set the bit at the "i"th position of "num".
3. Clear the bit at the "i"th position of "num".


We are starting bits from 1 instead of 0. (1-based)
For Example:
N=25  i=3
Output : 0 29 25

Bit at the 3rd position from LSB is 0. (1 1 0 0 1)
The value of the given number after setting the 3rd bit is 29. (1 1 1 0 1)
The value of the given number after clearing the 3rd bit is 25. (1 1 0 0 1)

"""

def bitManipulation(num : int, i : int) -> List[int]:
    # Write your code here.
    pass
    mask=1<<(i-1)
    # print(mask)

    d=[]

    d1=num&mask

    if d1!=0:d.append(1)

    else:d.append(0)

    d.append(num|mask)

    d.append(num&~mask)
    # print(~mask)

    return d
