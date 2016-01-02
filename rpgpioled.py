# Raspberry Pi GPIO - LED (Simulator)
# Patrick Gillen
# Copyright 2016

# Raspberry Pi General Purpose Input Output (GPIO) header pins
#
# Board Number  BCM Name    Internal
# ------------  --------    --------
# 7             BCM4        0
# 11            BCM17       1
# 12            BCM18       2
# 13            BCM27       3
# 15            BCM22       4
# 16            BCM23       5
# 18            BCM24       6
# 22            BCM25       7

from tkinter import *
from time import sleep

BOARD = 0
BCM = 1

IN = 0
OUT = 1

LOW = 0
HIGH = 1

class rpgpioled:

    _Board_Number = { 7 : 0, 11 : 1, 12 : 2, 13 : 3, 15 : 4, 16 : 5, 18 : 6, 22 : 7 }
    _BCM_Name = {4 : 0, 17 : 1, 18 : 2, 27 : 3, 22 : 4, 23 : 5, 24 : 6, 25 : 7 }

    def __init__(self):
        
        self._root = Tk()
        self._root.title("Raspberry Pi GPIO - LED (Simulator)")

        self._canvas = Canvas(self._root, width=475, height=200)
        self._canvas.pack()

        self._canvas.create_rectangle(10, 10, 465, 190)

        self._leds = []
        for i in range(0, 8):
            self._leds.append(self._canvas.create_rectangle(50 + i * 50, 20, 75 + i * 50, 180, fill = 'black'))

        self._leds_direction = [None] * 8
        self._leds_state = [None] * 8

    def setmode(self, mode):
        if mode == BOARD:
            self._mode = BOARD
        elif mode == BCM:
            self._mode = BCM
        else:
            raise RuntimeError('mode must be BOARD or BCM')

    def getmode(self):
        if self._mode == BOARD:
            return('BOARD')
        elif self._mode == BCM:
            return('BCM')
        else:
            raise RuntimeError('something unexpected happened: 201601021706')
        return self._mode

    def setup(self, channel, direction):
        if direction == IN:
            raise RuntimeError('direction IN has not been implemented yet')
        elif direction == OUT:
            if self._mode == BOARD:
                if channel in self._Board_Number.keys():
                    self._leds_direction[self._Board_Number[channel]] = OUT
                else:
                    raise RuntimError('BOARD channel unavailable')
            elif self._mode == BCM:
                if channel in self._BCM_Name.keys():
                    self._leds_direction[self._BCM_Name[channel]] = OUT
                else:
                    raise RuntimeError('BCM channel unavailable')
            else:
                raise RuntimeError('something unexpected happened: 201601011839')
        else:
            raise RuntimeError('direction must be IN or OUT')

    def output(self, channel, state):
        if state not in [LOW, HIGH]:
            raise RuntimeError('state must be LOW or HIGH')
        else:
            if self._mode == BOARD:
                if channel in self._Board_Number.keys():
                    self._leds_state[self._Board_Number[channel]] = state
                else:
                    raise RuntimeError('BOARD channel unavailable')
            elif self._mode == BCM:
                if channel in self._BCM_Name.keys():
                    self._leds_state[self._BCM_Name[channel]] = state
                else:
                    raise RuntimeError('BCM channel unavailable')
            else:
                raise RuntimeError('something unexpected happened: 201601021713')
        self._update()

    def _update(self):
        for i in range(0, 8):
            if self._leds_direction[i] == OUT:
                if self._leds_state[i] == LOW:
                    self._canvas.itemconfigure(self._leds[i], fill = 'black')
                elif self._leds_state[i] == HIGH:
                    self._canvas.itemconfigure(self._leds[i], fill = 'red')
                else:
                    pass # if the state has not been set then take no action
            self._root.update_idletasks()
        self._root.update()
