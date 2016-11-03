# -*- coding: utf-8 -*-
"""
Rongxin Yin, 11/2/2016

"""
from __future__ import division

import csv
import pandas as pd
import numpy as np
#import matplotlib.pylot as plt
import datetime

import seaborn as sns

customers = pd.read_csv('../../2016/PGE/D1977_OFFICE_LBNL.csv', delimiter=',')