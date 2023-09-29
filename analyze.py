# Example of a command line 
# import auto "c:/Users/lasse/Dropbox/Backgammon/Matches/Galaxy matches/raw/match972338.txt"

# Examples of using this scripts
# Run the following from gnu-cli command line prompt
# > from analyze import *                                              # Note: GNUBG should be restarted to load any changes 
# > files = get_files('c:/Users/LMDN\OneDrive - Novo Nordisk/R-Projects/backgammon/data-raw/galaxy-matches/raw/')
# > analyze_files(files, out_dir = 'c:/Users/LMDN\OneDrive - Novo Nordisk/R-Projects/backgammon/data-raw/galaxy-matches/analyzed/3-ply/', ply = 3)

import gnubg
import os
import glob

def get_files(path="c:\\Users\\lasse\\R-projects\\backgammon\\data-raw\\galaxy-matches\\raw\\", extension="txt"):
    search_pattern = os.path.join(path, f"*.{extension}")
    files = glob.glob(search_pattern)
    return files

def maybe_swap_players():
    match_info = gnubg.match()['match-info']
    o_player_name = match_info['O']['name']
    if o_player_name != 'lasse':
        gnubg.command('swap players')

def analyze_files(files, out_dir = "c:\\Users\\lasse\\R-projects\\backgammon\\data-raw\\galaxy-matches\\analyzed\\", ply=3, sgf=False):
    # Make sure the directory exists, and if not, create it
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        
    # Parameters for analysis
    gnubg.command('set analysis cube on')
    gnubg.command('set analysis moves on')
    gnubg.command('set analysis luck off')
    
    gnubg.command('set analysis chequerplay type evaluation')
    gnubg.command('set analysis chequerplay evaluation prune on')
    gnubg.command('set analysis chequerplay evaluation cubeful on')
    gnubg.command(f'set analysis chequerplay evaluation plies {ply}')

    gnubg.command('set analysis cubedecision type evaluation')
    gnubg.command('set analysis cubedecision evaluation prune on')
    gnubg.command('set analysis cubedecision evaluation cubeful on')
    gnubg.command(f'set analysis cubedecision evaluation plies {ply}')
    
    for file in files:
        # Create the name for the new .sgf and .txt files based on the original filename
        file_name = os.path.basename(file)  # Extract just the filename without path
        sgf_file = os.path.join(out_dir, file_name[:-4] + ".sgf")
        txt_file = os.path.join(out_dir, file_name[:-4] + ".txt")
        
        # Check if the file has already been analyzed
        if os.path.exists(txt_file):
            continue

        # Import and analyze the text match file
        gnubg.command(f'import auto "{file}"')
        maybe_swap_players()
        gnubg.command('analyze match')

        # Export the match to .sgf and .txt format
        if sgf:
            gnubg.command(f'save match "{sgf_file}"')
        gnubg.command(f'export match text "{txt_file}"')
