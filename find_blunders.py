# NOTES
# -----

# To run functions in a script from the GNUBG command line, I did:
# gnubg-cli                                                                  # Starts the command line version of GNUBG
# set player 1 gnu                                                           # Lets gnu make moves for player
# > from matchseries import playMatchSeries                                  # Imports the playMatchSeries function (> calls python)
# > playMatchSeries(matchLength=1, noOfMatches=2, statsFile="my_stats.txt")  # Runs playMatchSeries
# The my_stats.txt file ended up in: c:\Users\LMDN\AppData\Local\gnubg\      # Where gnubg is installed


# For this script:

# > sys.path.append('c:\\Users\\LMDN\\gnubg\\scripts')                       # Note: GNUBG should be restarted to load any changes  
# > from find_blunders import *

import gnubg

def get_files():
    files = ['scripts\match1484923.txt', 'scripts\match1486073.txt']
    return files

def convert_files(files):
    file = files[1] # Replace with loop
    gnubg.command('import auto ' + file)
    file = file[:-3] + "sgf"
    gnubg.command('save match "' + file)



