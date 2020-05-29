#cambiare le costanti
#i file dat si devono chiamare pallinometro-n.dat dove n è il numero (1 <= n <= infinito)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy import stats
import pandas as pd
import math
from scipy import interpolate

#funzioni
def PrevisionePossion(Lambda,xmin,xmax,n):
    x = np.arange(xmin,xmax)
    k_list = [] 
    sigma_k_list = []
    for i in x:
        p_i = stats.poisson.pmf(i, Lambda)
        k_list.append( n*p_i )
        sigma_k_list.append( math.sqrt( n * p_i * (1-p_i) ) )  
    k = np.asarray(k_list)
    sigma_k = np.asarray(sigma_k_list)
    return k, sigma_k

#costanti
N_misure = 200
nlineelist = [5, 5, 5, 25, 25, 25, 50, 50, 50]
lambdalist = [0.250, 1.250, 2.500, 1.250, 6.250, 12.500, 2.500, 12.500, 25.000
delimitatore = '\t' #delimitatore per i valori dat (al momento è una tablatura)

#ciclo principale
i = 1
while i <= len(nlineelist):
    data1 = np.genfromtxt('pallinometro-'+str(i)+'.dat',
                     skip_header=0,
                     skip_footer=0,
                     names=True,
                     dtype=None,
                     delimiter=delimitatore)

    
    j = 0
    col1, col2, col3 = [], [], []
    
    while j < len(data1):
        splitted = str(data1[j]).split(",")
        temp1 = splitted[0].replace('(','')
        temp2 = splitted[1].replace(' ','')
        temp3 = splitted[2].replace(')','')
        temp3bis = temp3.replace(' ','')
        col1.append(float(temp1)) #numero della misura (non serve)
        col2.append((float(temp2))) #y
        col3.append(float(temp3bis)) #m
        
        splitted = []
        temp1, temp2, temp3, temp3bis = "","","",""
        j += 1
    
    xmin = 0
    nlinee = nlineelist[(i-1)]
    xmax = nlinee+1
    mylambda = lambdalist[(i-1)]
    Nbins= xmax-xmin
    plt.hist(col2,bins=Nbins,range=(xmin-0.5,xmax-0.5),label="Data")
    x_prev = np.arange(xmin,xmax)
    k_prev, sigma_k_prev = PrevisionePossion(mylambda,xmin,xmax,N_misure)
    plt.errorbar(x_prev,
             k_prev,
             yerr=sigma_k_prev,
             marker='o',markersize=3,linestyle='none',label="Previsione")
    plt.xlabel("")
    plt.ylabel("")
    plt.legend()  
    sbplt = "91"+str(i)
    plt.savefig("data/"+str(i)+".png")
    plt.clf()
    
    xmin, xmax, nlinee, mylambda, Nbins = "","","","",""
    data1, col1, col2, col3 = [], [], [], []
    j = 0
    print ("passo: "+str(i))
    
    i += 1
