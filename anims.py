import sys
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import *
from pynput.keyboard import Key, KeyCode, Listener
from pynput import keyboard
import time
from PyQt5.QtGui import QPixmap

# rotation_rasial = ['e','r','w','alt + q','w', 'e', 'alt+x','g','s','a','d','s']
rotation_rasial = [
    frozenset([KeyCode(vk=69)]),
    frozenset([KeyCode(vk=82)]),
    frozenset([KeyCode(vk=87)]),
    frozenset([Key.alt_l, KeyCode(vk=81)]),
    frozenset([KeyCode(vk=87)]),
    frozenset([KeyCode(vk=69)]),
    frozenset([Key.alt_l, KeyCode(vk=88)]),
    frozenset([KeyCode(vk=71)]),
    frozenset([KeyCode(vk=83)]),
    frozenset([KeyCode(vk=65)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=83)]),
]

# rotation_rasial_p13 = ['alt+s','alt + a','a','g','alt+g','shift+c','alt+w','s','f','d','d','a','g','alt e','e','s','f','d','f','d','a','s']
rotation_rasial = [
    frozenset([KeyCode(vk=69)]),
    frozenset([KeyCode(vk=82)]),
    frozenset([KeyCode(vk=87)]),
    frozenset([KeyCode(vk=87)]),
    frozenset([Key.alt_l, KeyCode(vk=81)]),
    frozenset([KeyCode(vk=69)]),
    frozenset([Key.alt_l, KeyCode(vk=88)]),
    frozenset([KeyCode(vk=71)]),
    frozenset([KeyCode(vk=83)]),
    frozenset([KeyCode(vk=65)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=83)]),
    frozenset([Key.alt_l, KeyCode(vk=83)]),
    frozenset([Key.alt_l, KeyCode(vk=65)]),  # Adrenaline
    frozenset([KeyCode(vk=65)]),
    frozenset([KeyCode(vk=71)]),
    frozenset([Key.alt_l, KeyCode(vk=71)]),  # bloat
    frozenset([Key.alt_l, KeyCode(vk=87)]),
    frozenset([KeyCode(vk=83)]),
    frozenset([KeyCode(vk=70)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=65)]),
    frozenset([KeyCode(vk=71)]),
    frozenset([Key.alt_l, KeyCode(vk=69)]),
    frozenset([KeyCode(vk=69)]),
    frozenset([KeyCode(vk=83)]),
    frozenset([KeyCode(vk=70)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=70)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=65)]),
    frozenset([KeyCode(vk=83)]),
    frozenset([KeyCode(vk=71)]),
    frozenset([Key.shift_l, KeyCode(vk=68)]),  # limitless
    frozenset([Key.shift_l, KeyCode(vk=72)]),
    frozenset([KeyCode(vk=83)]),
    frozenset([KeyCode(vk=81)]),
    frozenset([KeyCode(vk=70)]),
    frozenset([KeyCode(vk=88)]),
]

rotation_rasial2 = [
    frozenset([KeyCode(vk=69)]),
    frozenset([KeyCode(vk=87)]),
    frozenset([KeyCode(vk=82)]),
    frozenset([KeyCode(vk=87)]),
    frozenset([Key.shift_l, KeyCode(vk=67)]),
    frozenset([KeyCode(vk=69)]),
    frozenset([Key.alt_l, KeyCode(vk=88)]),
    frozenset([KeyCode(vk=71)]),
    frozenset([KeyCode(vk=83)]),
    frozenset([KeyCode(vk=65)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=83)]),
    frozenset([Key.alt_l, KeyCode(vk=83)]),
    frozenset([Key.alt_l, KeyCode(vk=65)]),
    frozenset([KeyCode(vk=65)]),
    frozenset([Key.alt_l, KeyCode(vk=69)]),
    frozenset([KeyCode(vk=71)]),
    frozenset([Key.alt_l, KeyCode(vk=87)]),
    frozenset([KeyCode(vk=70)]),  # finger
    frozenset([KeyCode(vk=68)]),  # auto
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=70)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=71)]),
    frozenset([KeyCode(vk=65)]),
    frozenset([KeyCode(vk=70)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=70)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=69)]),
    frozenset([KeyCode(vk=65)]),
    frozenset([KeyCode(vk=83)]),
    frozenset([KeyCode(vk=68)]),
    frozenset([KeyCode(vk=71)]),
    frozenset([Key.shift_l, KeyCode(vk=68)]),
    frozenset([Key.shift_l, KeyCode(vk=72)]),
    frozenset([KeyCode(vk=81)]),  # volley
    frozenset([KeyCode(vk=70)]),
    frozenset([KeyCode(vk=88)]),
    frozenset([KeyCode(vk=65)]),
    frozenset([KeyCode(vk=70)]),
    frozenset([KeyCode(vk=69)]),
    frozenset([KeyCode(vk=68)]),
]

