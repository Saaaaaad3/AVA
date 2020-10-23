import win32clipboard as win32
import AssistantSpeak as ASpeak
import time
import pyautogui as pya
import pyperclip


def copydata():
    win32.OpenClipboard()
    copiedData = win32.GetClipboardData()
    win32.CloseClipboard()
    ASpeak.speak("\n" + copiedData)

def copy():
    pya.hotkey('ctrl', 'c')
    time.sleep(0.3)

def paste():
    pya.hotkey('ctrl','v')
    