import random
import matplotlib.pyplot as plt


class Model():
    def __init__(self, a=1000, b=3, c=0, d=0.09, e=0.05, f=0.003, g=0.002, h=0.2):
        self.s = int(a)
        self.i = int(b)
        self.r = int(c)
        self.b = float(d)
        self.g = float(e)
        self.m1 = float(f)
        self.m2 = float(g)
        self.f = float(h)

    def create_graph(self):
        S = S2= S3 = S4 = self.s #здоровые
        I = I2 = I3 = I4 = self.i #больные
        R = R2 = R4 = self.r #мёртвые/выжившие


        N = S+I+R

        N = float(N)

        #счётчик времени
        t = 0
        t2 = 0
        t3 = 0
        t4 = 0

        #вероятность заболеть
        b = self.b

        #вероятность выздороветь
        g = self.g
        m1 = self.m1
        m2 = self.m2
        f = self.f

        sList = []
        iList = []
        rList = []

        sList2 = []
        iList2 = []
        rList2 = []

        sList3 = []
        iList3 = []

        sList4 = []
        iList4 = []
        rList4 = []

        while (I > 0) and (S > 0):
            newI = 0
            for i in range(S):
                if random.random() < b*(I/N):
                    newI += 1
            recoverI = 0
            for i in range(I):
                if random.random() < g:
                    recoverI += 1
            S -= newI
            I += (newI - recoverI)
            R += recoverI

            sList.append(S)
            iList.append(I)
            rList.append(R)
            t += 1

        while (S2>0) and (I2 > 0):
            N2 = S2+I2+R2
            N2 = float(N2)
            newI2 = 0
            for i in range(S2):
                if random.random() < b*(I2/N2):
                    newI2 += 1
            recoverI2 = 0
            for i in range(I2):
                if random.random() < g:
                    recoverI2 += 1
            b1 = 0
            for i in range(round(N2)):
                if random.random() < m2:
                    b1 += 1

            d1 = 0
            for i in range(S2):
                if random.random() < m1:
                    d1 += 1
            d2 = 0
            for i in range(I2):
                if random.random() < m1:
                    d2 += 1
            d3 = 0
            for i in range(R2):
                if random.random() < m1:
                    d3 += 1

            S2 -= newI2+b1-d1
            I2 += (newI2 - recoverI2)-d2
            R2 += recoverI2-d3
            sList2.append(S2)
            iList2.append(I2)
            rList2.append(R2)
            t2 += 1

        while (S3>0) and (I3 > 0):
            N3 = S2+I2
            N3 = float(N3)
            newI3 = 0
            for i in range(S3):
                if random.random() < b*(I3/N3):
                    newI3 += 1
            recoverI3 = 0
            for i in range(I3):
                if random.random() < g:
                    recoverI3 += 1
            b1 = 0
            for i in range(round(N3)):
                if random.random() < m2:
                    b1 += 1

            d1 = 0
            for i in range(S3):
                if random.random() < m1:
                    d1 += 1
            d2 = 0
            for i in range(I3):
                if random.random() < m1:
                    d2 += 1

            S3 -= newI2+b1-d1+recoverI3
            I3 += (newI3 - recoverI3)-d2
            sList3.append(S3)
            iList3.append(I3)
            t3 += 1

        while (S4>0) and (I4 > 0):
            N4 = S4+I4+R4
            N4 = float(N4)
            newI4 = 0
            for i in range(S4):
                if random.random() < b*(I4/N4):
                    newI4 += 1
            recoverI4 = 0
            for i in range(I4):
                if random.random() < g:
                    recoverI4 += 1
            b1 = 0
            for i in range(round(N4)):
                if random.random() < m2:
                    b1 += 1

            d1 = 0
            for i in range(S4):
                if random.random() < m1:
                    d1 += 1
            d2 = 0
            for i in range(I4):
                if random.random() < m1:
                    d2 += 1
            d3 = 0
            for i in range(R4):
                if random.random() < m1:
                    d3 += 1

            f1 = 0
            for i in range(R4):
                if random.random() < f:
                    f1 += 1

            S4 -= newI4+b1-d1+f1
            I4 += (newI4 - recoverI4)-d2
            R4 += recoverI4-d3-f1
            sList4.append(S4)
            iList4.append(I4)
            rList4.append(R4)
            t4 += 1

        f2 = plt.figure()
        plt.plot(rList, 'r', label='Recovered')
        plt.plot(iList, 'b', label='Infectives')
        plt.plot(sList, 'g', label='Susceptibles')
        plt.legend()
        plt.title('SIR model')
        plt.xlabel('time')
        plt.ylabel('population')
        f2.savefig('sir.png')

        f1 = plt.figure()
        plt.plot(rList2, 'r', label='Recovered')
        plt.plot(iList2, 'b', label='Infectives')
        plt.plot(sList2, 'g', label='Susceptibles')
        #plt.legend()
        plt.xlabel('time')
        plt.ylabel('population')
        plt.title('SIR model with birth and death')
        f1.savefig('sir2.png')

        f3 = plt.figure()
        plt.plot(iList3, 'b', label='Infectives')
        plt.plot(sList3, 'g', label='Susceptibles')
        #plt.legend()
        plt.xlabel('time')
        plt.ylabel('population')
        plt.title('SIS model with birth and death')
        f3.savefig('sir3.png')

        f4 = plt.figure()
        plt.plot(rList4, 'r', label='Recovered')
        plt.plot(iList4, 'b', label='Infectives')
        plt.plot(sList4, 'g', label='Susceptibles')
        plt.title('SIRS model with birth and death')
        #plt.legend()
        plt.xlabel('time')
        plt.ylabel('population')
        f4.savefig('sir4.png')