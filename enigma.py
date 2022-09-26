# Author: Authey
# Date: 26/09/2022

import random


class Enigma:

    def __init__(self, a, b, c):
        self.rotor_0 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.rotor_1 = ['E', 'K', 'M', 'F', 'L', 'G', 'D', 'Q', 'V', 'Z', 'N', 'T', 'O', 'W', 'Y', 'H', 'X', 'U', 'S', 'P', 'A', 'I', 'B', 'R', 'C', 'J']
        self.rotor_2 = ['A', 'J', 'D', 'K', 'S', 'I', 'R', 'U', 'X', 'B', 'L', 'H', 'W', 'T', 'M', 'C', 'Q', 'G', 'Z', 'N', 'P', 'Y', 'F', 'V', 'O', 'E']
        self.rotor_3 = ['B', 'D', 'F', 'H', 'J', 'L', 'C', 'P', 'R', 'T', 'X', 'V', 'Z', 'N', 'Y', 'E', 'I', 'W', 'G', 'A', 'K', 'M', 'U', 'S', 'Q', 'O']
        self.rotor_4 = ['E', 'S', 'O', 'V', 'P', 'Z', 'J', 'A', 'Y', 'Q', 'U', 'I', 'R', 'H', 'X', 'L', 'N', 'F', 'T', 'G', 'K', 'D', 'C', 'M', 'W', 'B']
        self.rotor_5 = ['V', 'Z', 'B', 'R', 'G', 'I', 'T', 'Y', 'U', 'P', 'S', 'D', 'N', 'H', 'L', 'X', 'A', 'W', 'M', 'J', 'Q', 'O', 'F', 'E', 'C', 'K']
        self.rotor_6 = ['J', 'P', 'G', 'V', 'O', 'U', 'M', 'F', 'Y', 'Q', 'B', 'E', 'N', 'H', 'Z', 'R', 'D', 'K', 'A', 'S', 'X', 'L', 'I', 'C', 'T', 'W']
        self.rotor_7 = ['N', 'Z', 'J', 'H', 'G', 'R', 'C', 'X', 'M', 'Y', 'S', 'W', 'B', 'O', 'U', 'F', 'A', 'I', 'V', 'L', 'P', 'E', 'K', 'Q', 'D', 'T']
        self.rotor_8 = ['F', 'K', 'Q', 'H', 'T', 'L', 'X', 'O', 'C', 'B', 'J', 'S', 'P', 'D', 'Z', 'R', 'A', 'M', 'E', 'W', 'N', 'I', 'U', 'Y', 'G', 'V']
        self.reflector_1 = {'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'I': 'P', 'J': 'X', 'K': 'N', 'M': 'O', 'T': 'Z', 'V': 'W'}
        self.reflector_2 = {'A': 'F', 'B': 'V', 'C': 'P', 'D': 'J', 'E': 'I', 'G': 'O', 'H': 'Y', 'K': 'R', 'L': 'Z', 'M': 'X', 'N': 'W', 'T': 'Q', 'S': 'U'}
        self.rotor_settings = [a, b, c]
        self.all_rotor_list = [self.rotor_1, self.rotor_2, self.rotor_3, self.rotor_4, self.rotor_5, self.rotor_6, self.rotor_7, self.rotor_8]
        self.all_reflector_list = [self.reflector_1, self.reflector_2]
        self.rotors = [self.rotor_1, self.rotor_2, self.rotor_3]
        self.reflector = [self.reflector_1]

    def random_rotors(self):
        self.rotors = random.sample(self.all_rotor_list, 3)

    def random_reflector(self):
        self.reflector = random.sample(self.all_reflector_list, 1)

    def random_plugbooard(self):
        # TODO
        pass

    def encrypt_and_decrypt(self, text):
        result = []
        for letter in text:
            if letter == ' ':
                result.append(' ')
                continue
            cur_index = (self.rotor_0.index(letter) + self.rotor_settings[0]) % 26
            cur_letter = self.rotors[0][cur_index]
            cur_index = (self.rotor_0.index(cur_letter) + self.rotor_settings[1]) % 26
            cur_letter = self.rotors[1][cur_index]
            cur_index = (self.rotor_0.index(cur_letter) + self.rotor_settings[2]) % 26
            cur_letter = self.rotors[2][cur_index]
            if cur_letter in self.reflector[0].keys():
                cur_letter = self.reflector[0][cur_letter]
            else:
                cur_letter = [key for key, value in self.reflector[0].items() if value == cur_letter][0]
            cur_index = (self.rotors[2].index(cur_letter) + self.rotor_settings[2]) % 26
            cur_letter = self.rotor_0[cur_index]
            cur_index = (self.rotors[1].index(cur_letter) + self.rotor_settings[1]) % 26
            cur_letter = self.rotor_0[cur_index]
            cur_index = (self.rotors[0].index(cur_letter) + self.rotor_settings[0]) % 26
            cur_letter = self.rotor_0[cur_index]
            result.append(cur_letter)
        return ''.join(result)
