import argparse, sys
#extend
from configobj import ConfigObj
#library
import codes.globalclasses as gc
from codes.const import *
import codes.app as app
import codes.cli_auto as cli
import codes.ut as ut
import codes.ui as ui

def get_parser():
    parser = argparse.ArgumentParser(prog = "argparse_test.py",
                                     add_help = False,
                                     description = "Rewrite some functions of the waterswak system and can run automatically.",
                                     epilog = "END!")
    parser.add_argument('-h', '--help', action = 'help', default = argparse.SUPPRESS,
                        help = '----- Show help message about this system.')

    parser.add_argument('-b', '--basinID', default = '1420', type = int, 
                        help = "----- Please input BasinID, ex: 1300.")

    parser.add_argument('-m', '--stream', dest='stream', action='store_true', 
                        help = "----- Input this command and the system will output \"stream\" files.")

    parser.add_argument('-s', '--subbas', dest='subbas', action='store_true', 
                        help = "----- Input this command and the system will output \"subbas\" files.")

    parser.add_argument('-p', '--path', default = ['226930', '2686356'], metavar = ('TWD97_1', 'TWD97_2'), nargs = 2, type = int, 
                        help = "----- According to the BasinID entered by user, input two integer coordinates in TWD97 format for the ID, ex: 253520 2743364.")
    return parser

def auto(args):
    #init global classes   
    gc.SETTING  = ConfigObj("include/waterswak.ini")
    gc.UI = ui.UserInterface()
    gc.GAP = app.SApp()
    gc.CLI = cli.Cli()
    
    print("\n########## set_basin ##########")
    gc.CLI.cli_cx.set_basin(basin_id = str(args.basinID))
    print("\n---------- Success！ ----------")

    # print(args.stream)
    if (args.stream):
        print("\n########## output stream ##########")
        gc.CLI.cli_cx.do_output(line = "stream")
        print("\n---------- Success！ ----------")
        
    if (args.subbas):
        print("\n########## output stream ##########")
        gc.CLI.cli_cx.do_output(line = "subbas")
        print("\n---------- Success！ ----------")

    # for path
    if (args.path[0] < args.path[1]):
        min = args.path[0]
        max = args.path[1]
    temp = "path", " ", str(min), ",", str(max), ",", "name_a"
    path_name = ''.join(temp)

    print("\n########## output path ##########")
    gc.CLI.cli_cx.do_output(line = path_name)
    print("\n---------- Success！ ----------")


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    auto(args)



        