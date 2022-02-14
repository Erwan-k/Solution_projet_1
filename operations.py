from math import gcd

#Operations sur des polynomes
def somme_rationnels(a,b):
    [N_a,D_a],[N_b,D_b] = a,b
    s = [N_a*D_b+N_b*D_a,D_a*D_b]
    c = gcd(s[0],s[1])
    return [int(s[0]/c),int(s[1]/c)]

def produit_rationnels(a,b):
    [N_a,D_a],[N_b,D_b] = a,b
    s = [N_a*N_b,D_a*D_b]
    c = gcd(s[0],s[1])
    return [int(s[0]/c),int(s[1]/c)]
    
def produit_polynomes(P,Q):
    n,p = len(P),len(Q)
    s = []
    for i in range(n+p-1):
        coeff = [0,1]
        for k in range(i+1):
            if k < len(P) and i-k < len(Q):
                coeff = somme_rationnels(coeff,produit_rationnels(P[k],Q[i-k]))
        s += [coeff]
    return s

def somme_polynome(P,Q):
    s = []
    for i in zip(P,Q):
        s += [somme_rationnels(i[0],i[1])]
    p,q = len(P),len(Q)
    if p>q:
        P,Q,p,q = Q,P,q,p
    if p<q:
        s += Q[p:]
    return s

def produit_scalaire_polynome(scalaire,poly):
    for i in range(len(poly)):
        stock = produit_rationnels(poly[i],scalaire)
        s = gcd(stock[0],stock[1])
        poly[i] = [int(stock[0]/s),int(stock[1]/s)]
    return poly


#Ecriture de polynomes
def simplifier_fraction(rapport):
    [x,y] = rapport
    z = gcd(x,y)
    return [int(x/z),int(y/z)]

def ecrire_polynome(points):
    s = ""
    for i in range(len(points)-1,-1,-1):
        #Gestion du signe
        if points[i][1] < 0:
            [points[i][0],points[i][1]] = [-points[i][0],-points[i][1]]
            
        #Simplification de la fraction
        points[i] = simplifier_fraction(points[i])
        
        #Entier si entier
        if points[i][1] == 1:
            #Cas ou le nombre vaut 0
            if points[i][0] == 0:
                pass
            #Cas ou le nombre vaut 1
            elif points[i][0] == 1:
                if i == 0:
                    s+="+1"
                elif i == 1:
                    s+="+x"
                else:
                    s+="+x^{"+str(i)+"}"
            #Cas ou le nombre vaut -1
            elif points[i][0] == -1:
                if i == 0:
                    s+="-1"
                elif i == 1:
                    s+="-x"
                else:
                    s+="-x^{"+str(i)+"}"
            #Cas ou le nombre est positif
            elif points[i][0] > 0:
                if i == 0:
                    s+="+"+str(points[i][0])
                elif i == 1:
                    s+="+"+str(points[i][0])+"x"
                else:
                    s+="+"+str(points[i][0])+"x^{"+str(i)+"}"
            #Cas ou le nombre est négatif
            else:
                if i == 0:
                    s+=str(points[i][0])
                elif i == 1:
                    s+=str(points[i][0])+"x"
                else:
                    s+=str(points[i][0])+"x^{"+str(i)+"}"
            
        #Ajout de fraction
        else:
            #Cas ou le numerateur vaut 0
            if points[i][0] == 0:
                pass
            #Cas ou le rapport est positif
            if points[i][0] > 0:
                if i == 0:
                    s+="+\\\\frac{"+str(points[i][0])+"}{"+str(points[i][1])+"}"
                elif i == 1:
                    s+="+\\\\frac{"+str(points[i][0])+"}{"+str(points[i][1])+"}x"
                else:
                    s+="+\\\\frac{"+str(points[i][0])+"}{"+str(points[i][1])+"}x^{"+str(i)+"}"
            #Cas ou le rapport est négatif
            if points[i][0] > 0:
                if i == 0:
                    s+="-\\\\frac{"+str(-points[i][0])+"}{"+str(points[i][1])+"}"
                elif i == 1:
                    s+="-\\\\frac{"+str(-points[i][0])+"}{"+str(points[i][1])+"}x"
                else:
                    s+="-\\\\frac{"+str(-points[i][0])+"}{"+str(points[i][1])+"}x^{"+str(i)+"}"
    return s[1:]





