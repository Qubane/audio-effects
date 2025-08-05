"""
Main file
"""


import wave
import numpy as np


def read_wav_file(filepath: str) -> tuple[bytes, dict[str, int]]:
    """
    Reads wav files
    :param filepath: path to wave file
    :return: tuple of raw bytes and wave parameters
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
        frames = file.readframes(file.getnframes())

    # return parameters
    return frames, parameters


class Application:
    """
    Application class
    """

    def __init__(self):
        ...

    def run(self):
        ...


def main():
    app = Application()
    app.run()


if __name__ == '__main__':
    main()
