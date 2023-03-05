import sys
import yaml

# def readConfigFile(filepath):
    # configs = {
    #     "watch":[],
    #     "ignore":[],
    #     "type": {}
    # }
    # with open(filepath, "r") as config:
    #     for line in config:
    #         if (line.startswith("+")):
    #             configs["watch"].append(line.removeprefix("+").removesuffix("\n").strip())
    #         elif (line.startswith("-")):
    #             configs["ignore"].append(line.removeprefix("-").removesuffix("\n").strip())
    #         elif (line.startswith("$")):
    #             configs["type"].append()
                
    #         else:
    #             pass
    # return configs

def readConfigFile(filepath):
    with open(filepath, "r") as file:
        config = yaml.load(file, yaml.FullLoader)
        print(config)
        return config

if __name__=="__main__":
    readConfigFile(sys.argv[1])