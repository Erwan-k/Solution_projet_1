
from operations import somme_rationnels,produit_rationnels,produit_polynomes,somme_polynome,produit_scalaire_polynome

def approximation_lagrange(pts):
    #Reprendre les points (pour transformer gérer les entiers et les rationnels)
    for i in range(len(pts)):
        if type(pts[i][0]) == type(1):
            pts[i][0] = [pts[i][0],1]
        if type(pts[i][1]) == type(1):
            pts[i][1] = [pts[i][1],1]
        
    s_poly = []
    for i in range(len(pts)):
        stock = produit_scalaire_polynome(pts[i][1],[[1,1]])
        for k in range(len(pts)):
            if i != k:
                coef_constant = somme_rationnels(pts[k][0],[-pts[i][0][0],pts[i][0][1]])
                coef_constant = produit_rationnels(pts[k][0],[coef_constant[1],coef_constant[0]])
                coef_dominant = somme_rationnels(pts[i][0],[-pts[k][0][0],pts[k][0][1]])
                coef_dominant = produit_rationnels([1,1],[coef_dominant[1],coef_dominant[0]])
                stock = produit_polynomes(stock,[ coef_constant,coef_dominant ])
        s_poly = somme_polynome(s_poly,stock)
    return s_poly

















