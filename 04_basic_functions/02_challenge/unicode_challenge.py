def encode(message):
    if not message:
        return "Input is empty"
    return " ".join(str(ord(char)) for char in message)

def decode(unicode_sequence):
    if not unicode_sequence:
        return "Input is empty"
    try:
        return "".join(chr(int(code)) for code in unicode_sequence.split())
    except ValueError:
        return "Invalid input"

# Example usage:
if __name__ == "__main__":
    encoded_message = encode("Hello World")
    print(encoded_message)  # Output: 72 101 108 108 111 32 119 111 114 108 100

    decoded_message = decode(encoded_message)
    print(decoded_message)  # Output: Hello World

    # Edge cases
    print(encode(""))  # Output: Input is empty
    print(decode(""))  # Output: Input is empty
    print(decode("72 101 abc"))  # Output: Invalid input