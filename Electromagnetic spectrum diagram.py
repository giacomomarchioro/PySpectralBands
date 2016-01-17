# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 23:40:16 2013

@author: giacomo
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker
from pylab import *
t = np.arange(0,16, .01)
#s = np.sin(2*np.pi*t)
fig  = plt.figure(figsize=(16,3), dpi=150)
ax = fig.add_subplot(1,1,1)
ax.axes.get_yaxis().set_visible(False)
ax.set_xticks('15')
plt.xticks([15], '15')
#ax.plot(t,s)
plt.axis([0.2,16,-1,1])
ax.set_xscale('log')
from matplotlib.ticker import FormatStrFormatter
ax.xaxis.set_minor_formatter(matplotlib.ticker.ScalarFormatter())
ax.xaxis.set_minor_formatter(matplotlib.ticker.FormatStrFormatter('%.1f'))
#ax.xaxis.set_minor_formatter(matplotlib.ticker.FuncFormatter(lambda x, pos: str(int(round(x)))))
ax.xaxis.set_major_formatter(matplotlib.ticker.ScalarFormatter())
ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter('%d'))
ax.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, pos: str(int(round(x)))))
ax.tick_params(axis='x',which='minor',bottom='on')
#-----------ULTRA VIOLET-----------------
UV = plt.axvspan(0.1,0.4, facecolor='w', alpha=0.5,linewidth=2.5)
#UVA = plt.axvspan(0.315,0.4, facecolor='w', alpha=0.5,linewidth=2.5)
#UVB = plt.axvspan(0.315,0.280, facecolor='w', alpha=0.5,linewidth=2.5)
#UVC = plt.axvspan(0.280,0.100, facecolor='w', alpha=0.5,linewidth=2.5)
#NUV = plt.axvspan(0.400,0.300, facecolor='w', alpha=0.5,linewidth=2.5)
#MUV = plt.axvspan(0.300,0.200, facecolor='w', alpha=0.5,linewidth=2.5)
#FUV = plt.axvspan(0.200,0.122, facecolor='w', alpha=0.5,linewidth=2.5)
#H_Lyman_alfa=plt.axvspan(0.122,0.121, facecolor='w', alpha=0.5,linewidth=2.5)
#EUV=plt.axvspan(0.121,0.010, facecolor='w', alpha=0.5,linewidth=2.5)
#VUV=plt.axvspan(0.200,0.010, facecolor='w', alpha=0.5,linewidth=2.5)
#------------VISIBLE--------------
#VIS=plt.axvspan(0.380, 0.700, facecolor='w', alpha=0.5,linewidth=2.5)
VIOLET=plt.axvspan(0.380,0.450, facecolor='violet', alpha=0.5,linewidth=2.5)
BLUE=plt.axvspan(0.450,0.495, facecolor='b', alpha=0.5,linewidth=2.5)
GREEN=plt.axvspan(0.495,0.570, facecolor='g', alpha=0.5,linewidth=2.5)
YELLOW=plt.axvspan(0.570,0.590, facecolor='y', alpha=0.5,linewidth=2.5)
ORANGE=plt.axvspan(0.590,0.620, facecolor='orange', alpha=0.5,linewidth=2.5)
RED=plt.axvspan(0.620,0.750, facecolor='r', alpha=0.5,linewidth=2.5)
#-----------INFRA RED------------
NIR=plt.axvspan(0.75,1.4, facecolor='w', alpha=0.5,linewidth=2.5)
SWIR=plt.axvspan(1.4,3,facecolor='w', alpha=0.5,linewidth=2.5)
MWIR=plt.axvspan(3,8,facecolor='w', alpha=0.5,linewidth=2.5)
LWIR = plt.axvspan(8,15, facecolor='w', alpha=0.5,linewidth=2.5)
FIR =  plt.axvspan(15,1000, facecolor='w', alpha=0.5,linewidth=2.5)
#-------CIE DIVISON SCHEME--------
#IR_A=plt.axvspan(0.700,1.4, facecolor='w', alpha=0.5,linewidth=2.5)
#IR_B=plt.axvspan(1.4,3, facecolor='w', alpha=0.5,linewidth=2.5)
#IR_C=plt.axvspan(3,1000, facecolor='w', alpha=0.5,linewidth=2.5)
#-------ISO 20573 SCHEME-----
#NIR_iso=plt.axvspan(0.78,3, facecolor='w', alpha=0.5,linewidth=2.5)
#MIR_iso=plt.axvspan(3,50, facecolor='w', alpha=0.5,linewidth=2.5)
#FIR_iso=plt.axvspan(50,1000, facecolor='w', alpha=0.5,linewidth=2.5)
#------Astronomy division scheme---
#NIR_astro=plt.axvspan(0.7,5, facecolor='w', alpha=0.5,linewidth=2.5)
#MIR_astro=plt.axvspan(5,40, facecolor='w', alpha=0.5,linewidth=2.5)
#FIR=plt.axvspan(40,350, facecolor='w', alpha=0.5,linewidth=2.5)

#savefig("exercice_4.png",dpi=150)
plt.show()

