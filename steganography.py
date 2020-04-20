import cv2
import numpy as np

class Steganography:
    def __init__(self, filepath):
        self._image = cv2.imread(filepath)
        self._height, self._width, self._channels = self._image.shape
    
    def _convert_message(self, message, DELIMITER):
        message = DELIMITER + message + DELIMITER
        message = [format(ord(char), 'b').zfill(8) for char in message]
        return ''.join(message)

    def _check_size_enough(self, msg_length):
        '''
            (IMG_HEIGHT * IMG_WIDTH * QUANT_CHANNELS) / BYTE_SIZE
        '''
        if msg_length*8 + 16 > (self._height * self._width * self._channels)/8:
            raise ValueError('The choosen image does not have size enough')

    def encode(self, message, DELIMITER='%'):
        self._check_size_enough(len(message))
        bin_message = self._convert_message(message, DELIMITER)

        for x in range(self._width):
            for y in range(self._height):
                for channel in self._image[y, x]:
                    channel = ord(format(channel, 'b'))[:-1]
            


    def decode(self, DELIMITER=''):
        pass