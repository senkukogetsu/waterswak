import sys
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
temp = "point_catchment_csv", " ", '"' + name + '"'
file = ''.join(temp)

# for point_catchment
# coordinate_1 = 200998.5
# coordinate_2 = 2632927.8
coordinate_1 = sys.argv[2]
coordinate_2 = sys.argv[3]
temp = "point_catchment", " ", str(coordinate_1), ",", str(coordinate_2)
coordinate = ''.join(temp)
# print(coordinate)

# for path
temp = "path", " ", str(coordinate_1), ",", str(coordinate_2), ",", "name_a"
path_name = ''.join(temp)

#Spec: program init, mode selection, start
#How/NeedToKnow:
if __name__ =='__main__':
    #init global classes   
    gc.SETTING  = ConfigObj("include/waterswak.ini")
    gc.UI = ui.UserInterface()
    gc.GAP = app.SApp()
    gc.CLI = cli.Cli()

    print("\n---------- set_basin ----------")
    gc.CLI.cli_cx.set_basin(basin_id = sys.argv[1])
    print("\n########## Success！ ##########")

    print("\n---------- desc ----------")
    gc.CLI.cli_cx.do_desc(line = "")
    print("\n########## Success！ ##########")

    # print("\n---------- output stream ----------")
    # gc.CLI.cli_cx.do_output(line = "stream")
    # print("\n########## Success！ ##########")

    # print("\n---------- output subbas ----------")
    # gc.CLI.cli_cx.do_output(line = "subbas")
    # print("\n########## Success！ ##########")

    # print("\n---------- output point_catchment_csv ----------")
    # try:
    #     gc.CLI.cli_cx.do_output(line = file)
    #     print("\n########## Save to CSV Success！ ##########")
    # except Exception as e:
    #     print("\n########## Error Message ##########\n ", e)
    #     print("\n########## Save to CSV Failed！ ##########")

    print("\n---------- output point_catchment ----------")
    try:
        gc.CLI.cli_cx.do_output(line = coordinate)
        print("\n########## Save to CSV Success！ ##########")
    except Exception as e:
        print("\n########## Error Message ##########\n ", e)
        print("\n########## Save to CSV Failed！ ##########")

    # print("\n---------- output path ----------")
    # gc.CLI.cli_cx.do_output(line = path_name)
    # print("\n########## Success！ ##########")

    # print("\n---------- output nx_write_shp ----------")
    # gc.CLI.cli_cx.do_output(line = "nx_write_shp")
    # print("\n########## Success！ ##########")

    # print("\n---------- output pathline_interpolate 10 ----------")
    # gc.CLI.cli_cx.do_output(line = "pathline_interpolate 10")
    # print("\n########## Success！ ##########")
    
    
        
    


