#_____________________________________________________________________________________________________________________
def M(i,j):
    s=0
    x=len(t[0])
    y=len(t)
    for k in range (x-1):
        for l in range (y-1):
            s+=(k**i)*(l**j)*t[l][k]
    return s

def n(i,j):
    return ((u(i,j))/((u(0,0))**(1+(i+j)/2)))

def x0():
    return (m[1][0])/(m[0][0])

def y0() :
    return (m[0][1])/(m[0][0])

def u (i,j):
    s=0
    x=len(t[0])
    y=len(t)
    for k in range (x-1):
        for l in range (y-1):
            s+=((k-x0())**i)*((l-y0())**j)*t[l][k]
    return s

def tablM():
    m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m[0][0]=M(0,0)
    m[0][1]=M(0,1)
    m[1][1]=M(1,1)
    m[0][2]=M(0,2)
    m[2][1]=M(2,1)
    m[1][2]=M(1,2)
    m[0][3]=M(0,3)
    m[1][0]=M(1,0)
    m[2][0]=M(2,0)
    m[3][0]=M(3,0)
    return m

def Hu ():
   I1=  (n(2,0)) + (n(0,2))
   I2= ((n(2,0))-(n(0,2)))**2 + 4*((n(1,1))**2)
   I3= (n(3,0)-3*(n(1,2)))**2 +(3*(n(2,1))-(n(0,3)))
   I4= (n(3,0)+(n(1,2)))**2+(n(2,1)+ n(0,3))**2
   I5=(n(3,0)-3*n(1,2))*(n(3,0)+n(1,2))*((n(3,0)+n(1,2))**2-3*(n(2,1)+n(0,3))**2)+(3*n(2,1)-n(0,3))*(n(2,1)+n(0,3))*(3*(n(3,0)+n(1,2))**2-(n(2,1)+n(0,3))**2)
   I6= (n(2,0)-n(0,2))*((n(3,0)+n(1,2))**2-(n(2,1)+n(0,3))**2)+4*n(1,1)/(n(3,0)+n(1,2))*(n(2,1)+n(0,3))
   I7= (3*n(2,1)-n(0,3))*(n(3,0)+n(1,2))*((n(3,0)+n(1,2))**2-3*(n(2,1)+n(0,3))**2)-(n(3,0)-3*n(1,2))*(n(2,1)+n(0,3))*(3*(n(3,0)+n(1,2))**2-(n(2,1)+n(0,3))**2)
   hu=[str(I1),str(I2),str(I3),str(I4),str(I5),str(I6),str(I7)]
   return hu

def getlist (b):
    aj=glob.glob(b+'*.jpg')
    ap=glob.glob(b+'*.png')
    li=[]
    for e in aj:
        li.append(e)
    for e in ap:
        li.append(e)
    return li
def calchu (e):
    global t
    global m
    imga = img.open(e)
    imga = imga.resize((1000,1000),img.ANTIALIAS)
    img0 = imga.convert('L') # conversion en niveau de gris
    t=np.array(img0)
    m=tablM()
    hu=Hu()
    hu.append(e)
    return hu

def maketabl (b):
    global t
    global m
    li=getlist (b)
    for e in li :
        hu=calchu(e)
        tableau.append(hu)
    return tableau

def writedoc (nametabl,pathi):  
    tableau= maketabl(pathi)
    fichier = open(nametabl,"w")  
    for i in range (len(tableau)) :
        for item in tableau[i]:
            fichier.write(str(item))
            fichier.write(" /// ")
        fichier.write("\n")
    fichier.close()

def ajout(nametabl,pathadd):
    tableau= maketabl(pathadd)
    fichier = open(nametabl,"a")  
    for i in range (len(tableau)) :
        for item in tableau[i]:
            fichier.write(str(item))
            fichier.write(" /// ")
        fichier.write("\n")
    fichier.close()
def getvalues (nametabl):
    tabl=open(nametabl,"r")
    tableau=[]
    for ligne in tabl :
        l=ligne.split(" /// ")
        tableau.append(l)
    return tableau

def indicemin(liste):
    maxi = liste[0]
    lon=len(liste)
    indice = 0
    for i in range(lon):
        if liste[i] >= maxi:
            maxi = liste[i]
            indice = i
    return indice

def comparaison (etest,nametabl):
    hu=calchu(etest)
    differences=[]
    tableau=getvalues(nametabl)
    for image in tableau:
        s=0
        for i in range (7):
            s+= abs(abs(float(hu[i]))-abs(float(image[i])))
        differences.append(s)
    indice=indicemin(differences)
    print( (tableau[indice][7]).lstrip(pathi))

                
    
    
#_________________________________________________________________________________________________________________________
from PIL import Image as img
import numpy as np
import glob
import matplotlib.image as mpimg
import numpy as np
global t
global m
t=[]
m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
pathi='C:/Users/emmab/Desktop/TIPE/Hu/pictures/'
nametabl="data.txt"
pathadd='C:/Users/emmab/Desktop/TIPE/Hu/picturesadd/'
tableau=[]

etest='d.jpg'

writedoc (nametabl,pathi)
comparaison (etest,nametabl)