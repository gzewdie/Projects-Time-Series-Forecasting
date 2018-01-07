#!/usr/bin/env python
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
server.retrieve({
'stream'    : "oper",
    'levtype'   : "sfc",
    'param'     : "50.128/57.128/58.128/142.128/143.128",
    'dataset'   : "interim",
    'step'      : "0",
    'grid'      : "0.5/0.5",
    'time'      : "00/06/12/18",
    'date'      : "1987-01-01/to/2014-12-31",
    'type'      : "an",
    'class'     : "ei",
    'area'      : "36.5/-96.5/35.5/-95.5",
    'format'    : "netcdf",
    'target'    : "TestDownloadmyArea1987To2014G9.nc"})

