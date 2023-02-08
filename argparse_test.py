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
import datetime

today = datetime.datetime.now()
now = today.strftime("%Y_%m_%d %H_%M_%S")

# define the path 
nc_file = "./hackathon_20211001_v0.4/hackathon/20230104_test/C1300QE-202107251400.nc/C1300QE-202107251400.nc"
# Method 1
# temp = nc_file.rsplit('/', 1)[-1]
# print(name)
# Method 2
temp = nc_file.rpartition('/')[-1]
flow_ID = temp.rpartition('.')[0]

def get_parser():
    parser = argparse.ArgumentParser(prog = "argparse_test.py",
                                     add_help = False,
                                     description = "Rewrite some functions of the waterswak system and can run automatically.",
                                     epilog = "END!")

    parser.add_argument('-h', '--help', action = 'help', default = argparse.SUPPRESS,
                        help = '----- Show help message about this system.')

    parser.add_argument('-b', '--set_basin',  metavar = ('basinID'), nargs = "?", #default = '1300', type = int,
                        help = "----- Please input BasinID, ex: 1300.")

    parser.add_argument('-m', '--stream', dest='stream', action='store_true', 
                        help = "----- Input this command and the system will output \"stream\" files.")

    parser.add_argument('-s', '--subbas', dest='subbas', action='store_true', 
                        help = "----- Input this command and the system will output \"subbas\" files.")

    parser.add_argument('-p', '--path', metavar = ('TWD97_1', 'TWD97_2'), nargs = 2, type = int,  # default = ['226930', '2686356'], 
                        help = "----- According to the BasinID entered by user, input two integer coordinates in TWD97 format for the ID, ex: 253520 2743364.")
    
    parser.add_argument('-n', '--name', default = now, 
                        help = "----- Decide the folder name when outputting files to a folder. ")

    parser.add_argument('--get_flow', nargs = '?', const = flow_ID,
                        # nargs = '?', const = flow_ID,
                        help = "----- Input the flow ID. ")

    # parser.add_argument('--time', action="store_true", dest="time",
    #                     help = "----- time_xy. ")
    parser.add_argument('--time_xy', metavar = ('t', 'x', 'y', 'o'), nargs = 4,
                        # default = ['27114180', '120.9339', '24.4961', '10'], type = float, metavar = ('t', 'x', 'y', 'o'), nargs = 4, 
                        help = "t x y o. ")

    # parser.add_argument('--his', action="store_true", dest="his",
    #                     help = "----- his_xy. ")
    parser.add_argument('--his_xy', metavar = ('x', 'y', 'o'), nargs = 3, 
                        help = " x y o. ")

    # parser.add_argument('--max', action="store_true", dest="max",
    #                     help = "----- max_offset. ")
    parser.add_argument('--max_offset', metavar = ('x', 'y', 'o'), nargs = 3, 
                        help = " x y o. ")

    return parser

def auto(args):
    #init global classes   
    gc.SETTING  = ConfigObj("include/waterswak.ini")
    gc.UI = ui.UserInterface()
    gc.GAP = app.SApp()
    gc.CLI = cli.Cli()
    
    if (args.set_basin != None):
        print("\n########## set_basin ##########")
        gc.CLI.cli_cx.set_basin(basin_id = str(args.set_basin))
        print("\n---------- Success！ ----------")

        # print(args.stream)
        if (args.stream):
            print("\n########## output stream ##########")
            gc.CLI.cli_cx.do_output(line = "stream")
            print("\n---------- Success！ ----------")
            
        if (args.subbas):
            print("\n########## output subbas ##########")
            gc.CLI.cli_cx.do_output(line = "subbas")
            print("\n---------- Success！ ----------")

        if (args.path != None):
            # for path
            if (args.path[0] < args.path[1]):
                min = args.path[0]
                max = args.path[1]
            temp = "path", " ", str(min), ",", str(max), ",", "name_a"
            path_name = ''.join(temp)

            print("\n########## output path ##########")
            gc.CLI.cli_cx.do_output(line = path_name)
            print("\n---------- Success！ ----------")

        print("The relevant output files are temporarily stored in the \"output\" folder. If the \"-n\", \"--name\" argument is used, it will be stored in a folder with the specified name. If not, it will be temporarily stored in a folder with the current date and time of execution.")
    # else:
    #     print("To use the \"output_stream\", \"output_subbas\", and \"path\" functions, please enter --set_basin and the basin_ID first!")
    
    if (args.get_flow):        
        # print("\n########## The default flow_id ##########")
        # print('flow_id:', args.get_flow)
        print("\n########## get_flow flow_id desc ##########")
        cmdline = str(args.get_flow) + ' desc'
        # print(cmdline)  
        gc.CLI.cli_tool.do_get_flow(line = cmdline)
        print("\n---------- Success！ ----------")

        if (args.time_xy != None):
            print("\n########## get_flow flow_id time_xy ##########")
            time_cmdline_temp = str(args.get_flow) , ' ','time_xy', ' ', str(args.time_xy[0]), ' ', str(args.time_xy[1]), ' ', str(args.time_xy[2]), ' ', str(args.time_xy[3])
            time_cmdline = ''.join(time_cmdline_temp)
            # print(args.time_xy) 
            # print(time_cmdline) 
            gc.CLI.cli_tool.do_get_flow(line = time_cmdline)
            print("\n---------- Success！ ----------")

        if (args.his_xy != None):
            print("\n########## get_flow flow_id his_xy ##########")
            his_cmdline_temp = str(args.get_flow) , ' ','his_xy', ' ', str(args.his_xy[0]), ' ', str(args.his_xy[1]), ' ', str(args.his_xy[2])
            his_cmdline = ''.join(his_cmdline_temp)
            # print(his_cmdline) 
            gc.CLI.cli_tool.do_get_flow(line = his_cmdline)
            print("\n---------- Success！ ----------")

        if (args.max_offset != None):
            print("\n########## get_flow flow_id max_offset ##########")
            max_cmdline_temp = str(args.get_flow) , ' ','max_offset', ' ', str(args.max_offset[0]), ' ', str(args.max_offset[1]), ' ', str(args.max_offset[2])
            max_cmdline = ''.join(max_cmdline_temp)
            gc.CLI.cli_tool.do_get_flow(line = max_cmdline)
            print("\n---------- Success！ ----------")    

    # else:
    #     print("To use the \"time_xy\", \"his_xy\", and \"max_offset\" functions, please enter --get_flow and the flow_ID first!")

if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    auto(args)



        