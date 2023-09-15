import dpdata
d_dump = dpdata.System("last.dump")
d_dump.to("lammps/lmp", "conf.lmp", frame_idx=0)
