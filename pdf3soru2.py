import math
a=2
i=0

while i < 4:
    f=4*(math.e**(-0.5*a))-a
    f1=-2*(math.e**(-0.5*a))-1
    ak=a-(f/f1)
    a=ak
    i += 1

print("4 yineleme sonucu bulunan kok",ak)
