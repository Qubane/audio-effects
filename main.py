"""
Main file
"""


import wave
import numpy as np


def read_wav_file(filepath: str) -> tuple[np.ndarray, dict[str, int]]:
    """
    Reads wav files
    :param filepath: path to wave file
    :return: tuple of samples and wave parameters
    """

    # basic parameters
    parameters = {
        "sample_width": 1,
        "channel_number": 1,
        "sample_rate": 48000}

    # open file and read stuff
    with wave.open(filepath, "r") as file:
        parameters["sample_width"] = file.getsampwidth()
        parameters["channel_number"] = file.getnchannels()
        parameters["sample_rate"] = file.getframerate()

        if parameters["sample_width"] == 1:
            samples = np.array(file.readframes(file.getnframes()), dtype=np.int8) ^ 127
        elif parameters["sample_width"] == 2:
            samples = np.array(file.readframes(file.getnframes()), dtype=np.int16)
        elif parameters["sample_width"] == 4:
            samples = np.array(file.readframes(file.getnframes()), dtype=np.float32)
        else:
            raise NotImplementedError

    # return parameters
    return samples, parameters


def write_wav_file(filename: str, samples: np.ndarray, parameters: dict[str, int]) -> None:
    """
    Writes wave file
    :param filename: writing filename
    :param samples: wave file samples
    :param parameters: wave file parameters
    """

    with wave.open(filename, "w") as file:
        file.setsampwidth(parameters["sample_width"])
        file.setnchannels(parameters["channel_number"])
        file.setframerate(parameters["sample_rate"])
        file.writeframes(samples.tobytes())


class Application:
    """
    Application class
    """

    def __init__(self):
        ...

    def run(self):
        """
        Runs the application
        """


def main():
    app = Application()
    app.run()


if __name__ == '__main__':
    main()