rotation_rasial = [
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([KeyCode(vk=82)]),  # R
    frozenset([KeyCode(vk=87)]),  # W
    frozenset([KeyCode(vk=87)]),  # W
    frozenset([Key.alt_l, KeyCode(vk=81)]),  # Alt + Q
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=88)]),  # Alt + X
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([Key.alt_l, KeyCode(vk=83)]),  # Alt + S
    frozenset([Key.alt_l, KeyCode(vk=65)]),  # Alt + A
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([Key.alt_l, KeyCode(vk=87)]),  # Alt + W
    frozenset([Key.alt_l, KeyCode(vk=71)]),  # Alt + G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.alt_l, KeyCode(vk=69)]),  # Alt + E
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.shift_l, KeyCode(vk=68)]),  # shift d
    frozenset([Key.shift_l, KeyCode(vk=72)]),  # shift h
    frozenset([KeyCode(vk=81)]),  # Q
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=88)]),
]  # X

rotation_rasial = [
    frozenset([KeyCode(vk=82)]),  # R
    frozenset([KeyCode(vk=87)]),  # W
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=82)]),  # Alt + R
    frozenset([KeyCode(vk=87)]),  # W
    frozenset([Key.alt_l, KeyCode(vk=81)]),  # Alt + Q
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=88)]),  # Alt + X
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([Key.alt_l, KeyCode(vk=83)]),  # Alt + S
    frozenset([Key.alt_l, KeyCode(vk=65)]),  # Alt + A
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([Key.shift_l, KeyCode(vk=66)]),  # Shift + B,
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=87)]),  # Alt + W
    frozenset([Key.alt_l, KeyCode(vk=71)]),  # Alt + G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.alt_l, KeyCode(vk=69)]),  # Alt + E
    frozenset([KeyCode(vk=88)]),  # X
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.shift_l, KeyCode(vk=68)]),  # shift d
    frozenset([Key.shift_l, KeyCode(vk=72)]),  # shift h
    frozenset([KeyCode(vk=81)]),  # Q
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=88)]),
]  # X


rotation_rasial = [
    frozenset([KeyCode(vk=89)]),  # Y
    frozenset([Key.alt_l, KeyCode(vk=81)]),  # Alt + Q
    frozenset([Key.alt_l, KeyCode(vk=82)]),  # Alt + R
    frozenset([KeyCode(vk=87)]),  # W
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=88)]),  # Alt + X
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S #Pre-living Death
    frozenset([Key.alt_l, KeyCode(vk=83)]),  # Alt + S
    frozenset([Key.alt_l, KeyCode(vk=65)]),  # Alt + A
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.shift_l, KeyCode(vk=66)]),  # Shift + B,
    frozenset([Key.alt_l, KeyCode(vk=87)]),  # Alt + W
    frozenset([Key.alt_l, KeyCode(vk=71)]),  # Alt + G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.alt_l, KeyCode(vk=69)]),  # Alt + E
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=88)]),  # X
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.shift_l, KeyCode(vk=68)]),  # shift d
    frozenset([Key.shift_l, KeyCode(vk=72)]),  # shift h
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([Key.shift_l, KeyCode(vk=67)]),  # shift c
    frozenset([KeyCode(vk=81)]),  # Q
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=88)]),  # X
    frozenset([KeyCode(vk=68)]),  # D
]  # X

