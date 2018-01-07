# This simple code helps to extract weather and land surface parameters from ECMWF global data, https://www.ecmwf.int/,
#https://www.ecmwf.int/en/forecasts/datasets/browse-reanalysis-datasets
#!/usr/bin/env python

# Import ECMWFDataServer
from ecmwfapi import ECMWFDataServer
server = ECMWFDataServer()
# Set your parameters and  type od experiment,  selection eare etc, See the read me file for details!

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
    'area'      : "32.8/-97/32.8/-97",
    'format'    : "netcdf",
    'target'    : "DownloadsParam1.nc"})

   # area is the  an example of a place near dallas, you can also use "United Sates",  "Europe" to download over a large area.
   # see http://apps.ecmwf.int/datasets/data/interim-full-daily/levtype=sfc/ for interactive uasage to select parameters.
