# Author: Authey
# Date: 26/09/2022

from enigma import Enigma


if __name__ == '__main__':
    machine = Enigma(0, 0, 0)
    machine.random_rotors()
    machine.random_reflector()
    command = input('Type your command: ')
    while command != 'end':
        if command == 'encrypt':
            plaintext = input('Type your plaintext: ')
            print('Ciphertext is: {}'.format(machine.encrypt_and_decrypt(plaintext.upper())))
            command = input('Type your command: ')
        elif command == 'decrypt':
            ciphertext = input('Type your ciphertext: ')
            print('Plaintext is: {}'.format(machine.encrypt_and_decrypt(ciphertext).lower()))
            command = input('Type your command: ')
        else:
            print('Unknown command')
            command = input('Retype your command: ')
