#!/usr/bin/python
import json
import os

class HexaShell:

    # constructor: initalize the shell
    def __init__(self):
        self.__settingsJSON = None
        self.__settings = None

        self.__openSettingFile()# __openSettingsFile()
        self.__aliases = self.__settings["aliases"]

    def prompt(self):
        while True:
            print("the Hexa Shell:")
            command = input(">> ")

            try:
                os.system(self.__aliases[command])
                continue

            except KeyError:
                os.system(command)

    def __openSettingFile(self):
    
        self.__settingsJSON = open("settings.json", "r")
        self.__settings = json.load(self.__settingsJSON)
        
