import firebase_admin
from pyinjector import inject
from firebase_admin import credentials
from firebase_admin import db
from os import system

VERSION = "1.0"

cred = credentials.Certificate('abobaclient-204b2-firebase-adminsdk-zn3ec-1855bbdccf.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://abobaclient-204b2-default-rtdb.firebaseio.com/'})
ref2 = db.reference('/').get()


def zalupa_txt():
    print(""" _______ ______   _____  ______  _______ _______        _____ _______ __   _ _______
 |_____| |_____] |     | |_____] |_____| |       |        |   |______ | \  |    |   
 |     | |_____] |_____| |_____] |     | |_____  |_____ __|__ |______ |  \_|    |   
                                                                                    """)


def getpid(proc):
    import os
    return [item.split()[1] for item in os.popen('tasklist').read().splitlines()[4:] if proc in item.split()]


def check_version():
    if VERSION != ref2['VER']:
        print(f'Your version is outdate\nYour: {VERSION}\nLatest:{ref2["VER"]}')
        with open('version.txt', 'wt', encoding='UTF8') as f:
            f.write(f"Download latest version: \n {ref2['link']}")
        system('version.txt')
        exit(-1)


if __name__ == "__main__":
    zalupa_txt()
    check_version()
    inject(int(getpid('javaw.exe')[0]), "GishCode-1.12.2-v0.5.0.dll") # enter the name of the process and the dll you want to inject
