import os
import math

LS = 5000000
atoms = 20
NBIN = 100

def main():
    sample = 0
    num_files = 116
    dftx, dfty, dftz, dpx, dpy, dpz = 0, 0, 0, 0, 0, 0
    fxdft, fydft, fzdft, fxdp, fydp, fzdp = [0] * LS, [0] * LS, [0] * LS, [0] * LS, [0] * LS, [0] * LS
    fx, fy, fz = [0] * LS, [0] * LS, [0] * LS
    fxerror, fyerror, fzerror = 0, 0, 0
    rangeL, rangeH, rangebin = 0, 1, 0.05
    binx, biny, binz = 0, 0, 0
    area1, area2, area3 = 0, 0, 0
    hisbx, hisby, hisbz = [0] * NBIN, [0] * NBIN, [0] * NBIN

    for i in range(NBIN):
        hisbx[i] = 0
        hisby[i] = 0
        hisbz[i] = 0

    sample = 0
    for i in range(num_files):
        filename = "{:03d}.f.out".format(i)
        if os.path.exists(filename):
            with open(filename, "r") as file:
                for line in file:
                    if line.startswith('#'):
                        continue  # Skip comments
                    data = line.strip().split()
                    if len(data) == 6:
                        dftx, dfty, dftz, dpx, dpy, dpz = map(float, data)
                        fxdft[sample] = dftx
                        fydft[sample] = dfty
                        fzdft[sample] = dftz
                        fxdp[sample] = dpx
                        fydp[sample] = dpy
                        fzdp[sample] = dpz
                        sample += 1
        else:
            print("File {} does not exist".format(filename))

    M = sample
    print("M:", M)
    if M > LS:
        print("The size of the array is too small!")
        exit(-10)

    area1 = 0
    area2 = 0
    area3 = 0
    with open("Force-all", "w") as fp:
        for i in range(M):
            fx[i] = abs(fxdft[i] - fxdp[i])
            fy[i] = abs(fydft[i] - fydp[i])
            fz[i] = abs(fzdft[i] - fzdp[i])
            fxerror += fx[i]
            fyerror += fy[i]
            fzerror += fz[i]
            binx = int((fx[i] - rangeL) / rangebin)
            biny = int((fy[i] - rangeL) / rangebin)
            binz = int((fz[i] - rangeL) / rangebin)
            if binx < NBIN:
                hisbx[binx] += 1
                area1 += 1
            if biny < NBIN:
                hisby[biny] += 1
                area2 += 1
            if binz < NBIN:
                hisbz[binz] += 1
                area3 += 1
            fp.write("{:.2f}  {:.2f}\n".format(fxdft[i], fxdp[i]))
            fp.write("{:.2f}  {:.2f}\n".format(fydft[i], fydp[i]))
            fp.write("{:.2f}  {:.2f}\n".format(fzdft[i], fzdp[i]))

    with open("Force-error", "w") as fp:
        fp.write("num: {} :F: {:.2f} eV/A \n".format(M, (fxerror + fyerror + fzerror) / M / 3))

    with open("distribution-force", "w") as fp:
        for i in range(NBIN):
            fp.write("{:.2f}  {:.2f}\n".format(rangeL + (i + 0.5) * rangebin, ((hisbx[i] + hisby[i] + hisbz[i]) / (area1 + area2 + area3)) * 100))

if __name__ == "__main__":
    main()
