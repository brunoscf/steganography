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
        first_char = np.where(self._image[:8] % 2, '1', '0')
        first_char = ''.join(first_char)

        if chr(int(first_char, 2)) != DELIMITER:
             raise ValueError('The image has no a hidden message written using the choosen delimiter')

    def encode(self, message, DELIMITER='%'):
        self._check_size_enough(len(message))
        bin_message = self._get_converted_message(message, DELIMITER)

        try:
            for pos, channel in enumerate(self._image):
                self._image[pos] = int(format(channel, 'b')[:-1] + next(bin_message), 2)

        except StopIteration:
            pass

        finally:
            self._image = self._image.reshape(self._initial_shape)
            cv2.imwrite(time.strftime('%m-%d-%Y %H-%M-%S') + '.png', self._image)

    def decode(self, DELIMITER='%'):
        self._has_message_hidden(DELIMITER)
        
        decoded_msg = []
        while True:
            self._image = np.delete(self._image, [0, 1, 2, 3, 4, 5, 6, 7])
            byte = np.where(self._image[:8] % 2, '1', '0')
            byte = "".join(byte)
            char = chr(int(byte, 2))
            if char == DELIMITER:
                break
            decoded_msg.append(char)

        return "".join(decoded_msg)