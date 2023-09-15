import os
import matplotlib.pyplot as plt

def extract_data(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    x_values = []
    y_values = []

    for line in lines:
        if line.strip():  
            x, y = map(float, line.strip().split())
            x_values.append(x)
            y_values.append(y)

    return x_values, y_values

def plot_scatter(x_data, y_data, x_label, y_label, title, color):
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data, y_data, color=color, s=50)
    plt.plot([min(x_data), max(x_data)], [min(x_data), max(x_data)], color='red', linestyle='--')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(False)  


def plot_bar(x_data, y_data, x_label, y_label, title, color):
    plt.figure(figsize=(10, 6))
    width = 0.04 
    plt.bar(x_data, y_data, color=color, alpha=0.5, width=width, align='center')  
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.grid(False)  

def main():
    data_directory = os.getcwd()

    
    force_all_file_path = os.path.join(data_directory, 'collect', 'force', 'Force-all')
    x_data_force, y_data_force = extract_data(force_all_file_path)
    plot_scatter(x_data_force, y_data_force, 'AIMD (eV/A)', 'DP (eV/A)', 'AIMD Force Fitting', 'green')
   

    
    distribution_force_file_path = os.path.join(data_directory, 'collect', 'force', 'distribution-force')
    dist_x, dist_y = extract_data(distribution_force_file_path)
    filtered_dist_x = [x for x in dist_x if 0 <= x <= 0.5]
    filtered_dist_y = [y for x, y in zip(dist_x, dist_y) if 0 <= x <= 0.5]  
    plt.figure(figsize=(10, 6))
    plt.scatter(x_data_force, y_data_force, color='green', s=50)
    plt.plot([min(x_data_force), max(x_data_force)], [min(y_data_force), max(y_data_force)], color='red', linestyle='--')
    plt.xlabel('DFT (eV/A)')
    plt.ylabel('DP (eV/A)')
    plt.title('Force')
    
    plt.axes([0.62, 0.2, 0.25, 0.25])  
    width = 0.04 
    plt.bar(filtered_dist_x, filtered_dist_y, color='green', alpha=0.5, width=width, align='center')  
    plt.xlabel('Error (eV/A)')
    plt.ylabel('Proportion')
    plt.title('Distribution of Error')

    plt.savefig('force.png')
    plt.show()

if __name__ == "__main__":
    main()
