import string

class Rotor:
    def __init__(self, wiring, notch):
        self.wiring = wiring
        self.notch = notch
        self.position = 0

    def set_position(self, position):
        self.position = position % 26

    def rotate(self):
        self.position = (self.position + 1) % 26

    def input(self, letter, forward=True):
        if forward:
            return self.wiring[(ord(letter) - ord('A') + self.position) % 26]
        else:
            return chr((self.wiring.index(letter) - self.position + 26) % 26 + ord('A'))

class Reflector:
    def __init__(self, wiring):
        self.wiring = wiring

    def reflect(self, letter):
        return self.wiring[ord(letter) - ord('A')]

class EnigmaMachine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def set_rotor_positions(self, positions):
        for i, rotor in enumerate(self.rotors):
            rotor.set_position(positions[i])

    def rotate(self):
        self.rotors[0].rotate()
        for i in range(len(self.rotors) - 1):
            if (self.rotors[i].position + 1) % 26 == ord(self.rotors[i].notch) - ord('A'):
                self.rotors[i + 1].rotate()

    def encrypt_letter(self, letter):
        for i, rotor in enumerate(self.rotors):
            letter = rotor.input(letter)
        letter = self.reflector.reflect(letter)
        for i in range(len(self.rotors) - 1, -1, -1):
            letter = rotor.input(letter, forward=False)
        self.rotate()
        return letter

    def encrypt(self, message):
        message = message.upper()
        encrypted_message = ""
        for letter in message:
            if letter in string.ascii_uppercase:
                encrypted_message += self.encrypt_letter(letter)
            else:
                encrypted_message += letter
        return encrypted_message

# Konfigurasi rotor dan reflektor
rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "R")
rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", "F")
rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", "W")
reflectorB = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
reflectorC = Reflector("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

rotors = [rotor1, rotor2, rotor3]
enigma = EnigmaMachine(rotors, reflectorC)

# Set posisi awal rotor
rotor_positions = [0, 0, 0]
enigma.set_rotor_positions(rotor_positions)

# Enkripsi pesan
plain_text = "RYU MIRZA ABRISAM "
cipher_text = enigma.encrypt(plain_text)
print("Pesan Terenkripsi:", cipher_text)
print("Pesan Terdekripsi:", plain_text)