rotation_rasial = [
    frozenset([KeyCode(vk=89)]),  # Y
    frozenset([Key.alt_l, KeyCode(vk=81)]),  # Alt + Q
    frozenset([Key.alt_l, KeyCode(vk=82)]),  # Alt + R
    frozenset([KeyCode(vk=87)]),  # W
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=88)]),  # Alt + X
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([Key.alt_l, KeyCode(vk=83)]),  # Alt + S
    frozenset([Key.alt_l, KeyCode(vk=65)]),  # Alt + A
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([Key.shift_l, KeyCode(vk=66)]),  # Shift + B,
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=87)]),  # Alt + W
    frozenset([Key.alt_l, KeyCode(vk=71)]),  # Alt + G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.alt_l, KeyCode(vk=69)]),  # Alt + E
    frozenset([KeyCode(vk=88)]),  # X
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.shift_l, KeyCode(vk=68)]),  # shift d
    frozenset([Key.shift_l, KeyCode(vk=72)]),  # shift h
    frozenset([KeyCode(vk=81)]),  # Q
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=88)]),
]  # X

rotation_rasial = [
    frozenset([KeyCode(vk=89)]),  # Y
    frozenset([Key.alt_l, KeyCode(vk=81)]),  # Alt + Q
    frozenset([Key.alt_l, KeyCode(vk=82)]),  # Alt + R
    frozenset([KeyCode(vk=87)]),  # W
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=88)]),  # Alt + X
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([Key.alt_l, KeyCode(vk=83)]),  # Alt + S
    frozenset([Key.alt_l, KeyCode(vk=65)]),  # Alt + A
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([Key.shift_l, KeyCode(vk=66)]),  # Shift + B
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=87)]),  # Alt + W
    frozenset([Key.alt_l, KeyCode(vk=71)]),  # Alt + G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([Key.alt_l, KeyCode(vk=69)]),  # Alt + E
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=88)]),  # X
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.shift_l, KeyCode(vk=68)]),  # shift d
    frozenset([Key.shift_l, KeyCode(vk=72)]),  # shift h
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=81)]),  # Q
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=88)]),
]  # X
# This is the rasial rotation
rotation_rasial = [
    frozenset([KeyCode(vk=89)]),  # Y
    frozenset([Key.alt_l, KeyCode(vk=81)]),  # Alt + Q
    frozenset([Key.alt_l, KeyCode(vk=82)]),  # Alt + R
    frozenset([KeyCode(vk=87)]),  # W
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=88)]),  # Alt + X
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([Key.alt_l, KeyCode(vk=83)]),  # Alt + S
    # frozenset([Key.alt_l, KeyCode(vk=65)]),  # Alt + A
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.shift_l, KeyCode(vk=66)]),  # Shift + B
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=87)]),  # Alt + W
    frozenset([Key.alt_l, KeyCode(vk=71)]),  # Alt + G
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.alt_l, KeyCode(vk=69)]),  # Alt + E
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=88)]),  # X
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.shift_l, KeyCode(vk=68)]),  # shift d
    frozenset([Key.shift_l, KeyCode(vk=72)]),  # shift h
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([KeyCode(vk=81)]),  # Q
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=88)]),  # X
    frozenset([KeyCode(vk=68)]),  # D
]  # X

# BUt really this is the vorkath rotation
""""""
rotation_rasial2 = [
    frozenset([KeyCode(vk=89)]),  # Y
    frozenset([Key.alt_l, KeyCode(vk=87)]),  # Alt + W
    frozenset([Key.alt_l, KeyCode(vk=81)]),  # Alt + Q
    frozenset([KeyCode(vk=87)]),  # W
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=88)]),  # Alt + X
    frozenset([Key.alt_l, KeyCode(vk=71)]),  # Alt + G
    frozenset([Key.shift_l, KeyCode(vk=67)]),  # Shift C
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=81)]),  # Q
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([Key.alt_l, KeyCode(vk=82)]),  # Alt + R
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.alt_l, KeyCode(vk=88)]),  # Alt + X
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([Key.alt_l, KeyCode(vk=83)]),  # Alt + S
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=69)]),  # Alt + E
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([Key.ctrl_l, KeyCode(vk=88)]),  # CTRL X
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([Key.alt_l, KeyCode(vk=88)]),  # Alt + X
    frozenset([KeyCode(vk=68)]),  # D
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([Key.alt_l, KeyCode(vk=87)]),  # Alt + W
    frozenset([Key.alt_l, KeyCode(vk=71)]),  # Alt + G
    frozenset([Key.alt_l, KeyCode(vk=81)]),  # Alt + Q
    frozenset([KeyCode(vk=65)]),  # A
    frozenset([KeyCode(vk=83)]),  # S
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([Key.ctrl_l, KeyCode(vk=88)]),  # CTRL X
    frozenset([KeyCode(vk=81)]),  # Q
    frozenset([KeyCode(vk=70)]),  # F
    frozenset([KeyCode(vk=88)]),  # X
    frozenset([KeyCode(vk=88)]),  # X
]  # X

