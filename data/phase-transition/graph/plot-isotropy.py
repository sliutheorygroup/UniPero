#!/usr/bin/env python
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

plt.style.use('nature.mplstyle')

# Color
clr1 = np.array([ 46, 89,130]).reshape(1,-1)/255
clr2 = np.array([255,206,111]).reshape(1,-1)/255
clr3 = np.array([240, 83,120]).reshape(1,-1)/255
clr4 = np.array([ 69,189,156]).reshape(1,-1)/255
clr5 = np.array([196,151,178]).reshape(1,-1)/255
clr6 = np.array([169,184,198]).reshape(1,-1)/255
clr7 = np.array([135, 206, 235]).reshape(1,-1)/255
clr8 = np.array([255, 192, 203]).reshape(1,-1)/255
clr9 = np.array([50, 205, 50]).reshape(1,-1)/255

# Figure
fig = plt.figure(figsize=(6.8, 1.82))
gs = mpl.gridspec.GridSpec(1,3, width_ratios=[1, 1, 1], left=0.055, right=0.967, wspace=0.3,
                                 height_ratios=[1], bottom=0.143, top=0.980, hspace=0)

ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])

ax1.text(-0.18, 1.02, 'a', ha='center', va='top', fontsize=8, fontweight='bold', transform=ax1.transAxes)
ax2.text(-0.20, 1.02, 'b', ha='center', va='top', fontsize=8, fontweight='bold', transform=ax2.transAxes)
ax3.text(-0.20, 1.02, 'c', ha='center', va='top', fontsize=8, fontweight='bold', transform=ax3.transAxes)

# Function
def plot_lattice1(ax):
    ax.set_box_aspect(0.75)
    ax.set_xlabel(r' Temperature (K)')
    ax.set_ylabel(r' Lattice Constants ($\mathrm{\AA}$)')
    #ax.set(xlim=(-10.2, -9.2), ylim=(-10.2, -9.2))
    #ax.set_xticks(np.linspace(4.9, 5.4, 6))
    #ax.set_yticks(np.linspace(0.0, 0.3, 4))
    ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(2))
    #ax.plot(np.linspace(5.15, 5.15, 2), np.linspace(0, 0.35, 2), alpha=0.9, ls='--', c='C3', zorder=1)
    return ax

# Function
def plot_lattice2(ax):
    ax.set_box_aspect(0.75)
    ax.set_xlabel(r' Temperature (K)')
    ax.set_ylabel(r' Lattice Constants ($\mathrm{\AA}$)')
    ax.set(xlim=(30, 220), ylim=(3.89, 3.927))
    ax.set_yticks(np.linspace(3.89, 3.93, 5))
    #ax.set_xticks(np.linspace(0.0, 0.3, 4))
    ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(2))
    return ax


def plot_lattice3(ax):
    ax.set_box_aspect(0.75)
    ax.set_xlabel(r' Temperature (K)')
    ax.set_ylabel(r' Lattice Constants ($\mathrm{\AA}$)')
    ax.set(xlim=(25,320), ylim=(3.95, 4.052))
    #ax.set_xticks(np.linspace(-7, 8, 5))
    #ax.set_yticks(np.linspace(-7, 8, 5))
    ax.xaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(mpl.ticker.AutoMinorLocator(2))
    return ax


# Subfigure 1
f = open('new_PTO.dat','r')
data = np.loadtxt(f)
DFT = data[:,0]
DP1 = data[:,1]
DP2 = data[:,2]
DP3 = data[:,3]
DP4 = data[:,4]
DP5 = data[:,5]
DP6 = data[:,6]
#sizes = np.full_like(DFT, 1)
ax1.errorbar(DFT, DP1, yerr=DP2,capthick=0.5,capsize=1.0, c=clr7,label='$a$',marker='o')
ax1.errorbar(DFT, DP3, yerr=DP4,capthick=0.5,capsize=1.0, c=clr2,label='$b$',marker='o')
ax1.errorbar(DFT, DP5, yerr=DP6,capthick=0.5,capsize=1.0, c=clr1,label='$c$',marker='o')
ax1 = plot_lattice1(ax1)
ax1.legend(loc='best',frameon=False, ncol=1)
ax1.axvline(x=550, color='gray', linestyle='--')
ax1.text(0.5, 1.105, r'PbTiO$_3$', ha='center', va='top', transform=ax1.transAxes, fontsize=6.0)
ax1.text(0.2, 0.45, r'$P4mm$', ha='center', va='top', transform=ax1.transAxes, fontsize=6.0)
ax1.text(0.85, 0.45, r'$Pm\bar{3}m$', ha='center', va='top', transform=ax1.transAxes, fontsize=6.0)

