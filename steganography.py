import cv2
import numpy as np
import time

class Steganography:
    def __init__(self, filename):
        self._image = cv2.imread(filename)
        self._height, self._width, self._channels = self._image.shape
    
    def _get_converted_message(self, message, DELIMITER):
        message = DELIMITER + message + DELIMITER
        message = [format(ord(char), 'b').zfill(8) for char in message]

        for char in ''.join(message):
            yield int(char)
    
    def _get_pixel(self):
        for x in np.arange(self._width):
            for y in np.arange(self._height):
                yield self._image[y, x]

    def _check_size_enough(self, msg_length):
        '''
            (IMG_HEIGHT * IMG_WIDTH * QUANT_CHANNELS) / BYTE_SIZE
        '''
        if msg_length*8 + 16 > (self._height * self._width * self._channels)/8:
            raise ValueError('The choosen image does not have size enough')

    def encode(self, message, DELIMITER='%'):
        self._check_size_enough(len(message))
        bin_message = self._get_converted_message(message, DELIMITER)

        try:
            for pixel in self._get_pixel():
                for pos, channel in enumerate(pixel):
                    pixel[pos] = channel | next(bin_message)

        except StopIteration:
            pass

        finally:
            cv2.imwrite(time.strftime('%m-%d-%Y %H-%M-%S') + '.png', self._image)

    def decode(self, DELIMITER=''):
        pass