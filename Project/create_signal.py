import numpy as np
import random
import scipy
from scipy.io import wavfile

# sample rate
FS = 44100
def create_signal(_freq, _dur, _type):

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
    # sig = np.array(sig, dtype=np.int16)
    return sig