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

#Spec: program init, mode selection, start
#How/NeedToKnow:
if __name__ =='__main__':
    #init global classes   
    gc.SETTING  = ConfigObj("include/waterswak.ini")
    gc.UI = ui.UserInterface()
    gc.GAP = app.SApp()
    # gc.CLI = cli.Cli()
    # gc.CLI.cmdloop()

    cli.Cli().cli_cx.do_set_basin(line=sys.argv[1])
    print("------------------------------------------")
    cli.Cli().cli_cx.do_set_basin(line=sys.argv[2])
    # cli.Cli().cli_cx.do_output(line="stream")
    # print("success")


    # parser = argparse.ArgumentParser()
    # parser.add_argument('basin_id')
    # args = parser.parse_args(sys.argv[1:])
    # print(sys.argv[1:])
    # if (sys.argv[1] == "catchment"):
        # cli.Cli().do_catchment("catchment")
    # print(cli.Cli().cli_cx.basin_id)
    # cli.CliCx(stdout).set_basin(basin_id=sys.argv[1])
    # print(cli.Cli().cli_cx.basin_id)
    
        
    


