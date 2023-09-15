import os

# Enter the input and output paths below
input_path = "./traj.lammpstrj"
output_dir = "./"

with open(input_path, 'r') as f:
    lines = f.readlines()

num_files = len(lines) // 49 + 1

for i in range(num_files):
    start_index = i * 49
    end_index = min((i+1) * 49, len(lines))
    output_filename = "{:04d}.lammpstrj".format(i)
    output_path = os.path.join(output_dir, output_filename)
    with open(output_path, 'w') as f:
        f.writelines(lines[start_index:end_index])

