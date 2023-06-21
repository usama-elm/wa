import numpy as np
import matplotlib.pyplot as plt

#exemple de matrice A, tel que [[0, 1, 0],
#                               [1, -4, 1],
#                               [0, 1, 0]] laplacien discret

A = np.ones((3, 3))

def discrete_laplacien(M):
    """Renvoie le laplacien discret de la matrice M"""
    n, m = M.shape
    L = np.zeros((n, m))
    for i in range(1, n-1):
        for j in range(1, m-1):
            L[i, j] = M[i+1, j] + M[i-1, j] + M[i, j+1] + M[i, j-1] - 4*M[i, j]
    return L

def gray_scott_update(A, B, DA, DB, f, k, delta_t):
    """Renvoie les matrices A et B après un pas de temps delta_t"""
    """Le feed rate est le kill rate avec LA/LB les laplaciens discrets de A et B"""

    L_A = discrete_laplacien(A)
    L_B = discrete_laplacien(B)

    #Gray-Scott formula
    A += delta_t * (DA * L_A - A*B**2 + f * (1 - A))
    B += delta_t * (DB * L_B + A*B**2 - (k + f) * B)

    return A, B

def get_intitial_configuration(N, random_influence=0.2):
    """On crée les matrices avec 1 et 0, puis on ajoute un peu de bruit pour améliorer la diffusion
    puis on crée un carré de concentration 0.5 au centre et un carré de concentration 0.25 au centre"""

    """Chaque pixel est égal a une concentration de A et B, a cotnient le u et b le v de maniere que u+2v -> 3v"""
    A = (1-random_influence) * np.ones((N, N)) + random_influence *  np.random .random((N, N))
    B = random_influence * np.random.random((N, N))
    
    N2 = N//2
    r = int(N/10)
    A[N2-r:N2+r, N2-r:N2+r] = 0.50
    B[N2-r:N2+r, N2-r:N2+r] = 0.25
    
    return A, B

def draw(A, B):
    #La partie plot du truc
    fig, ax = pl.subplot(1,2,figsize=(5.65,4))
    ax[0].imshow(A, cmap=jet)
    ax[1].imshow(B, cmap=jet)
    ax[0].axis('off')
    ax[1].axis('off')
    ax[0].set_title('A')
    ax[1].set_title('B')

#Update time
delta_t = 1.0

#Diffusion coefficients
DA = 0.19
DB = 0.05

#taux aleatoires de feed/kill
#f=rd.uniform(0.1, 0.01)
#k=rd.uniform(0.045, 0.07)

f=0.06
k=0.062

#taille de la matrice
N= 256
N_simulation_steps=10000

A, B = get_intitial_configuration(200)

for t in range(N_simulation_steps):
    A, B = gray_scott_update(A, B, DA, DB, f, k, delta_t)
    if t%100 == 0:
        draw(A, B)
        plt.savefig('images/gray_scott_{}.png'.format(t))
        plt.close()
        print(t)

draw(A,B)