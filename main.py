from steganography import Steganography, StegError

if __name__ == '__main__':
    #ENCODE EXAMPLE
    try:
        steg = Steganography('monalisa.jpg')
        steg.encode("""I have no passwords or money to hide!
                                        -Just another poor programmer...""")

    except StegError:
        print('Insert a larger image or a smaller message!')
        
    

    #DECODE EXAMPLE
    # try:
    #     filename = '' #puts here a encoded image
    #     steg = Steganography(filename)
    #     code = steg.decode()
        
    #     print(code)
    
    # except StegError:
    #     print('No one message was found!')