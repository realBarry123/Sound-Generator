import numpy as np
import random
from scipy.io import wavfile
from create_signal import create_signal

chords = [[261.63, 327.04],[196, 245],[220, 264],[174.61, 209.53]]

FS = 44100

for i in range(input("Number of repetitions: ")):

# chords

    signal = []

    for chord in chords:
        for j in range(50):
            note = create_signal(random.choice(chord) / 4 * random.randint(2, 14), 0.1, random.choice(("sin", "triangle")))
            signal.append(note)

    signal = np.concatenate(signal)
    combined = signal * 0.04 / np.max(signal)

# melody
    for j in range(2):
        signal = []

        for chord in chords:
            for k in range(4):
                note = create_signal(random.choice(chord) * random.choice((1, 2, 1.5)), 1.25, "triangle")
                signal.append(note)

        signal = np.concatenate(signal)

        combined += signal * 0.1 / np.max(signal)

    # bass

    signal = []

    for chord in chords:
        for j in range(10):
            note = create_signal(random.choice(chord)/2 * random.choice((1, 1.5)), 0.5, "sin")
            signal.append(note)

    signal = np.concatenate(signal)

    combined += signal * 0.1 / np.max(signal)

    if i == 0:
        song = combined
    else:
        song = np.concatenate((song, combined))


wavfile.write(str("combined.wav"), FS, song)