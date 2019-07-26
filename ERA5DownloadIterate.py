# -*- coding: utf-8 -*-
"""
Created on Thu May 23 17:11:25 2019

@author: mjolly
"""

import os
import glob
import cdsapi
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import matplotlib as mpl
from datetime import datetime, timedelta

#list_of_days=list(range(1,7))

vars = ['2m_temperature','2m_dewpoint_temperature','10m_u_component_of_wind','10m_v_component_of_wind','surface_pressure','surface_solar_radiation_downwards','total_precipitation']
dovars = ['10m_u_component_of_wind','10m_v_component_of_wind']
for v in vars:
    if v in dovars:
        for yr in range(1979,2019):
            
            base_dir_and_filename_2_download='/run/media/mjolly/BigFire/projects/era5/data/era5_single_levels_%s_%s' % (v,yr)
            print (base_dir_and_filename_2_download)
            c = cdsapi.Client()  
            save_filename=base_dir_and_filename_2_download+'.nc'
            c.retrieve('reanalysis-era5-single-levels',
            {'product_type':'reanalysis',
                   'format':'netcdf',
                   'variable':str(v),
                  'year': str(yr),
                  "month":["01","02","03","04","05","06","07","08","09","10","11","12"],
                  "day": ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"],
                  'time':['00:00','01:00','02:00','03:00','04:00','05:00','06:00','07:00','08:00','09:00','10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00','20:00','21:00','22:00','23:00']},save_filename)