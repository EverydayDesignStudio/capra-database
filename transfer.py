#!/usr/bin/env python3

# Transfers data from one computer to another over SSSH using SCP command

import os

DB_PROJECTOR = '/Users/Jordan/Developer/eds/capra-database/capra-projector.db'
DB_CAMERA = '/Users/Jordan/Developer/eds/capra-database/capra-camera.db'


def main():
    print('Starting transfer script...')

    os.system("scp foo.txt pi@192.168.0.111:/home/pi/foo.txt")
    # e.g. os.system("scp foo.bar joe@srvr.net:/path/to/foo.bar")

    print('...ending transfer script')

if __name__ == "__main__":
    main()
