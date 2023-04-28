import numpy as np
import matplotlib.pyplot as plt

import csv

# you must first use Fiji Image J software to measure
# ~20 point along the curve of your sample
# copy the table under Measure in an excel sheet (AS A CSV !!!) and open it below
# check the name and save it in the same folder as this script

"""
here is a sample of the measure table, the name are not included when you
copy paste it to excel.

24	0.000	31	31	31	78.476	20.653	78.480	20.645	0.018	0.018
25	0.000	20	20	20	81.759	20.333	81.760	20.335	0.018	0.018

"""
Tableau = []
with open('RadiusValue.csv', newline='') as f:
    reader = csv.reader(f)
    Tableau = [list(row) for row in reader]
    print(Tableau)
x= []
y = []
for line in Tableau :
    x.append(line[5]) # column 5 is the x coordinate
    y.append(line[6]) # column 6 is the y coordinate
#enter your n points here
x = np.array([1.439, 3.835, 6.158, 8.8, 11.684, 14.567, 18.09, 22.175, 25.539, 28.342, 32.746, 35.71, 39.874, 42.277, 45.4, 48.924, 50.926, 53.569, 57.413, 61.578, 65.021, 69.186, 74.952, 78.476, 81.759, 85.043, 88.326, 91.61, 95.374])
y = np.array([19.297, 19.372, 19.772, 19.932, 20.253, 20.573, 20.733, 21.134, 21.294, 21.454, 21.614, 21.694, 21.774, 21.855, 21.774, 21.855, 21.855, 21.774, 21.694, 21.614, 21.454, 21.214, 20.974, 20.653, 20.333, 20.173, 19.852, 19.372, 18.971])
pol = np.polyfit(x,y,7)  # polynomial coefficients
# polynome of degree 7 is enough
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

plt.axis([min(xx)-2, max(xx)+2, min(yy)-20, max(yy)+5])
plt.savefig('foo.png')

# print(pol)    # show the polynom coeeficient (for debugging purpose)
# print(polprime)
# print(polpprime)

# print radius

center = x.mean()
print("center : " + str(center))
curvature = (np.polyval(polpprime, center))/pow((1+pow(np.polyval(polprime, center), 2)), 1.5)
print("curvature : " + str(curvature))
print("radius of curvature : " + str(1/curvature))
# enter the Young modulus E and the thickness h for your sample here.
alphaA = 36.8*pow(10,-6)
ha = 0.009  # unit in meters
hb = 0.0055 # unit in meters
Ea = 70*pow(10,9)
Eb = 170*pow(10,9)
T = 100
k = curvature
top = (Ea**2)*(ha**4) + 4*Ea*Eb*(ha*hb)**2 + 4*Ea*Eb*ha*(hb**3) + (Eb**2)*(hb**4)
bottom = 6*Ea*Eb*(ha+hb)*ha*hb
quotient = k*top/(bottom*T)
print("using : ")
print("sample A thermal coeeficient : "+str(alphaA))
print("sample A thickness : "+str(ha))
print("sample B thickness : "+str(hb))
print("sample A Young Modulus : "+str(Ea))
print("sample B Young Modulus : "+str(Eb))
print("Temperature Delta : "+str(T))
print("------------------")
print("we get the Coeficeint of thermal Expension of B: " + str(alphaA - quotient))

