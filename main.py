from steganography import Steganography

#s = Steganography('/home/bruno/Documents/Programacao/Python/steganography/04-22-2020 17-50-30.png')
s = Steganography('/home/bruno/Documents/Programacao/Python/steganography/04-23-2020 18-06-04.png')
# s.encode("""
#     Bruno Simões Cardoso Ferreira
#     Engenharia de Computação
# """)
print(s.decode())