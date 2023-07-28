import cmath  # import module

a = 1  # first parameter
b = 5  # second parameter
c = 6  # third parameter

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
