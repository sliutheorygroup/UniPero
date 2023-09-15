from dpdata import LabeledSystem, MultiSystems
from glob import glob

"""
process multi systems
"""
fs = glob("./0*/")  # remeber to change here !!!
ms = MultiSystems()
for f in fs:
    try:
        ls = LabeledSystem(f,fmt='abacus/scf')
    except:
        print(f)
    if len(ls) > 0:
        ms.append(ls)

ms.to_deepmd_raw("deepmd")
ms.to_deepmd_npy("deepmd")
