from steganography import Steganography

Steganography.set_delimiter('&')
#s = Steganography('/home/bruno/Documents/Programacao/Python/steganography/04-22-2020 17-50-30.png')
s = Steganography('/home/bruno/Documents/Programacao/Python/steganography/04-23-2020 18-47-34.png')
# s.encode("""
#      Bruno Simões Cardoso Ferreira
#      Engenharia de Computação
# """)
print(s.decode())