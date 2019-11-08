import os, sys

if 'SUMO_HOME' in os.environ:
     tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
     sys.path.append(tools)
     print("we have sumo")
else:
     sys.exit("please declare environment variable 'SUMO_HOME'")

 # import the library
sys.path.append('/home/jonny-smyth/Desktop/sumo/tools')
import traci
import sumolib
from sumolib import checkBinary
import traci.constants as tc


sumoBinary = "/usr/bin/sumo"
sumoConfig = ["-c", "network.sumocfg", "-S"]
sumoCmd = [sumoBinary, sumoConfig[0], sumoConfig[1], sumoConfig[2]]

# lets start with python interface.

def get_options():
    opt_parser = optparser.OptionParser()
    opt_parser.add_option("--nogui", action="store_true",
                            default=False, help="run the command verison of sumo")
    options, args = opt_parser.parse_args()
    return options
def run():
    while traci.sumulation.getMinExepectedNumber() > 0:



if __name__ == "__main__":
    options = get_options()
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    traci.start([sumoBinary, "-c", "network.sumocfg"])
    run()