# Subfigure 2
f = open('new_STO.dat','r')
data = np.loadtxt(f)
DFT = data[:,0]
DP1 = data[:,1]
DP2 = data[:,2]
DP3 = data[:,3]
DP4 = data[:,4]
DP5 = data[:,5]
DP6 = data[:,6]

#sizes = np.full_like(DFT, 1)
ax2.errorbar(DFT, DP1, yerr=DP2,capthick=0.5,capsize=1.0,c=clr7,label='$a$',marker='o')
ax2.errorbar(DFT, DP3, yerr=DP4,capthick=0.5,capsize=1.0, c=clr2,label='$b$',marker='o')
ax2.errorbar(DFT, DP5, yerr=DP6,capthick=0.5,capsize=1.0, c=clr1,label='$c$',marker='o')
ax2 = plot_lattice2(ax2)
ax2.axvline(x=170, color='gray', linestyle='--')
ax2.legend(loc='best',frameon=False)
ax2.text(1.81, 1.105, r'SrTiO$_3$', ha='center', va='top', transform=ax1.transAxes, fontsize=6.0)
ax2.text(1.5, 0.45, r'$I4/mcm$', ha='center', va='top', transform=ax1.transAxes, fontsize=6.0)
ax2.text(2.13, 0.45, r'$Pm\bar{3}m$', ha='center', va='top', transform=ax1.transAxes, fontsize=6.0)

# Subfigure 3
f = open('new_BTO.dat','r')
data = np.loadtxt(f)
DFT = data[:,0]
DP1 = data[:,1]
DP2 = data[:,2]
DP3 = data[:,3]
DP4 = data[:,4]
DP5 = data[:,5]
DP6 = data[:,6]
#sizes = np.full_like(DFT, 1)
ax3.errorbar(DFT, DP1, yerr=DP2,capthick=0.5,capsize=1.0, c=clr7,label='$a$',marker='o')
ax3.errorbar(DFT, DP3, yerr=DP4,capthick=0.5,capsize=1.0, c=clr2,label='$b$',marker='o')
ax3.errorbar(DFT, DP5, yerr=DP6,capthick=0.5,capsize=1.0, c=clr1,label='$c$',marker='o')
ax3 = plot_lattice3(ax3)
ax3.axvspan(0, 90, color='lightblue', alpha=0.5, linewidth=0)
ax3.axvspan(90, 140, color='#90ee90', alpha=0.5, linewidth=0)
ax3.axvspan(140, 200, color='#ffffcc', alpha=0.5, linewidth=0)
ax3.axvspan(200, 320, color='#ffc0cb', alpha=0.5, linewidth=0)
ax3.legend(loc='best',frameon=False)
ax3.text(3.12, 1.105, r'BaTiO$_3$', ha='center', va='top', transform=ax1.transAxes, fontsize=6.0)
ax3.text(2.71, 0.97, r'$R3m$', ha='center', va='top', transform=ax1.transAxes, fontsize=6.0)
ax3.text(2.9, 0.97, r'$Amm2$', ha='center', va='top', transform=ax1.transAxes, fontsize=6.0)
ax3.text(3.10, 0.97, r'$P4mm$', ha='center', va='top', transform=ax1.transAxes, fontsize=6.0)
ax3.text(3.32, 0.97, r'$Pm\bar{3}m$', ha='center', va='top', transform=ax1.transAxes, fontsize=6.0)


# Save
fig.savefig('Tc.jpg')
fig.savefig('Tc.pdf')


