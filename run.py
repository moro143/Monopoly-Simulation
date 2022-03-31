from src.main import run
import argparse

parser = argparse.ArgumentParser(description='Monopoly Simulation.')
parser.add_argument('-r', 
                    action='store_true', 
                    help='Run monopoly simulation')

args = parser.parse_args()
if args.r:
    run()