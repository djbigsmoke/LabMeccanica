#cambiare le costanti
#i file dat si devono chiamare pallinometro-n.dat dove n è il numero (1 <= n <= infinito)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy import stats
import pandas as pd
import math
from scipy import interpolate
from scipy.stats import binom
from scipy.stats import chisquare

#costanti
N_misure = 200
nlineelist = [5, 5, 5, 25, 25, 25, 50, 50, 50]
plist = [0.05, 0.25, 0.5, 0.05, 0.25, 0.5, 0.05, 0.25, 0.5]
lambdalist = [0.250, 1.250, 2.500, 1.250, 6.250, 12.500, 2.500, 12.500, 25.000]
delimitatore = '\t' #delimitatore per i valori dat (al momento è una tablatura)

#ciclo principale
i = 1
while i <= len(nlineelist):
    data1 = np.genfromtxt('misure/pallinometro-'+str(i)+'.dat',
                     skip_header=0,
                     skip_footer=0,
                     names=True,
                     dtype=None,
                     delimiter=delimitatore)

    
    j = 0
    col1, col2, col3 = [], [], []
    
    frequenzetotali = np.empty((nlineelist[(i-1)]+1))
    
    while j < len(data1):
        splitted = str(data1[j]).split(",")
        temp1 = splitted[0].replace('(','')
        temp2 = splitted[1].replace(' ','')
        temp3 = splitted[2].replace(')','')
        temp3bis = temp3.replace(' ','')
        col1.append(float(temp1)) #numero della misura (non serve)
        col2.append((float(temp2))) #y
        col3.append(float(temp3bis)) #m
        frequenzetotali[int(temp2)] += 1
        
        splitted = []
        temp1, temp2, temp3, temp3bis = "","","",""
        j += 1
    
    #Disegno l'istogramma
    xmin = 0
    nlinee = nlineelist[(i-1)]
    xmax = nlinee+1
    Nbins= xmax-xmin
    plt.hist(col2,bins=Nbins,range=(xmin-0.5,xmax-0.5),label="Data")


    #CALCOLO LA DISTRIBUZIONE BINOMIALE
    p = plist[(i-1)]
    n = nlineelist[(i-1)]
    x = list(range(0,(int(nlineelist[(i-1)])+1)))
    l = 1

    bn = binom.pmf(x, n, p)
    binomm = (bn)*N_misure

    #Disegno la binomiale
    plt.plot(x, binomm, 'bo', ms=8, label='binom pmf')
    plt.xlabel("")
    plt.ylabel("")
    plt.legend()  
    sbplt = "91"+str(i)
    plt.savefig("data/"+str(i)+".png")
    plt.clf()
    
    #Calcolo la probabilità di successo supponendo che sia la media della colonna Y diviso il numero di righe
    mmean = np.mean(np.asarray(col2))
    probsuccesso = mmean/nlineelist[(i-1)]
    
    #Ottengo le frequenze osservate
    #frequenze = frequenzetotali/N_misure
    
    #Eseguo test del chi quadro
    #chi2 = chisquare(frequenze, binomm)
    
    xmin, xmax, nlinee, mylambda, Nbins = "","","","",""
    data1, col1, col2, col3, x, = [], [], [], [], []
    j = 0

    #Stampo
    print ("passo: "+str(i))
    print ("1 - Salvo su file l'istogramma")
    print ("2 - La probabilità di successo è "+str(probsuccesso))
    #print ("3 - Test del Chi Quadro:")
    #print (chi2)

    probsuccesso = ""
    chi2 = []
    binomm, frequenzetotali, frequenze = [], [], []
    
    i += 1

print ("Fine esecuzione del codice")
sleep(10000)
