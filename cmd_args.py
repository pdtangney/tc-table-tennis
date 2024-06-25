""" Module to manage command line arguments."""
import argparse

from settings import Settings

parser = argparse.ArgumentParser(prog=Settings.game_name_alt,
                                 epilog="For more help visit "
                                 "rockytcgames.com/TableTennis")
parser.add_argument("-f", "--fullscreen",
                    help=f"Run {Settings.game_name} in fullscreen mode",
                    action="store_true")
parser.add_argument('-v', "--version", action="version",
                    version=Settings.version)
args = parser.parse_args()
