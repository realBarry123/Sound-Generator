# Sound-Generator

## Overview
This is a project that aims to help me create music with the help of simple Python programs. It is messy. There is a quadruple nested for loop in experiment1.py that I am trying my best to ignore. 

## Main.py
Running this file will give you 2 options: 
#### 1: Generate Wav File
Writes a .wav file based on the given frequency, duration, and wave shape
#### 2: Create Random Music
Generates random notes and writes in a .wav file

## Experiment1.py
This writes a melody, chordal accompaniment, and bass line based on the generic C G A- F- progression

## Experiment2.py
Does gliss. Sounds terrible

## Functions
#### create_signal(_freq: number in hertz, _dur: number in seconds, _type: string "sin", "triangle", "sawtooth", "square")
- Output: np array of a signal
#### rotate_signal(_sig: list representation of signal, target: number)
- Output: list rotated with target number at the front
