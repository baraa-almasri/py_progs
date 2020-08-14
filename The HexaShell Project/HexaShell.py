#!/usr/bin/python
import json
import os

class HexaShell:

    # constructor: initalize the shell
    def __init__(self):
        # create vars
        self.__settingsJSON = None
        self.__settings = None
        self.__username = None
        self.__hostname = None
        self.__directory = "None"
        # initialize shell
        self.__initShell()
        # aliases dictionary
        self.__aliases = self.__settings["aliases"]

    def prompt(self):
        while True:
            self.__printPrompt()
            command = input()

            try:
                os.system(self.__aliases[command])
                continue

            except KeyError:
                os.system(command)

    def __initShell(self):
        
        # load settings from file
        self.__openSettingFile()
        self.__username = os.getenv("USER")
        self.__hostname = os.getenv("HOSTNAME")
        self.__setDirectory()
        


    def __printPrompt(self):
        self.__setDirectory()
        print("[%s @ %s]{%s}:$ " % (self.__username, self.__hostname, self.__directory)  , end = "" )
        

    def __openSettingFile(self):
    
        self.__settingsJSON = open("settings.json", "r")
        self.__settings = json.load(self.__settingsJSON)


    def __setDirectory(self):
        self.__directory = os.getcwd()
        if ( "/home/" + self.__username ) in self.__directory:
            self.__directory = self.__directory.replace("/home/" + self.__username, "~")
            

    def __printHelp(self):
        # disclaimer
        print("The HexaShell Project:")
        print("This is a pre-release")
        print("Not much working nor functional")
        input("press enter to continue....")
