#!/usr/bin/env python3

class Rational(object):
    def __init__(self, param1, param2):
            self.upper = param1
            self.lower = param2

    def __str__(self):
        return str(self.upper)+"/"+str(self.lower)
    def __add__(self,y):
        if self.lower != int(y.lower):
            yla1=self.upper
            yla2=y.upper
            ala1=self.lower
            ala2=y.lower
            yla2 = int(yla2)*ala1
            ala1 = int(ala1)*int(ala2)
            yla1 = int(yla1)*int(ala2)
            ala2 = int(ala2)*ala1
        return Rational(str(yla1+yla2),str(ala1))
    def __sub__(self,y):
        if self.lower != int(y.lower):
            yla1=self.upper
            yla2=y.upper
            ala1=self.lower
            ala2=y.lower
            yla2 = int(yla2)*ala1
            ala1 = int(ala1)*int(ala2)
            yla1 = int(yla1)*int(ala2)
            ala2 = int(ala2)*ala1
            
        return Rational(str(yla1-yla2),str(ala1))
    def __mul__(self,y):
        return Rational(str(self.upper*y.upper),str(self.lower*y.lower))
    def __truediv__(self,y):
        return Rational(str(self.upper*y.lower),str(self.lower*y.upper))
    def __eq__(self,y):
        if self.lower != y.lower:
            yla1=int(self.upper)
            ala1=int(self.lower)
            ala2=y.lower
            yla2=y.upper
            yla2 = yla2*ala1
            ala1 = ala1*ala2
            yla1 = yla1*ala2
            ala2 = ala2*ala1
            return yla1==yla2
        else:
            return self.upper==y.upper
    def __gt__(self,y):
        if self.lower != y.lower:
            yla1=self.upper
            yla2=y.upper
            ala1=self.lower
            ala2=y.lower
            yla2 = int(yla2)*ala1
            ala1 = int(ala1)*int(ala2)
            yla1 = int(yla1)*int(ala2)
            ala2 = int(ala2)*ala1
            return yla1>yla2
        else:
            return self.upper>y.upper
    def __lt__(self,y):
        if self.lower != y.lower:
            yla1=self.upper
            yla2=y.upper
            ala1=self.lower
            ala2=y.lower
            yla2 = int(yla2)*ala1
            ala1 = int(ala1)*int(ala2)
            yla1 = int(yla1)*int(ala2)
            ala2 = int(ala2)*ala1
            return yla1<yla2
        else:
            return self.upper<y.upper

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print((r1+r2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,4) < Rational(2,3))
    print(r1)
    print(r2)

if __name__ == "__main__":
    main()
