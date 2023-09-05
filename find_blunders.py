# NOTES
# -----

# To run functions in a script from the GNUBG command line, I did:
# gnubg-cli                                                                  # Starts the command line version of GNUBG
# set player 1 gnu                                                           # Lets gnu make moves for player
# > from matchseries import playMatchSeries                                  # Imports the playMatchSeries function (> calls python)
# > playMatchSeries(matchLength=1, noOfMatches=2, statsFile="my_stats.txt")  # Runs playMatchSeries
# The my_stats.txt file ended up in: c:\Users\LMDN\AppData\Local\gnubg\      # Where gnubg is installed


# For this script:
# > from find_blunders import *                                              # Note: GNUBG should be restarted to load any changes 

import gnubg
import os
import glob

def get_files(path="c:\\Users\\LMDN\\AppData\\Local\\gnubg\\scripts\\matches", extension="txt"):
    search_pattern = os.path.join(path, f"*.{extension}")
    files = glob.glob(search_pattern)
    return files

def analyze_files(files, out_dir = "c:\\Users\\LMDN\\AppData\\Local\\gnubg\\scripts\\output", ply=3):
    # Make sure the directory exists, and if not, create it
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        
    # Parameters for analysis
    gnubg.command('set analysis cube on')
    gnubg.command('set analysis moves on')
    gnubg.command('set analysis chequerplay type evaluation')
    gnubg.command('set analysis chequerplay evaluation prune on')
    gnubg.command('set analysis chequerplay evaluation cubeful on')
    gnubg.command(f'set analysis chequerplay evaluation plies {ply}')
    
    for file in files:
        # Import the text match file
        gnubg.command(f'import auto {file}')

        # Analyze match
        gnubg.command('analyze match')
        
        # Create the name for the new .sgf and .txt files based on the original filename
        file_name = os.path.basename(file)  # Extract just the filename without path
        sgf_file = os.path.join(out_dir, file_name[:-4] + "_analyzed.sgf")
        txt_file = os.path.join(out_dir, file_name[:-4] + "_analyzed.txt")

        # Export the match to .sgf and .txt format
        gnubg.command(f'save match "{sgf_file}"')
        gnubg.command(f'export match text "{txt_file}"')
