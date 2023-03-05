import sys
import yaml
import os

def readConfigFile(filepath):
    try:
        with open(filepath, "r") as file:
            config = yaml.load(file, yaml.FullLoader)
            print(config)
            return config
    except FileNotFoundError:
        print(f"{os.path.expandvars(filepath)} not found")

if __name__=="__main__":
    readConfigFile(sys.argv[1])