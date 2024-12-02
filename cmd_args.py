""" Module to manage command line arguments."""
import argparse

from settings import Settings

parser = argparse.ArgumentParser(prog=Settings.game_name_alt,
                                 epilog="For more help visit "
                                 "https://github.com/pdtangney/tc-table-tennis")
parser.add_argument("-f", "--fullscreen",
                    help=f"Run {Settings.game_name} in fullscreen mode",
                    action="store_true")
parser.add_argument("-v", "--version", action="version",
                    version=Settings.version)
parser.add_argument("-d", "--debug", action="store_true",
                    help="Show extra debugging info, including version number,"
                    " codename, and build date.")
args = parser.parse_args()
