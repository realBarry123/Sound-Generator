
import numpy as np
import random
from scipy.io import wavfile
from create_signal import create_signal

# sample rate
FS = 44100

print("Would you like to: \n[1] Generate Wav File\n[2] Create Random Music")
choice = input(">>> ")

if choice == "2":

    duration = int(input("Enter duration of signal (in seconds) >>> "))

    note_length = float(input("Enter length of each note (in seconds) >>> "))

    signals = []

    for i in range(int(duration / note_length)):
        signal = create_signal(
            random.randint(200, 1000),
            note_length,
            # random.choice(("sin", "square", "triangle", "sawtooth"))
            random.choice(("triangle", "sin"))
        )
        signals.append(signal)

    # Concatenate the signals
    signal = np.concatenate(signals)


elif choice == "1":

    frequency = int(input("Enter fundamental frequency >>> "))

    duration = float(input("Enter duration of signal (in seconds) >>> "))

    wave_type = input("Enter wave type >>> ")

    signal = create_signal(frequency, duration, wave_type)

else:

    raise Exception("enter a fucking number")

fileName = input("Name your audio: ")
wavfile.write(str(fileName + ".wav"), FS, signal)
