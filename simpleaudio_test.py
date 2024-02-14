'''
Created for CS-370 Lab Week 3
This is the most basic example of how to play a file using the simpleaudio package
'''

import sounds as sounds
import simpleaudio as sa
import os

# This is a test sound file
def play_sound(filename):
    try:
        wave_obj = sa.WaveObject.from_wave_file(filename)
        print("I am now playing " + filename)
        print(wave_obj)
        play_obj = wave_obj.play()
        play_obj.wait_done()  # Wait until sound has finished playing
    except:
        print('Invalid filepath')

def play_sounds_at_once(filenames):
    waveObjects = []
    for filename in filenames:
        waveObjects.append(sa.WaveObject.from_wave_file(filename))
    playObjects = []
    for wave in waveObjects:
        playObjects.append(wave.play())
    for play in playObjects:
        play.wait_done()

def rename_sound_file(old_name, new_name):
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"File '{old_name}' not found.")
    except FileExistsError:
        print(f"File '{new_name}' already exists.")

'''
TODO: Re-write the above as a function that takes in a filename/filepath as an argument
and plays the sound file
'''



