%%writefile dataset_set_up.py
import json
import random
import os, sys
from IPython.display import display, clear_output, HTML
from random import randrange, choice
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"]=25,25
import numpy as np
import seaborn as sns
import re

random.seed(42)
!git clone http://gitlab.aicrowd.com/amazon-prime-air/airborne-detection-starter-kit.git
os.chdir("airborne-detection-starter-kit/data")