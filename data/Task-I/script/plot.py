import os
import re
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator, FuncFormatter

file_names = [
    "BST-300K", "BST-450K", "BT-300K", "BT-450K", "BZT-BCT-300K", "BZT-BCT-450K",
    "NN-BT-300K", "NN-BT-450K", "PIN-PMN-PT-300K", "PIN-PMN-PT-450K", "PMN-PT-300K",
    "PMN-PT-450K", "PT-300K", "PT-450K", "PZT-300K", "PZT-450K", "ST-300K", "ST-450K",
    "ST-900K", "BST-900K", "BT-900K", "BZT-BCT-900K", "NN-BT-900K", "PIN-PMN-PT-900K",
    "PMN-PT-900K", "PT-900K", "PZT-900K", "KNN-300K", "KNN-450K", "KNN-900K"
]

system_temps = {} 

for filename in file_names:
    match = re.match(r'([A-Z-]+)-(\d+)K', filename)
    if match:
        system_name = match.group(1)
        temp = match.group(2)
    
        if system_name not in system_temps:
            system_temps[system_name] = []
        system_temps[system_name].append(temp)

num_rows = len(system_temps)
num_cols = 3
fig, axs = plt.subplots(num_rows, num_cols, figsize=(15, 20), sharex='col') 

for i, (system_name, temps) in enumerate(system_temps.items()):
    for j, temp in enumerate(temps):
        ax = axs[i, j]
        
        aimd_plotted = False  
        dp_plotted = False   
        file_path = os.path.join("energy-vs-time", f"{system_name}-{temp}K")

        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        x = []  
        y_aimd = []  
        y_dp = []  
        
        for line in lines:
            if line.startswith("#"):
                continue
            columns = line.split()
            if len(columns) >= 3:
                x.append(float(columns[0])/100) 
                y_aimd.append(float(columns[1]) / 40) 
                y_dp.append(float(columns[2]) / 40)    
        
        if not aimd_plotted and y_aimd:
            ax.plot(x, y_aimd, color='k', linestyle='-', label='AIMD')
            aimd_plotted = True
        
        if not dp_plotted and y_dp:
            ax.plot(x, y_dp, color='b', linestyle='-', label='DP')
            dp_plotted = True

        ax.set_title(f'{system_name} {temp}K')
        ax.set_xlabel('Time (ps)')
        ax.set_ylabel('Energy (eV/atom)')
        ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: '{:.2f}'.format(x)))
        ax.legend().set_visible(False)
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right')
fig.suptitle('AIMD fitting: Energy vs. Time - All systems', fontsize=16, y=1.0)
plt.tight_layout()
plt.show()
plt.savefig("energy-vs-time.png")