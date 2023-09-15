import os
import matplotlib.pyplot as plt

data_directory = os.path.join(os.getcwd(), 'collect', 'energy')

x_data = []
y_data = []

file_list = [file for file in os.listdir(data_directory) if file.startswith('EN-')]

for file_name in file_list:
    file_path = os.path.join(data_directory, file_name)
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    for line in lines:
        if line.strip():  
            x, y = map(float, line.strip().split())
            x_data.append(x)
            y_data.append(y)

output_file_path = os.path.join(os.getcwd(), 'AIMD-energy-fitting')
with open(output_file_path, 'w') as output_file:
    for x, y in zip(x_data, y_data):
        output_file.write(f"{x} {y}\n")


plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, color='purple', s=50)
plt.plot([min(x_data), max(x_data)], [min(x_data), max(x_data)], color='red', linestyle='--')
plt.xlabel('AIMD (eV)')
plt.ylabel('DP (eV)')
plt.title('AIMD Energy Fitting')
plt.grid(False)  

plt.savefig('AIMD-energy-fitting.png')
plt.show()
