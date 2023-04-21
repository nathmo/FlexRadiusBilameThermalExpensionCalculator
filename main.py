import numpy as np
import matplotlib.pyplot as plt

#enter your n points here
x = np.array([2., 3., 4., 5., 6.])
y = np.array([2., 6., 5., 5., 6.])
pol = np.polyfit(x,y,len(x)-1)  # polynomial coefficients

# derivative 1
polprime = []

for i in range(0,len(pol)-1):
    polprime.append(pol[i]*(len(pol)-1-i))

# derivative 2
polpprime = []

for i in range(0,len(polprime)-1):
    polpprime.append(polprime[i]*(len(polprime)-1-i))


xx = np.linspace(min(x),max(x))
yy = np.polyval(pol,xx)         # polynomial value in the points contained in xx
plt.plot(xx, yy, '-',x, y, 'ro')

yyy = np.polyval(polprime,xx)         # polynomial value in the points contained in xx
plt.plot(xx, yyy, '-',x, y, 'ro')

yyyy = np.polyval(polpprime,xx)         # polynomial value in the points contained in xx
plt.plot(xx, yyyy, '-',x, y, 'ro')

plt.axis([min(xx)-2, max(xx)+2, min(yy)-2, max(yy)+2])
plt.savefig('foo.png')

# print(pol)    # show the polynom coeeficient (for debugging purpose)
# print(polprime)
# print(polpprime)

# print radius
print("radius from each point : ")
for center in x:
    # formula for the radius of a curve in a point ()
    radius = (np.polyval(polpprime, center))/pow((1+pow(np.polyval(polprime, center), 2)), 1.5)
    print(radius)

