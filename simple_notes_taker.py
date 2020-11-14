#!/usr/bin/python3

import mysql.connector


class NotesTaker:
    def __init__(self, username: str, password: str, hostname: str):
        self.__notesDB = mysql.connector.connect(
            user=username,
            password=password,
            host=hostname
        )
        self.__dbCursor = self.__notesDB.cursor()
        self.__connectToDB()

    def __del__(self):
        self.__notesDB.close()

    def listNotes(self):
        self.__dbCursor.execute("SELECT * FROM `NotesData`;")
        for n in self.__dbCursor:
            print(n)

    def getNote(self, title: str):
        self.__dbCursor.execute("SELECT * FROM `NotesData` WHERE `Title`=\"" + title + "\";")
        for n in self.__dbCursor:
            print(n)

    def addNote(self, title: str, content: str):
        self.__dbCursor.execute("INSERT INTO `NotesData` (`Date`, `Title`, `Content`)\
                                VALUES (CURRENT_DATE (), %s, %s)", (title, content))
        self.__notesDB.commit()

    def __connectToDB(self):
        try:
            self.__dbCursor.execute("USE Notes;")
        except mysql.connector.errors.ProgrammingError:
            self.__dbCursor.execute("CREATE DATABASE Notes;")
            self.__dbCursor.execute(
                "CREATE TABLE `Notes`.`NotesData` (\
                Date DATE, Title VARCHAR(45),\
                Content VARCHAR(2000) );"
            )
            self.__dbCursor.execute("USE Notes")


if __name__ == "__main__":
    note = NotesTaker("hmm", "hmm", "hmm")
    note.addNote("Blyat", "The Sky is High AF")
    note.listNotes()

    del note
