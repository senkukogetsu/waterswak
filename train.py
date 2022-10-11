import waterswak

import getopt
import sys
import unittest
import argparse

#extend
from configobj import ConfigObj

#library
import codes.globalclasses as gc
from codes.const import *
import codes.app as app
import codes.cli as cli
import codes.ut as ut
import codes.ui as ui

# for point_catchment_csv filename 
name = "data/喝好水 吃好物 有良居-公民協力 - 點位集水區.csv"
temp = "point_catchment_csv"," ",'"'+name+'"'
file = ''.join(temp)

# for point_catchment
coordinate_1 = 200998.5
coordinate_2 = 2632927.8
temp = "point_catchment"," ",str(coordinate_1),",",str(coordinate_2)
coordinate = ''.join(temp)
# print(coordinate)

# for path
temp = "path"," ",str(coordinate_1),",",str(coordinate_2),",", "name_a"
path_name = ''.join(temp)

#Spec: program init, mode selection, start
#How/NeedToKnow:
if __name__ =='__main__':
    #init global classes   
    gc.SETTING  = ConfigObj("include/waterswak.ini")
    gc.UI = ui.UserInterface()
    gc.GAP = app.SApp()
    # gc.CLI = cli.Cli()
    # gc.CLI.cmdloop()

    gc.CLI = cli.Cli()
    print("---------- set_basin ----------")
    gc.CLI.cli_cx.set_basin(basin_id=sys.argv[1])
    print("---------- desc ----------")
    gc.CLI.cli_cx.do_desc(line="")
    print("---------- output stream ----------")
    gc.CLI.cli_cx.do_output(line="stream")
    print("---------- output subbas ----------")
    gc.CLI.cli_cx.do_output(line="subbas")
    print("---------- output point_catchment_csv ----------")
    # gc.CLI.cli_cx.do_output(line=file)
    print("---------- output point_catchment ----------")
    gc.CLI.cli_cx.do_output(line=coordinate)
    print("---------- output path ----------")
    gc.CLI.cli_cx.do_output(line=path_name)
    print("---------- output nx_write_shp ----------")
    gc.CLI.cli_cx.do_output(line="nx_write_shp")
    print("---------- output pathline_interpolate 10 ----------")
    gc.CLI.cli_cx.do_output(line="pathline_interpolate 10")
    
    
        
    


