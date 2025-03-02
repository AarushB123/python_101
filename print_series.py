"""
1
1, 2
1, 2, 3
1, 2, 3, 4
1, 2, 3, 4, 5
"""

def print_series(x):

    for i in range(1, x+1, 1):
        s = ""
        for a in range(1, i+1,1):
            #s = s + str(a) + ", "
            s += str(a) + ", "
        print(s [:-2])  

print_series(10)
