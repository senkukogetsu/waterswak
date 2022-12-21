import sys, getopt
#extend
from configobj import ConfigObj
#library
import codes.globalclasses as gc
from codes.const import *
import codes.app as app
import codes.cli_auto as cli
import codes.ut as ut
import codes.ui as ui


# for point_catchment
coordinate_1 = sys.argv[2]
coordinate_2 = sys.argv[3]
temp = "point_catchment", " ", str(coordinate_1), ",", str(coordinate_2)
coordinate = ''.join(temp)

if __name__ =='__main__':
    #init global classes   
    gc.SETTING  = ConfigObj("include/waterswak.ini")
    gc.UI = ui.UserInterface()
    gc.GAP = app.SApp()
    gc.CLI = cli.Cli()

    
    print("\n---------- set_basin ----------")
    gc.CLI.cli_cx.set_basin(basin_id = sys.argv[1])
    print("\n########## Success！ ##########")

    print("\n---------- output point_catchment ----------")
    try:
        gc.CLI.cli_cx.do_output(line = coordinate)
        print("\n########## Save to CSV Success！ ##########")
    except Exception as e:
        print("\n########## Error Message ##########\n ", e)
        print("\n########## Save to CSV Failed！ ##########")


        