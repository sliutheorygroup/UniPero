import dpdata
d_lmp = dpdata.System('last.dump')
d_lmp.to('vasp/poscar','POSCAR')
