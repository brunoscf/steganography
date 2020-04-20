from steganography import Steganography

s = Steganography('/home/bruno/Documents/Programacao/Python/steganography/wallpaper2you_296491.jpg')
s.encode('b'*10_000)