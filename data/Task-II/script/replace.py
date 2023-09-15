
file_path = "./POSCAR"

replacements = {
    "TYPE_10": "Nb",
    "TYPE_11": "Mg",
    "TYPE_12": "In",
    "TYPE_13": "Zn",
    "TYPE_14": "O",
    "TYPE_9": "Zr",
    "TYPE_8": "Ti",
    "TYPE_7": "Hf",
    "TYPE_6": "Na",
    "TYPE_5": "K",
    "TYPE_4": "Bi",
    "TYPE_3": "Sr",
    "TYPE_2": "Ca",
    "TYPE_1": "Pb",
    "TYPE_0": "Ba"
}

with open(file_path, "r") as f:
    content = f.read()

for old_str, new_str in replacements.items():
    content = content.replace(old_str, new_str)

with open(file_path, "w") as f:
    f.write(content)