vorkath_hardmode = [
    frozenset([Key.alt_l, KeyCode(vk=81)]),  # Alt + Q
    frozenset([KeyCode(vk=89)]),  # Y
    frozenset([Key.alt_l, KeyCode(vk=82)]),  # Alt + R
    frozenset([KeyCode(vk=87)]),  # W
    frozenset([KeyCode(vk=69)]),  # E
    frozenset([Key.alt_l, KeyCode(vk=87)]),  # Alt + W
    frozenset([Key.alt_l, KeyCode(vk=88)]),  # Alt + X
    frozenset([Key.alt_l, KeyCode(vk=69)]),  # Alt + E
    frozenset([Key.alt_l, KeyCode(vk=71)]),  # Alt + G
    frozenset([KeyCode(vk=71)]),  # G
    frozenset([KeyCode(vk=81)]),  # Q
]  # X


VK_MAPPING = {
    65: "a",
    66: "b",
    67: "c",
    68: "d",
    69: "e",
    70: "f",
    71: "g",
    72: "h",
    73: "i",
    74: "j",
    75: "k",
    76: "l",
    77: "m",
    78: "n",
    79: "o",
    80: "p",
    81: "q",
    82: "r",
    83: "s",
    84: "t",
    85: "u",
    86: "v",
    87: "w",
    88: "x",
    89: "y",
    90: "z",
}

keybind_image_mappings = {
    None: "Images/Tertiary/End.png",
    "empty": "Images/Tertiary/Empty.png",
    frozenset([KeyCode(vk=65)]): "Images/Necromancy/Touch_of_Death.png",
    frozenset([KeyCode(vk=68)]): "Images/Necromancy/Necromancy_(ability).png",
    frozenset([KeyCode(vk=69)]): "Images/Necromancy/Conjure_Skeleton_Warrior.png",
    frozenset([KeyCode(vk=71)]): "Images/Necromancy/Death_Skulls.png",
    frozenset([KeyCode(vk=82)]): "Images/Necromancy/Conjure_Putrid_Zombie.png",
    frozenset([KeyCode(vk=83)]): "Images/Necromancy/Soul_Sap.png",
    frozenset([KeyCode(vk=87)]): "Images/Necromancy/Conjure_Vengeful_Ghost.png",
    frozenset([KeyCode(vk=89)]): "Images/Necromancy/Conjure_Undead_Army.png",
    frozenset([Key.alt_l, KeyCode(vk=88)]): "Images/Tertiary/Vulnerability_bomb.png",
    frozenset([Key.alt_l, KeyCode(vk=81)]): "Images/Necromancy/Invoke_Death.png",
    frozenset([Key.alt_l, KeyCode(vk=83)]): "Images/Necromancy/Living_Death.png",
    frozenset([Key.alt_l, KeyCode(vk=71)]): "Images/Necromancy/Bloat.png",
    frozenset([Key.shift_l, KeyCode(vk=67)]): "Images/Tertiary/Vengeance.png",
    frozenset([Key.alt_l, KeyCode(vk=87)]): "Images/Necromancy/Split_Soul.png",
    frozenset([KeyCode(vk=70)]): "Images/Necromancy/Finger_of_death.png",
    frozenset([Key.alt_l, KeyCode(vk=69)]): "Images/Tertiary/Undead_Slayer_ability.png",
    frozenset([Key.shift_l, KeyCode(vk=68)]): "Images/Tertiary/Limitless.png",
    frozenset([Key.shift_l, KeyCode(vk=72)]): "Images/Tertiary/Reflect.png",
    frozenset([KeyCode(vk=81)]): "Images/Necromancy/Volley_of_Souls.png",
    frozenset([KeyCode(vk=88)]): "Images/Tertiary/Weapon_Special_Attack.png",
    frozenset([Key.alt_l, KeyCode(vk=65)]): "Images/Tertiary/Adrenaline_renewal.png",
    frozenset([Key.alt_l, KeyCode(vk=82)]): "Images/Necromancy/Life_Transfer.png",
    frozenset([Key.shift_l, KeyCode(vk=66)]): "Images/Tertiary/Divert.png",
    frozenset([Key.ctrl_l, KeyCode(vk=88)]): "Images/Tertiary/Fire Ballista.png",
}

