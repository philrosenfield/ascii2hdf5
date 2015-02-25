# ascii2hdf5
Command line tool to convert ascii table to hdf5

usage: ascii2hdf5 [-h] [-f] [-c] [-o OUTPUT] [name [name ...]]

Convert ascii file to hdf5

positional arguments:
  name                  ascii file(s) to convert

optional arguments:
  -h, --help            show this help message and exit
  -f, --force           overwrite if hdf5 file exists
  -c, --clobber         remove input ascii file
  -o OUTPUT, --output OUTPUT
                        output file name: if not set, uses inputfile name (with hdf5 extension)
