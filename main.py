#!/usr/bin/env python3

import getch
import time
import sqlite3
from capra_data_types import Picture, Hike
from csv_to_sql import CSVtoSQL
from sql_controller import SQLController

modes = ('time', 'altitude', 'color')


def main():
    print('Starting SQLite3 program')
    mode_index = 0
    sql_controller = SQLController()
    current_picture = sql_controller.get_first_time_picture()
    # current_picture = sql_controller.get_greatest_altitude_picture()
    # current_picture = sql_controller.get_least_altitude_picture()

    while True:
        keycode = ord(getch.getch())
        if keycode == 61:       # Next
            print('NEXT in hike')
            if mode_index % 3 == 0:     # Time
                current_picture = sql_controller.next_time_picture_in_hike(current_picture)
            elif mode_index % 3 == 1:   # Altitude
                current_picture = sql_controller.next_altitude_picture_in_hike(current_picture)
            elif mode_index % 3 == 2:   # Color
                print('color')
            current_picture.print_obj()
        elif keycode == 45:     # Previous
            print('PREVIOUS in hike')
            if mode_index % 3 == 0:     # Time
                current_picture = sql_controller.previous_time_picture_in_hike(current_picture)
            elif mode_index % 3 == 1:   # Altitude
                current_picture = sql_controller.previous_altitude_picture_in_hike(current_picture)
            elif mode_index % 3 == 2:   # Color
                print('color')
            current_picture.print_obj()

        elif keycode == 67:     # Next across hikes
            print('NEXT across hikes')
            if mode_index % 3 == 0:     # Time
                current_picture = sql_controller.next_time_picture_across_hikes(current_picture)
            elif mode_index % 3 == 1:   # Altitude
                current_picture = sql_controller.next_altitude_picture_across_hikes(current_picture)
            elif mode_index % 3 == 2:   # Color
                print('color')
            else:
                raise Exception('Error on changing modes')
            current_picture.print_obj()

        elif keycode == 68:     # Previous across hikes
            print('PREVIOUS across hikes')
            if mode_index % 3 == 0:     # Time
                current_picture = sql_controller.previous_time_picture_across_hikes(current_picture)
            elif mode_index % 3 == 1:   # Altitude
                current_picture = \
                    sql_controller.previous_altitude_picture_across_hikes(current_picture)
            elif mode_index % 3 == 2:   # Color
                print('color')
            else:
                raise Exception('Error on changing modes')
            current_picture.print_obj()

        elif keycode == 109:    # Change mode
            mode_index += 1
            print('CHANGE MODE to: ' + modes[mode_index % 3])


def run_tests():
    sql_controller = SQLController()

    first = sql_controller.get_first_time_picture()
    first.print_obj()
    last = sql_controller.get_last_time_picture()
    last.print_obj()

    # biggest = sql_controller.get_greatest_altitude_picture()
    # biggest.print_obj()
    # least = sql_controller.get_least_altitude_picture()
    # least.print_obj()


if __name__ == "__main__":
    main()
