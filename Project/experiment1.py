import numpy as np
import random
from scipy.io import wavfile
from create_signal import create_signal

chords = [[261.63, 327.04],[196, 245],[220, 264],[174.61, 209.53]]

FS = 44100

signal = []

for chord in chords:
    for i in range(50):
        note = create_signal(random.choice(chord) / 4 * random.randint(2, 14), 0.1, random.choice(("sin", "triangle")))
        signal.append(note)

signal = np.concatenate(signal)
wavfile.write(str("melody.wav"), FS, signal)

signal = []

for chord in chords:
    for i in range(4):
        note = create_signal(random.choice(chord) * random.choice((1, 2, 1.5)), 1.25, random.choice(("sin", "triangle")))
        signal.append(note)

signal = np.concatenate(signal)

fileName = input("Name your audio: ")
wavfile.write(str("chords.wav"), FS, signal)

signal = []

for chord in chords:
    for i in range(10):
        note = create_signal(random.choice(chord)/2 * random.choice((1, 1.5)), 0.5, "sin")
        signal.append(note)

signal = np.concatenate(signal)

fileName = input("Name your audio: ")
wavfile.write(str("bass.wav"), FS, signal)