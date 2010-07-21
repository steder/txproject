"""scripts.py

Defines option parsers for all the commandline scripts in txProject

"""


from optparse import OptionParser


def getDirprinterOptionsParser(usage):
    parser = OptionParser(usage)
    return parser


def getTxprojectOptionsParser(usage):
    parser = OptionParser(usage)
    return parser
