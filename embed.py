import ctypes
from ctypes import *
import ctypes.util
import os
import sys

path = ctypes.util.find_library(os.path.join(os.getcwd(),"simple-vm"))
