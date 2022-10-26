import numpy as np

# Random numbers
a = np.random.random((3,2)) 
print(a)
b = np.random.randn(3,2)
print(b)

R = np.random.randn(10000)
print(R.mean(), R.var(), R.std())

R = np.random.randn(10, 3)
print(R.mean())

# random integer, low,high,size; high is exclusive
R = np.random.randint(3,10,size=(3,3))
print(R)

# with integer is between 0 up to integer exclusive
c = np.random.choice(7, size=10)
print(c)
# with an array it draws random values from this array
d = np.random.choice([1,2,3,4], size=8)
print(d)