MODIFIER_KEYS = {
    Key.alt_gr: "alt",
    Key.alt: "alt",
    Key.alt_l: "alt",
    Key.alt_r: "alt",
    Key.cmd: "cmd",
    Key.cmd_l: "cmd",
    Key.cmd_r: "cmd",
    Key.ctrl: "ctrl",
    Key.ctrl_r: "ctrl",
    Key.ctrl_l: "ctrl",
    Key.shift_l: "shift",
    Key.shift_r: "shift",
    Key.shift: "shift",
}


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None


def convert_to_str(frozen_set):
    if frozen_set is None:
        return ""
    display_bind = ""
    regular_set = set(frozen_set)
    set2 = set()
    for i in regular_set:
        if i in MODIFIER_KEYS:
            display_bind += str.upper(MODIFIER_KEYS[i])
            display_bind += "+"
        else:
            set2.add(int(str(i)[1:-1]))
    for i in set2:
        display_bind += str.upper(VK_MAPPING[i])
    return str(display_bind)


class MyNotification(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        # [frozenset([Key.shift, KeyCode(vk=65)]),frozenset([KeyCode(vk=65)]),frozenset([Key.shift, KeyCode(vk=66)]),frozenset([Key.alt_l, KeyCode(vk=71)])]
        self.rotation = self.run_rotation(rotation_rasial)  # shift a , shift b, l_alt g
        self.counter = 0
        self.head = self.rotation
        self.prev_abil = None

        self.combination_to_function = rotation_rasial

        self.pressed_vks = set()
        self.listener = Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        self.oldPos = None
        self.ability_change = False
        self.animation_ended = True
        # < Styles >
        self.background_style_css = (
            "background-color: rgba(0, 0, 0, 100); border-radius: 4px;"
        )
        self.close_button_style_css = """
                                        QPushButton{
                                                    background-color: none;
                                                    color: white; border-radius: 6px;
                                                    font-size: 18px;
                                                    }
                                    """
        # </ Styles >

        # < Global Settings >
        height, width = 150, 450
        self.setGeometry(500, 500, width, height)

        # < Main Style >
        self.main_back = QLabel(self)
        self.main_back.resize(width, height)
        self.main_back.setStyleSheet(self.background_style_css)
        # < Text Label >
        # -----------------------------

        layout_horizontal = QHBoxLayout()
        layout_prev = QVBoxLayout()
        layout_cur = QVBoxLayout()
        layout_next = QVBoxLayout()

        self.picture_label_prev = QLabel()
        pixmap = QPixmap(keybind_image_mappings[None])
        resized_pixmap = pixmap.scaled(50, 50)  # Resize the pixmap to 200x200
        self.picture_label_prev.setPixmap(resized_pixmap)
        layout_prev.addWidget(self.picture_label_prev, alignment=Qt.AlignCenter)
        self.prev_ability = QLabel("-")
        self.prev_ability.setText("-")
        self.prev_ability.setStyleSheet("color: white;")
        font = self.prev_ability.font()
        font.setPointSize(13)  # Change font size to 20
        self.prev_ability.setFont(font)
        layout_prev.addWidget(self.prev_ability, alignment=Qt.AlignCenter)
        layout_horizontal.addLayout(layout_prev)

        self.arrowl = QLabel("->")
        self.arrowl.setStyleSheet("color: white;")
        self.arrowl.setFont(font)
        layout_horizontal.addWidget(self.arrowl, alignment=Qt.AlignJustify)

        self.picture_label_cur = QLabel()
        pixmap = QPixmap(keybind_image_mappings[self.rotation.val])
        resized_pixmap = pixmap.scaled(70, 70)  # Resize the pixmap to 200x200
        self.picture_label_cur.setPixmap(resized_pixmap)
        layout_cur.addWidget(self.picture_label_cur, alignment=Qt.AlignCenter)
        self.current_ability = QLabel("Cur")
        self.current_ability.setText(convert_to_str(self.rotation.val))
        self.current_ability.setStyleSheet("color: white;")
        font = self.current_ability.font()
        font.setPointSize(15)  # Change font size to 20
        self.current_ability.setFont(font)
        layout_cur.addWidget(self.current_ability, alignment=Qt.AlignCenter)
        layout_horizontal.addLayout(layout_cur)

        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(1)
        self.picture_label_cur.setGraphicsEffect(self.opacity_effect)
        anim = QPropertyAnimation(self.opacity_effect, b"opacity")
        anim.setEasingCurve(QEasingCurve.InOutCubic)
        anim.setStartValue(1)
        anim.setEndValue(0.2)
        anim.setDuration(200)

        anim_2 = QPropertyAnimation(self.opacity_effect, b"opacity")
        anim_2.setEasingCurve(QEasingCurve.InOutCubic)
        anim_2.setStartValue(0.2)
        anim_2.setEndValue(1)
        anim_2.setDuration(200)

        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(anim)
        self.anim_group.addAnimation(anim_2)
        self.anim_group.finished.connect(self.update_abilites)

        self.arrowr = QLabel("->")
        self.arrowr.setStyleSheet("color: white;")
        self.arrowr.setFont(font)
        layout_horizontal.addWidget(self.arrowr, alignment=Qt.AlignJustify)

        self.picture_label_next = QLabel()
        pixmap = QPixmap(keybind_image_mappings[self.rotation.next.val])
        resized_pixmap = pixmap.scaled(50, 50)  # Resize the pixmap to 200x200
        self.picture_label_next.setPixmap(resized_pixmap)
        layout_next.addWidget(self.picture_label_next, alignment=Qt.AlignCenter)
        self.next_ability = QLabel("Next")
        self.next_ability.setText(convert_to_str(self.rotation.next.val))
        self.next_ability.setStyleSheet("color: white;")
        font = self.next_ability.font()
        font.setPointSize(13)  # Change font size to 20
        self.next_ability.setFont(font)
        layout_next.addWidget(self.next_ability, alignment=Qt.AlignCenter)
        layout_horizontal.addLayout(layout_next)

        widget = QWidget()
        widget.setLayout(layout_horizontal)
        self.setCentralWidget(widget)

        # < Header Style >
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.SplashScreen)
        # This Line Set Your Window Always on To
        # self.setWindowFlags(Qt.SplashScreen | Qt.WindowStaysOnTopHint)
        # </ Header Style >

    def terminal_ask(self):
        global flag_close, clickthrough, reset_rot, ability_change
        while True:
            # press a to print rk
            if flag_close:
                self.close_window()
            if not clickthrough:
                self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, False)
                self.setWindowFlags(self.windowFlags() & ~Qt.WindowTransparentForInput)
                self.show()
            if clickthrough:
                self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
                self.setWindowFlags(self.windowFlags() | Qt.WindowTransparentForInput)
                self.show()
            if reset_rot:
                reset_rot = False
                self.rotation = self.head
                self.prev_abil = None
                self.anim_group.start()

            if self.ability_change:
                self.ability_change = False
                self.anim_group.start()

            QApplication.processEvents()

    def close_window(self):
        self.close()
        sys.exit()

    def run_rotation(self, sample_rotation):
        head = Node(sample_rotation[0])
        cur = head
        for i in range(1, len(sample_rotation)):
            new_node = Node(sample_rotation[i])
            cur.next = new_node
            cur = new_node
        return head

    def print_rot(self, head):
        cur = head
        print("---------")
        while cur is not None:
            print(cur.val)
            cur = cur.next
        print("---------")

    def execute(self, combination):
        """One of your functions to be executed by a combination"""
        if (
            self.rotation is not None
            and self.rotation.val == combination
            and self.animation_ended
        ):
            self.counter += 1
            self.animation_ended = False
            self.prev_abil = self.rotation.val
            self.rotation = self.rotation.next
            self.ability_change = True

    def update_abilites(self):
        self.prev_ability.setText(convert_to_str(self.prev_abil))
        pixmap = QPixmap(keybind_image_mappings[self.prev_abil])
        resized_pixmap = pixmap.scaled(50, 50)  # Resize the pixmap to 200x200
        self.picture_label_prev.setPixmap(resized_pixmap)

        if self.rotation is None:
            self.current_ability.setText("End")
            self.next_ability.setText("-")
            pixmap = QPixmap(keybind_image_mappings[None])
            resized_pixmap = pixmap.scaled(70, 70)  # Resize the pixmap to 200x200
            self.picture_label_cur.setPixmap(resized_pixmap)

            pixmap = QPixmap(keybind_image_mappings["empty"])
            resized_pixmap = pixmap.scaled(50, 50)  # Resize the pixmap to 200x200
            self.picture_label_next.setPixmap(resized_pixmap)

        else:
            self.current_ability.setText(convert_to_str(self.rotation.val))
            pixmap = QPixmap(keybind_image_mappings[self.rotation.val])
            resized_pixmap = pixmap.scaled(70, 70)  # Resize the pixmap to 200x200
            self.picture_label_cur.setPixmap(resized_pixmap)

            if self.rotation.next is not None:
                self.next_ability.setText(convert_to_str(self.rotation.next.val))
                pixmap = QPixmap(keybind_image_mappings[self.rotation.next.val])
                resized_pixmap = pixmap.scaled(50, 50)  # Resize the pixmap to 200x200
                self.picture_label_next.setPixmap(resized_pixmap)
            else:
                pixmap = QPixmap(keybind_image_mappings[None])
                resized_pixmap = pixmap.scaled(50, 50)  # Resize the pixmap to 200x200
                self.picture_label_next.setPixmap(resized_pixmap)
                self.next_ability.setText("End")
        self.animation_ended = True

    def get_vk(self, key):
        """
        Get the virtual key code from a key.
        These are used so case/shift modifications are ignored.
        """
        return key.vk if hasattr(key, "vk") else key.value.vk

    def on_press(self, key):
        """When a key is pressed"""
        global flag_close, clickthrough, reset_rot
        if key == keyboard.Key.pause:
            self.listener.stop()
            flag_close = True

        vk = self.get_vk(key)  # Get the key's vk
        if vk not in self.pressed_vks:
            if key == keyboard.Key.home:
                clickthrough = False
            if key == keyboard.Key.end:
                reset_rot = True

            self.pressed_vks.add(vk)  # Add it to the set of currently pressed keys
            for (
                combination
            ) in self.combination_to_function:  # Loop through each combination
                if self.is_combination_pressed(
                    combination
                ):  # Check if all keys in the combination are pressed
                    self.execute(combination)  # If so, execute the function

    def on_release(self, key):
        """When a key is released"""
        global clickthrough

        vk = self.get_vk(key)  # Get the key's vk
        if key == keyboard.Key.home:
            clickthrough = True
        try:
            self.pressed_vks.remove(
                vk
            )  # Remove it from the set of currently pressed keys
        except:
            pass

    def is_combination_pressed(self, combination):
        """Check if a combination is satisfied using the keys pressed in pressed_vks"""
        return all([self.get_vk(key) in self.pressed_vks for key in combination])

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos is not None:
            delta = event.globalPos() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.oldPos = None


pressed = False

if __name__ == "__main__":
    ability_change = False
    reset_rot = False
    flag_close = False
    clickthrough = False
    My_Application = QApplication(sys.argv)
    MainWindow = MyNotification()
    MainWindow.show()
    MainWindow.terminal_ask()
    sys.exit(My_Application.exec_())
