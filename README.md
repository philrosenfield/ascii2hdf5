# ascii2hdf5
Command line tool to convert ascii table to hdf5

Output filename will have hdf5 extension instead of the original input file extension.

    $ ascii2hdf5 -h
    usage: ascii2hdf5 [-h] [-f] [-c] [-o OUTPUT] [name [name ...]]
    Convert ascii file to hdf5
    positional arguments:
      name                  ascii file(s) to convert
      optional arguments:
      -f, --force           overwrite if hdf5 file exists
      -c, --clobber         remove input ascii file
      -v, --verbose         verbose output

## Example:

    ascii2hdf5 datafile.dat
      will produce datafile.hdf5
