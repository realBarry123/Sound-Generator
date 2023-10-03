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


def rotate_signal(_sig, target):
    while True:
        if _sig[-1] <= target <= _sig[0] or _sig[0] <= target <= _sig[-1]:
            return _sig
        else:
            _sig = np.append(_sig,_sig[0])
            _sig = _sig[1:]


def concat_signal(_sig1, _sig2):
    return np.concatenate((_sig1, rotate_signal(_sig2, _sig1[-1])))


sig1 = create_signal(440, 1, "sin")
sig2 = create_signal(440, 1, "sin")

wavfile.write(str("test.wav"), FS, concat_signal(sig1, sig2))