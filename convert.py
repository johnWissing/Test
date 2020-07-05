from nptdms import TdmsFile as td
import os
import sys

if len(sys.argv) > 3:
    print("too many arguments!")
    sys.exit()
elif len(sys.argv) < 3:
    if len(sys.argv) == 2:
        if sys.argv[1] == "-h":
            print("\nFormat #convert.py <TDMS file> <CSV file>\n")
            sys.exit()
    else:        
        """
        This is a comment
        """
        print("too few arguments")
    sys.exit()
else:

    TDMSfilename = sys.argv[1] 
    CSVfilename  = sys.argv[2]
    print("converting now TDMS file \"%s\" to CSV file :\"%s\"" %(TDMSfilename, CSVfilename))

    td(TDMSfilename).as_dataframe().to_csv(CSVfilename)
