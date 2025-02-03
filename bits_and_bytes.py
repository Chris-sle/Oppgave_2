def binary_to_hex(binary_str):
    decimal = int(binary_str, 2)
    return format(decimal, 'X')

def binary_to_ascii(binary_str):
    chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    ascii_chars = [chr(int(b, 2)) for b in chars]
    return ''.join(ascii_chars)

def hex_to_binary(hex_str):
    hex_str = hex_str.replace(" ", "")
    decimal = int(hex_str, 16)
    binary_str = format(decimal, 'b')
    padded_binary = binary_str.zfill(8 * ((len(binary_str) + 7) // 8))
    return padded_binary

def hex_to_ascii(hex_str):
    hex_str = hex_str.replace(" ", "")
    ascii_chars = [chr(int(hex_str[i:i+2], 16)) for i in range(0, len(hex_str), 2)]
    return ''.join(ascii_chars)

def ascii_to_binary(ascii_str):
    return ' '.join(format(ord(char), '08b') for char in ascii_str)

def ascii_to_hex(ascii_str):
    return ' '.join(format(ord(char), '02x') for char in ascii_str)

def main():
    print("Velg konverteringstype:")
    print("1: Binært til Heksadesimal")
    print("2: Binært til ASCII")
    print("3: Heksadesimal til Binært")
    print("4: Heksadesimal til ASCII")
    print("5: ASCII til Binært")
    print("6: ASCII til Heksadesimal")

    choice = input("Skriv inn nummeret for konverteringen du ønsker: ")

    if choice.isdigit() and 1 <= int(choice) <= 6:
        data = input("Skriv inn teksten som skal konverteres: ")

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
        print("Ugyldig valg. Prøv igjen.")

if __name__ == "__main__":
    main()
