class Polynome():
    
    def __init__(self,coef):
        self.coef=coef
        for elt in self.coef:
            if not isinstance(elt,int):
                raise Exception("donnée invalide !{}".format(elt))
                break
            elif self.coef[0]==0:
                raise Exception("an ne doit pas être nul")
        
        
        
        
    def __str__(self):
        N=len(self.coef)
        l=list()
        ch=str()
        sgn=str()
        if len(self.coef)==1 and self.coef[0]==0:
            ch="0 (le polynome nul)"
        else:
            for i in range(N):
                x=abs(self.coef[i])
                if self.coef[i]>0:
                    sgn="+"
                else:
                    sgn="-" 
                if N>2:
                    if i<N-2 and x!=0 and x!=1:
                        if self.coef[i]>0 and i==0:
                            l.append(str(x)+"x^{0}".format(N-i-1))
                        else:
                            l.append("{}".format(sgn)+str(x)+"x^{0}".format(N-i-1))
                    elif i<N-2 and x!=0 and x==1:
                        if self.coef[i]>0 and i==0:
                            l.append("x^{0}".format(N-i-1))
                        else:
                            l.append("{1}x^{0}".format(N-i-1,sgn))
                    elif i==N-2 and x!=0:
                        l.append("{}".format(sgn)+str(x)+"x")
                    elif i==N-1 and x!=0:
                        l.append("{}".format(sgn)+str(x))
                elif N==2:
                    if i==N-2 and x!=0:
                        l.append(str(x)+"x")
                    elif i==N-1 and x!=0:
                        l.append("{}".format(sgn)+str(x))
                else:
                    l.append(str(x))
            ch="".join(l)
                
        return ch
    
    __repr__=__str__
            
            
    def degre(self):
        return len(self.coef)-1
    def coeficient_polynome(self):
        return self.coef[0]
    
    def plusP(self):
        self.coef=coef
        return Polynome(self.coef)
    def moinsP(self):
        for i in range(len(self.coef)):
            self.coef[i]=-self.coef[i]
        return Polynome(self.coef)
    
    def __add__(self,G):
        s=list()
        if len(self.coef)>len(G.coef):
            G.coef+=[0 for i in range(len(self.coef)-len(G.coef))]
        else:
            self.coef+=[0 for i in range(len(G.coef)-len(self.coef))]
        self.coef=self.coef[::-1]
        G.coef=G.coef[::-1]
            
        for i in range (max(len(self.coef),len(G.coef))):
            s.append(self.coef[i]+G.coef[i])
        s=s[::-1]
        S=Polynome(s)
        return S
    
    
    def __sub__(self,G):
        s=list()
        if len(self.coef)>len(G.coef):
            G.coef+=[0 for i in range(len(self.coef)-len(G.coef))]
        else:
            self.coef+=[0 for i in range(len(G.coef)-len(self.coef))]
        self.coef=self.coef[::-1]
        G=G.moinsP()  
        G.coef=G.coef[::-1]
        for i in range (max(len(self.coef),len(G.coef))):
            s.append(self.coef[i]+G.coef[i])
        s=s[::-1]
        S=Polynome(s)
        return S
    
    
    def __mul__(self,G):
        s=[]
        for i in range(self.degre()+G.degre()+1):
            a=0
            for j in range(i+1):
                if (i<=self.degre() and i-j<=G.degre()):
                    a=a+self.coef[j]*G.coef[i-j]
            s.append(a)
        S=Polynome(s)
        return S
    
    
    def __iter__(self):  
        return iter(self.coef)
    
    
    
    def evalP(self,x):
        r=0
        self.coef=self.coef[::-1]
        for i in range(len(self.coef)):
            r= r+ self.coef[i]*x**i
        return r
    
        
        
                
        
    
    
    __radd__=__add__
    __rsub__=__sub__
    

if __name__ == '__main__':
    p=Polynome([5,0])
    print(p)
    f=Polynome([7,2,3])
    f
    