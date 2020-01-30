from ctypes import *

def lim(self):
    win_lock = windll.LoadLibrary('user32.dll')
    win_lock.LockWorkStation()
