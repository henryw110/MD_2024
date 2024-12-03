import yaml
from yaml import Loader
import sys
stream=open("dump.yaml","r")
stream=stream.read()
y=yaml.load(stream,Loader=Loader)
print(str(y['thermo'][1]['data'][2]))