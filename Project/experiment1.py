import numpy as np
import random
from scipy.io import wavfile
from create_signal import create_signal

chords = [[261.63, 327.04],[196, 245],[220, 264],[174.61, 209.53]]

FS = 44100

# chords

signal = []

for chord in chords:
    for i in range(50):
        note = create_signal(random.choice(chord) / 4 * random.randint(2, 14), 0.1, random.choice(("sin", "triangle")))
        signal.append(note)

signal = np.concatenate(signal)
combined = signal * 0.06 / np.max(signal)

# melody
for i in range(2):
    signal = []

    for chord in chords:
        for j in range(4):
            note = create_signal(random.choice(chord) * random.choice((1, 2, 1.5)), 1.25, "triangle")
            signal.append(note)

    signal = np.concatenate(signal)

    combined += signal * 0.1 / np.max(signal)

# bass

signal = []

for chord in chords:
    for i in range(10):
        note = create_signal(random.choice(chord)/2 * random.choice((1, 1.5)), 0.5, "sin")
        signal.append(note)

signal = np.concatenate(signal)

combined += signal * 0.1 / np.max(signal)

wavfile.write(str("combined.wav"), FS, combined)