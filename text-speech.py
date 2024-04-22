import pyttsx3
import sys, pytesseract, cv2

engine = pyttsx3.init('dummy')

""" RATE"""
rate = engine.getProperty('rate')  # getting details of current speaking rate
print(rate)  # printing current voice   rate
engine.setProperty('rate', 125)  # setting up new voice rate

"""VOLUME"""
volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
print(volume)  # printing current volume level
engine.setProperty('volume', 1.0)  # setting up volume level  between 0 and 1

engine.say("Bonjour je m'appelle Paul")
engine.runAndWait()