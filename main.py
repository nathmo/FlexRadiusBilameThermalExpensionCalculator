import numpy as np
import matplotlib.pyplot as plt

#enter your n points here
x = np.array([1.439, 3.835, 6.158, 8.8, 11.684, 14.567, 18.09, 22.175, 25.539, 28.342, 32.746, 35.71, 39.874, 42.277, 45.4, 48.924, 50.926, 53.569, 57.413, 61.578, 65.021, 69.186, 74.952, 78.476, 81.759, 85.043, 88.326, 91.61, 95.374])
y = np.array([19.297, 19.372, 19.772, 19.932, 20.253, 20.573, 20.733, 21.134, 21.294, 21.454, 21.614, 21.694, 21.774, 21.855, 21.774, 21.855, 21.855, 21.774, 21.694, 21.614, 21.454, 21.214, 20.974, 20.653, 20.333, 20.173, 19.852, 19.372, 18.971])
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

