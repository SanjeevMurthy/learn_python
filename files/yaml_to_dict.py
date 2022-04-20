# from ruamel.yaml import YAML
# yaml = YAML()
import yaml

with open("config.yaml", 'r') as stream:
    try:
        parsed_yaml = yaml.safe_load(stream)
        print(parsed_yaml)
    except yaml.YAMLError as exc:
        print(exc)
