""" Utilities for converting an ascii table to hdf5 """
import os
from astropy.io import ascii

def replace_ext(filename, new_ext):
    '''
    replace a filename's extention with a new one
    '''
    if not new_ext.startswith('.'):
        new_ext = '.' + new_ext

    return '.'.join(filename.split('.')[:-1])  + new_ext

def ascii2hdf5(inputfile, outputfile, clobber=False, overwrite=True):
    """
    Convert a file to hdf5 using compression and path set to 'data'
    """
    tbl = ascii.read(inputfile)
    tbl.write(v, format='hdf5', path='data', compression=True,
              overwrite=overwrite)
    if clobber:
        os.remove(inputfile)
    return new_out
