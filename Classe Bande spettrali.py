# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 09:57:41 2013

@author: giacomo
"""

class SpectralBand(object):
    def __init__(self,longname,shortname, band, color,info):
        self.longname=longname
        self.shortname=shortname
        self.bandmicron=band
        self.color= color
        self.info=info

#------------------------------------
#-----------ULTRA VIOLET-----------------
#------------------------------------
UV = SpectralBand("Ultraviolet","UV",[0.1,0.4],'w')
UVA= SpectralBand("Utrlaviolet A","UVA",[0.315,0.4],'w')
UVB= SpectralBand("Ultraviolet B       ","UVB      ",[0.315,0.280],'w')
UVC= SpectralBand("Ultraviolet C       ","UVC      ",[0.280,0.100],'w')
NUV= SpectralBand("Near Ultraviolet    ","NUV      ",[0.400,0.300],'w')
MUV= SpectralBand("Middle Ultraviolet  ","MUV      ",[0.300,0.200],'w')
FUV= SpectralBand("Far Ultraviolet     ","FUV      ",[0.200,0.122],'w')
H_L= SpectralBand("Hydrogen Lyman-alpha","H Lyman-α",[0.122,0.121],'w')
EUV= SpectralBand("Extreme Ultraviolet ","EUV      ",[0.121,0.010],'w')
VUV= SpectralBand("Vacuum Ultraviolet  ","VUV      ",[0.200,0.010],'w')
#------------------------------------
#------------VISIBLE--------------
#----------------------------------
VIS=SpectralBand("Visible","",[0.380, 0.700],'w')
VIOLET=SpectralBand("Violet","Violet",[0.380,0.450],'violet')
BLUE=SpectralBand("B","Blue",[0.450,0.495],'b')
GREEN=SpectralBand("G","Green",[0.495,0.570],'g')
YELLOW=SpectralBand("Y","Yellow",[0.570,0.590],'y')
ORANGE=SpectralBand("Orange","Orange",[0.590,0.620],'orange')
RED=SpectralBand("R","Red",[0.620,0.750],'r')
#----------HUMAN VISION------------
ConetypeS=SpectralBand("Cone Type S"," β",[0.400,0.500],'violet') 
ConetypeM=SpectralBand("Cone Type M"," γ",[0.450,0.630],'y')  
ConetypeL=SpectralBand("Cone Type L"," ρ",[0.500,0.700],'orange')  

#------------------------------------
#-----------INFRA RED------------
#------------------------------------
NIR =SpectralBand("Near-infrared            ","NIR ",[0.75,1.4],'w')
SWIR=SpectralBand("Short-wavelength infrared","SWIR",[1.4,3],'w')
MWIR=SpectralBand("Mid-wavelength infrared  ","MWIR",[3,8],'w')
LWIR=SpectralBand("Long-wavelength infrared ","LWIR",[8,15],'w')
FIR =SpectralBand("Far infrared             ","FIR ",[15,1000],'w')
#-------CIE DIVISON SCHEME--------
IR_A=SpectralBand("Near-Infrared","IR-A",[0.700,1.4],'w')
IR_B=SpectralBand("Mid Infrared ","IR-B",[1.4,3],'w')
IR_C=SpectralBand("Far Infrared ","IR-C",[3,1000],'w')
#-------ISO 20573 SCHEME-----
NIR_iso=SpectralBand("Near-Infrared","NIR",[0.78,3],'w')
MIR_iso=SpectralBand("Mid Infrared ","MIR",[3,50],'w')
FIR_iso=SpectralBand("Far Infrared ","FIR",[50,1000],'w')
#------Astronomy division scheme---
NIR_astro=SpectralBand("Near-Infrared","NIR",[0.7,5],'w')
MIR_astro=SpectralBand("Mid Infrared ","MIR",[5,40],'w')
FIR_astro=SpectralBand("Far Infrared ","FIR",[40,350],'w')
