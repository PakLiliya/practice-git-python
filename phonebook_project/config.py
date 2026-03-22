from configparser import ConfigParser
import os

def load_config(filename='database.ini', section='postgresql'):
    print("Current dir:", os.getcwd())
    parser = ConfigParser()
    parser.read(filename)
    print("Files read:", parser.sections())
    config = {}
    if parser.has_section(section):
        for param in parser.items(section):
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found')
    return config

if __name__ == '__main__':
    config = load_config()
    print(config)