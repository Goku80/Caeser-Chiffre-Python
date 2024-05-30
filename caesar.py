import sys
from string import ascii_lowercase
from pprint import pprint


def encode_text(text, key):
    """
        Verschlüsselt oder entschlüsselt einen Text mit dem Caesar-Chiffre.

        Args:
            text (str): Der zu verschlüsselnde oder zu entschlüsselnde Text.
            key (int): Der Schlüssel für die Verschlüsselung oder Entschlüsselung.

        Returns:
            str: Der verschlüsselte oder entschlüsselte Text.
        """
    msg = str()
    # Unicode Codepoint: 65 - 90 = A - Z   |   97 - 122 = a - z
    for char in text:
        if char.islower():
            # Umwandlung Charakter in Unicode
            uni_char = ord(char)
            # Berechnung sicherstellen, dass der Bereich 97 - 122 nicht über- oder unterschritten wird
            shift = (uni_char - 97 + key) % 26 + 97
            msg += chr(shift)
        elif char.isupper():
            uni_char = ord(char)
            # Bereich 65 - 90
            shift = (uni_char - 65 + key) % 26 + 65
            msg += chr(shift)
        else:
            msg += char
    return msg


def string_histogram(text):
    """
        Erstellt ein Histogramm für einen gegebenen Text.

        Args:
            text (str): Der Text, für den das Histogramm erstellt wird.

        Returns:
            dict: Das Histogramm mit der Häufigkeit jedes Zeichens.
        """
    histogram = dict()
    text = text.lower()
    for char in text:
        if char.isalpha():
            if char in histogram.keys():
                histogram[char] += 1
            else:
                histogram[char] = 1
    return histogram


def frequencies(histogram):
    """
        Berechnet die Häufigkeit jedes Zeichens in einem Histogramm.

        Args:
            histogram (dict): Das Histogramm mit der Häufigkeit der Zeichen.

        Returns:
            list: Die Liste der Häufigkeiten für jedes Zeichen im Alphabet.
        """
    frequency_list = list()
    total_chars = sum(histogram.values())

    for char in ascii_lowercase:
        frequency_list.append(histogram.get(char, 0) / total_chars)
    return frequency_list


def chi_squared(encrypt_vector, exampletext_vector):
    """
        Berechnet den Chi-Quadrat-Test zwischen zwei Häufigkeitsvektoren.

        Args:
            encrypt_vector (list): Der Häufigkeitsvektor des verschlüsselten Textes.
            exampletext_vector (list): Der Häufigkeitsvektor des Beispiels.

        Returns:
            float: Der Wert des Chi-Quadrat-Tests.
        """
    chi = 0.0
    for i in range(26):
        o = encrypt_vector[i]
        e = exampletext_vector[i]
        if e != 0:
            chi += ((o - e) ** 2) / e
    return chi


def crack_caesar(exampletext, text):
    """
        Knackt den Caesar-Chiffre und entschlüsselt einen Text.

        Args:
            exampletext (str): Ein Beispielsatz zur Vergleich.
            text (str): Der verschlüsselte Text, der entschlüsselt werden soll.

        Returns:
            tuple: Ein Tupel, das den entschlüsselten Text und den Entschlüsselungsschlüssel enthält.
        """
    decrypted_text = str()
    decryption_key = 0
    chi_square_min = float('inf')

    for key in range(26):
        # Text verschlüsselt mit dem Schlüssel invertiert
        # Histogramm Buchstabenfrequenz erstellt
        # Histogramm zurückgegeben und umgewandelt
        exampletext_vector = frequencies(string_histogram(encode_text(exampletext, -key)))
        chi = chi_squared(exampletext_vector, text)

        if chi < chi_square_min:
            chi_square_min = chi
            decryption_key = key
            decrypted_text = encode_text(exampletext, -key)

    return decrypted_text, decryption_key


def main():
    # Aufgabe 2a
    if len(sys.argv) < 3:
        print("Bitte geben Sie beim Programmaufruf: caeser.py 'text' key(int) ein")
        sys.exit(1)

    text = " ".join(sys.argv[1:-1])
    key = int(sys.argv[-1])

    print("Aufgabe 2a")
    print(f"\nEntschlüsselter Text: {encode_text(text, key)}\n" if key < 0
          else f"Verschlüsselter Text: {encode_text(text, key)}\n")

    # Aufgabe 2b
    print("Aufgabe 2b")
    print(string_histogram("Das ist ein Text\n"))

    # Aufgabe 2c
    print("\nAufgabe 2c")
    pprint(frequencies(string_histogram(text)))

    # Aufgabe 2d
    print("\nAufgabe 2d")
    exampletext = "I know that virtue to be in you, Brutus, As well as I do know your outward favour. Well, honour is the subject of my story. I cannot tell what you and other men Think of this life; but, for my single self, I had as lief not be as live to be In awe of such a thing as I myself. I was born free as Caesar; so were you: We both have fed as well, and we can both Endure the winter's cold as well as he: For once, upon a raw and gusty day, The troubled Tiber chafing with her shores, Caesar said to me 'Darest thou, Cassius, now Leap in with me into this angry flood, And swim to yonder point?' Upon the word, Accoutred as I was, I plunged in And bade him follow; so indeed he did. The torrent roar'd, and we did buffet it With lusty sinews, throwing it aside And stemming it with hearts of controversy; But ere we could arrive the point proposed, Caesar cried 'Help me, Cassius, or I sink!' I, as Aeneas, our great ancestor, Did from the flames of Troy upon his shoulder The old Anchises bear, so from the waves of Tiber Did I the tired Caesar. And this man Is now become a god, and Cassius is A wretched creature and must bend his body, If Caesar carelessly but nod on him. He had a fever when he was in Spain, And when the fit was on him, I did mark How he did shake: 'tis true, this god did shake; His coward lips did from their colour fly, And that same eye whose bend doth awe the world Did lose his lustre: I did hear him groan: Ay, and that tongue of his that bade the Romans Mark him and write his speeches in their books, Alas, it cried 'Give me some drink, Titinius,' As a sick girl. Ye gods, it doth amaze me A man of such a feeble temper should So get the start of the majestic world And bear the palm alone."
    encrypted_text = "Reu jf zk zj. Wfi kyzj kzdv Z nzcc cvrmv pfl: Kf-dfiifn, zw pfl gcvrjv kf jgvrb nzky dv, Z nzcc tfdv yfdv kf pfl; fi, zw pfl nzcc, Tfdv yfdv kf dv, reu Z nzcc nrzk wfi pfl."
    histogram_d = string_histogram(exampletext)
    vector_d = frequencies(histogram_d)
    decrypted_text, decryption_key = crack_caesar(encrypted_text, vector_d)
    print(decrypted_text)


if __name__ == "__main__":
    main()
