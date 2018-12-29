# -*- coding: utf-8 -*-
"""
Authors: Tim Hessels
         IHE Delft 2017
Contact: t.hessels@un-ihe.org
Repository: https://github.com/wateraccounting/SEBAL
Module: SEBAL/SEBAL


Description:
This module contains a compilation of scripts and functions to run pySEBAL
(http://www.wateraccounting.org/)
"""

from .pySEBAL_code_new import main as pySEBAL_new
from .pySEBAL_code_new_s2 import main as pySEBAL_new_s2
from .pySEBAL_code import main as pySEBAL
from SEBAL.pySEBAL import pySEBAL_input_LANDSAT
from SEBAL.pySEBAL import pySEBAL_input_MODIS
from SEBAL.pySEBAL import pySEBAL_input_PROBAV_VIIRS

__all__ = ['pySEBAL_code', 'pySEBAL_code_new', 'pySEBAL_code_new_s2','pySEBAL_input_LANDSAT', 'pySEBAL_input_MODIS', 'pySEBAL_input_PROBAV_VIIRS']

__version__ = '0.1'
