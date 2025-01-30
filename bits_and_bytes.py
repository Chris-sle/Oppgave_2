def binary_to_hex(binary_str):
    # Konverterer en binær streng til en heksadesimal streng.
    decimal = int(binary_str, 2)  # Konverterer binært til desimal
    return format(decimal, 'X')  # Konverterer desimal til heksadesimal

def binary_to_ascii(binary_str):
    # Konverterer en binær streng til en ASCII-streng.
    # Deler binærstrengen i blokker på 8 biter, konverteres til tegn.
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    ascii_chars = [chr(int(b, 2)) for b in chars]
    return ''.join(ascii_chars)

def hex_to_binary(hex_str):
    # Konverterer en heksadesimal streng til en binær streng.
    hex_str = hex_str.replace(" ", "")  # Fjerner mellomrom
    decimal = int(hex_str, 16)  # Konverterer heksadesimal til desimal
    binary_str = format(decimal, 'b')  # Konverterer desimal til binært
    # Padding for å sikre at binærstrengen lengde er et multiplum av 8
    padded_binary = binary_str.zfill(8 * ((len(binary_str) + 7) // 8))
    return padded_binary

def hex_to_ascii(hex_str):
    # Konverterer en heksadesimal streng til en ASCII-streng.
    hex_str = hex_str.replace(" ", "")  # Fjerner mellomrom
    # Deler heksadesimalstrengen i par og konverterer hver til et tegn.
    ascii_chars = [chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2)]
    return ''.join(ascii_chars)

def ascii_to_binary(ascii_str):
    # Konverterer en ASCII-streng til en binær streng.
    # Finner den binære representasjonen for hver karakter.
    return ' '.join(format(ord(char), '08b') for char in ascii_str)

def ascii_to_hex(ascii_str):
    # Konverterer en ASCII-streng til en heksadesimal streng.
    # Finner den heksadesimale representasjonen for hver karakter.
    return ' '.join(format(ord(char), '02x') for char in ascii_str)

def main():
    # Gir brukeren valgmuligheter for hvilken type konvertering som skal gjøres.
    print("Velg konverteringstype:")
    print("1: Binært til Heksadesimal")
    print("2: Binært til ASCII")
    print("3: Heksadesimal til Binært")
    print("4: Heksadesimal til ASCII")
    print("5: ASCII til Binært")
    print("6: ASCII til Heksadesimal")

    # Henter brukerens valg
    choice = input("Skriv inn nummeret for konverteringen du ønsker: ")

    if choice.isdigit() and 1 <= int(choice) <= 6:
        # Ber brukeren skrive inn teksten som skal konverteres
        data = input("Skriv inn teksten som skal konverteres: ")

        # Utfører korrekt konvertering basert på brukerens valg
        if choice == '1':
            print("Resultat:", binary_to_hex(data))
        elif choice == '2':
            print("Resultat:", binary_to_ascii(data))
        elif choice == '3':
            print("Resultat:", hex_to_binary(data))
        elif choice == '4':
            print("Resultat:", hex_to_ascii(data))
        elif choice == '5':
            print("Resultat:", ascii_to_binary(data))
        elif choice == '6':
            print("Resultat:", ascii_to_hex(data))
    else:
        print("Ugyldig valg. Prøv igjen.")  # Feilmelding ved ugyldig valg

if __name__ == "__main__":
    main()  # Starter programmet
