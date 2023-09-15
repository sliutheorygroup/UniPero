import dpdata 
import numpy as np 
dp_d = dpdata.LabeledSystem('./',fmt='abacus/md')[1:1500:5] 
dp_d.to_deepmd_raw("deepmd") 
dp_d.to_deepmd_npy("deepmd") 
