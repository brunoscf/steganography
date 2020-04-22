from steganography import Steganography

s = Steganography('test.jpg')
s.encode('b'*10_000)