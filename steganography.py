import cv2
import numpy as np
import time

class StegError(Exception):
    pass
class Steganography:
    """
    This class allows you to encode and decode text messages within images.
      * The DELIMITER marks the beginning and the end of a message. It can be changed using
        the class method `set_delimiter`. The default delimiter is `^`.
      * The output of the encode method is a file, where the name is the current date and time
        and the format is .png
      * Encode method saves the output image automatically
    """

    DELIMITER = "^"

    def __init__(self, filename):
        self._image = cv2.imread(filename)
        self._original_shape = self._image.shape
        self._image = self._image.flatten()

    @classmethod
    def set_delimiter(self, DELIMITER: str):
        self.DELIMITER = DELIMITER

    def _get_converted_message(self, message: str) -> str:
        """
            Returns the message converted to binary between delimiters
        """
        message = self.DELIMITER + message + self.DELIMITER
        message = [format(ord(char), "b").zfill(8) for char in message]

        for char in "".join(message):
            yield char

    def _check_enough_size(self, msg_length: int):
        if msg_length * 8 + 16 > self._image.size / 8:
            raise StegError("The choosen image does not have size enough")

    def _has_message_hidden(self):
        """
            Checks if the current delimiter is the first character in the image. If it is, so the message has a hidden message
        """
        first_char = np.where(self._image[:8] % 2, "1", "0")
        first_char = "".join(first_char)

        if chr(int(first_char, 2)) != self.DELIMITER:
            raise StegError(
                "The image has no a hidden message written using the current delimiter"
            )

    def encode(self, message: str):
        self._check_enough_size(len(message))
        bin_message = self._get_converted_message(message)

        try:
            for pos, channel in enumerate(self._image):
                self._image[pos] = int(format(channel, "b")[:-1] + next(bin_message), 2)

        except StopIteration:
            pass

        finally:
            self._image = self._image.reshape(self._original_shape)  # recovery the image's original shape
            cv2.imwrite(time.strftime("%m-%d-%Y %H-%M-%S") + ".png", self._image)

    def decode(self) -> str:
        self._has_message_hidden()

        decoded_msg = []
        while True:
            self._image = np.delete(self._image, [0, 1, 2, 3, 4, 5, 6, 7])
            byte = np.where(self._image[:8] % 2, "1", "0")
            byte = "".join(byte)
            char = chr(int(byte, 2))

            if char == self.DELIMITER:
                break
            decoded_msg.append(char)

        return "".join(decoded_msg)
