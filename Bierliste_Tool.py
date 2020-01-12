#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import os
import tkinter as tk
from configparser import ConfigParser
import logger as logging


# todo gui
# todo import excel file
# todo export excel file (load example file)
# todo read settings file
# todo
#

NAME_SETTINGS_FILE = "settings.ini"


def handle_excep(exception, with_tb=True):
    """ prints exception """
    logging.Logger.static_critical(exception)
    if with_tb:
        import traceback
        logging.Logger.static_critical(traceback.format_exc())


class BierListeTool:

    def __init__(self):

        self.logger = logging.Logger(level='DEBUG')

        self.prices = SettingsGroup()
        self.prices.beer = None
        self.prices.radler = None
        self.prices.mate = None
        self.prices.pali = None
        self.prices.spezi = None
        self.read_settings_file(NAME_SETTINGS_FILE)

        self.gui = BierlisteToolGUI()

    def read_settings_file(self, settings_file):
        """
        Reads price list from settings .ini file
        :param settings_file: String, Name of settings file, type .ini
        :return: None
        """

        if not os.path.isfile(settings_file):
            raise FileNotFoundError("CRITICAL: Settings file not found: " + str(settings_file))

        self.logger.debug("Reading settings file:")

        # init configparser and get information
        config = ConfigParser()
        config.read(settings_file)

        try:
            # prices
            self.prices.beer = float(config.get('Preise', 'Bier'))
            self.prices.radler = float(config.get('Preise', 'Radler'))
            self.prices.mate = float(config.get('Preise', 'Mate'))
            self.prices.pali = float(config.get('Preise', 'Pali'))
            self.prices.spezi = float(config.get('Preise', 'Spezi'))

            self.logger.info("Successfully imported pricelist!")
            self.logger.debug("Preise | Bier: {}, Radler: {}, Mate: {}, Pali: {}, Spezi: {}".format(self.prices.beer, self.prices.radler, self.prices.mate, self.prices.pali, self.prices.spezi))
        except Exception as e:
            self.logger.error("Could not read Settings file!")
            handle_excep(e, with_tb=True)


class BierlisteToolGUI:

    def __init__(self):
        self.logger = logging.Logger()
        self.logger.debug("Building GUI:")



        # gui here
        self.logger.info("Sucesfully builded GUI")
        tk.mainloop()


class Person:
    """ Represents one person, holding all corresponding information """

    def __init__(self, name, room='', other='', balance=0, beers=0, radler=0, mate=0, pali=0, spezi=0):
        """

        :param name: String, name
        :param room: String, roomnumber
        :param other: String, additional data for example 'extern' or 'Untermieter/UM'
        :param balance: Float, money account
        :param beers: Integer, number of beers
        :param radler: Integer, number of radler
        :param mate: Integer, number of mate
        :param pali: Integer, number of pali
        :param spezi: Integer, number of spezi
        """
        self.name = name
        self.room = room
        self.other = other
        self.balance = balance
        self.beers = beers
        self.radler = radler
        self.mate = mate
        self.pali = pali
        self.spezi = spezi
        self.logger = logging.Logger()

    @staticmethod
    def new_person(name, room, other='', balance=0, beers=0, radler=0, mate=0, pali=0, spezi=0):
        """
        Creates new instance of person
        :param name: String, name
        :param room: String, roomnumber
        :param other: String, additional data for example 'extern' or 'Untermieter/UM'
        :param balance: Float, money account
        :param beers: Integer, number of beers
        :param radler: Integer, number of radler
        :param mate: Integer, number of mate
        :param pali: Integer, number of pali
        :param spezi: Integer, number of spezi
        """
        return Person(name, room=room, other=other, balance=balance, beers=beers, radler=radler, mate=mate, pali=pali, spezi=spezi)

    def add_drinks(self, beers, radler, mate, pali, spezi):
        """ Adds drinks to person """
        self.beers += beers
        self.radler += radler
        self.mate += mate
        self.pali += pali
        self.spezi += spezi
        self.logger.info("{} | Added {} Bier, {} Radler {} Mate, {} Pali, {} Spezi".format(self.name, beers, radler, mate, pali, spezi))

    def add_money(self, amount):
        """ adds money to balance of user """
        self.balance += amount
        self.logger.info("{} | Added {} Euro to new amount of {}".format(self.name, amount, self.balance))

    def __str__(self):
        return "Person | Name: {}, Room: {}, other: {}, balance: {}, Bier: {}, Radler: {}, Mate: {}, Pali: {}, Spezi: {}".format(self.name, self.room, self.other, self.balance, self.beers, self.radler, self.mate, self.pali, self.spezi)

    def __repr__(self):
        return '\n' + self.__str__() + '\n'


class SettingsGroup:
    """ Some Dummy class for grouping settings """

    def __str__(self):
        str_eq = ''
        for elem in self.__dict__:
            str_eq = str_eq + elem + ': ' + str(self.__dict__[elem]) + '\n'
        return str_eq

    def __repr__(self):
        return '\n' + str(self.__str__()) + '\n'


if __name__ == '__main__':
    print("Starting tool ....")
    tool = BierListeTool()
    print("\t ... Done")
