import os,multiprocessing
from subprocess import Popen, PIPE
import glob


rootdir = "/run/media/mjolly/BigFire/projects/era5/data"
cmds_list = []
for subdir, dirs, files in os.walk(rootdir):
    for f in files:
	if f.count("2m_dewpoint_temperature") > 0:
		filepath = os.path.join(subdir, f)
		if filepath.endswith(".nc"):
			ofile = filepath.replace(".nc",".flt")
			if ofile.count("2m_dewpoint_temperature") > 0:
				ofile = ofile.replace("2m_dewpoint_temperature","td2m")
			if ofile.count("_single_levels") > 0:
				ofile = ofile.replace("_single_levels","")

			cmd = "gdal_translate -of ENVI -co \"INTERLEAVE=BIP\" %s %s" % (filepath,ofile)
			os.system(cmd)
			cmds_list.append(cmd)




		

