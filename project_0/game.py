import numpy as np
a = 2.2
b = 3.5
c = 3.4
x = list(np.arange(0, 10, 0.1))
y = list(np.arange(0, 10, 0.1))
z = list(np.arange(0, 10, 0.1))
for i in x:
    for j in y:
        for k in z:
            summ = i+j+k 
            if a*i > summ and b*j > summ and c*k > summ:
                print(i, j, k)
                print()                    