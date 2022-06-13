# import numdifftools as nd

class func:
    powers = []
    coef = []
    point = []
    n = int(input('Enter the number of parameters: '))
    def __init__(self):       
        for i in range(self.n):
            self.coef.append(int(input('Enter x'+str(i) +' coefficient: ')))
            self.point.append(int(input('Enter x'+str(i) +' : ')))
            self.powers.append(int(input('Enter x'+str(i) +' power: ')))

    def myfunc(self,x):
        for i in range(self.n):
            x[i] = self.coef[i](x[i]**self.powers[i])

if __name__ == '__main__':
    f1 = func()
    print(f1.powers)



# %%
