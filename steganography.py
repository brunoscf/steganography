import cv2
import numpy as np
import time

class Steganography:
    def __init__(self, filename):
        self._image = cv2.imread(filename)
        self._initial_shape = self._image.shape
        self._image = self._image.flatten()

    def _get_converted_message(self, message, DELIMITER):
        message = DELIMITER + message + DELIMITER
        message = [format(ord(char), 'b').zfill(8) for char in message]

        for char in ''.join(message):
            yield char

    def _check_size_enough(self, msg_length):
        '''
            (IMG_HEIGHT * IMG_WIDTH * QUANT_CHANNELS) / BYTE_SIZE
        '''
        if msg_length*8 + 16 > self._image.size/8:
            raise ValueError('The choosen image does not have size enough')

    def _has_message_hidden(self, DELIMITER):
        print(self._image[:8])

    def encode(self, message, DELIMITER='%'):
        self._check_size_enough(len(message))
        bin_message = self._get_converted_message(message, DELIMITER)

        try:
            for pos, channel in enumerate(self._image):
                self._image[pos] = int(format(channel, 'b')[:-1] + next(bin_message), 2)

        except StopIteration:
            pass

        finally:
            self._image = np.reshape(self._image, self._initial_shape)
            cv2.imwrite(time.strftime('%m-%d-%Y %H-%M-%S') + '.bmp', self._image)

    def decode(self, DELIMITER='%'):
        self._has_message_hidden(DELIMITER)
        print('existe')