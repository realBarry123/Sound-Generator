
import numpy as np
import scipy
import random
from scipy.io import wavfile

# sample rate
FS = 44100


def create_signal(_freq, _dur, _type):
    """
    :param _freq: the frequency of the signal
    :param _dur: the duration of the signal
    :param _type: the signal type: "sin", "square", "triangle", "sawtooth"
    """

    samples = np.linspace(0, _dur, int(FS * _dur), endpoint=False)

    if _type == "sin":
        sig = np.sin(2 * np.pi * _freq * samples)

    elif _type == "square":
        sig = scipy.signal.square(2 * np.pi * _freq * samples)

    elif _type == "triangle":
        sig = scipy.signal.sawtooth(2 * np.pi * _freq * samples, 0.5)

    elif _type == "sawtooth":
        sig = scipy.signal.sawtooth(2 * np.pi * _freq * samples, 1)

    else:
        raise Exception("wave type not recognized")

    sig *= 32767
    sig = np.int16(sig)
    #sig = np.array(sig, dtype=np.int16)
    return sig


if input("Would you like to: \n[1] Generate Wav File\n[2] Create Random Music") == "2":

    duration = int(input("Enter duration of signal (in seconds): "))

    signals = []

    for i in range(duration * 5):
        signal = create_signal(
            random.randint(200, 1000),
            0.2,
            #random.choice(("sin", "square", "triangle", "sawtooth"))
            random.choice(("triangle", "sin"))
        )
        signals.append(signal)

    # Concatenate the signals
    signal = np.concatenate(signals)


else:

    frequency = int(input("Enter fundamental frequency: "))

    duration = float(input("Enter duration of signal (in seconds): "))

    wave_type = input("Enter wave type: ")

    signal = create_signal(frequency, duration, wave_type)


fileName = input("Name your audio: ")
wavfile.write(str(fileName + ".wav"), FS, signal)
