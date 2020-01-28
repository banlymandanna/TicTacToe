"""
a = 'X  |     |   '
b = '___|_____|___'
c = '   |     |   '
d = '   |  O  |   '
e = '___|_____|___'
f = '   |     |   '
g = '   |     |   '


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

"""
a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "



A = [[a,"|",b,"|",c], [ "-","-","-","-","-"], [d,"|",e,"|",f], [ "-","-","-","-","-"], [g,"|",h,"|",i]]

class Tic:
    def Board(self):

        for x in A:
            print"".join(x)

c = Tic()
c.Board()

