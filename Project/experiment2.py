import numpy as np
import random
from scipy.io import wavfile
from create_signal import create_signal

FS = 44100

frequency1 = int(input("Enter frequency of note 1: "))
frequency2 = int(input("Enter frequency of note 2: "))
# gliss_duration = input("Enter duration of gliss: ")

signal = [create_signal(frequency1, 1, "sin")]

for i in range(int(abs(frequency1 - frequency2) / 8)):
    signal.append(create_signal(frequency1 + i * 8, 0.05, "sin"))

signal.append(create_signal(frequency2, 1, "sin"))

signal = np.concatenate(signal)

wavfile.write(str("combined.wav"), FS, signal)