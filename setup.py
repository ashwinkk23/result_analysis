import py2exe
from distutils.core import setup
import matplotlib
import matplotlib.backends.backend_tkagg
import numpy
matplotlib.matplotlib_fname()
matplotlib.use('TkAgg')

setup( windows=[{"script": "results_data_analysis_GUI.py"}],options={'py2exe': {"includes" : ["matplotlib.backends.backend_tkagg","FileDialog","scipy.special._ufuncs_cxx","scipy", "scipy.integrate", "scipy.special.*","scipy.linalg.*","scipy.sparse.csgraph._validation"]}} ,data_files=matplotlib.get_py2exe_datafiles() )