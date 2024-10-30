#!/usr/bin/python3
"""
Interview UTF-8 Validation
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding.
    """
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for num in data:
        # Get the 8 least significant bits of the integer
        byte = num & 0xFF

        if n_bytes == 0:
            # Determine how many bytes the character has
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1

            # If no bytes are needed, this is a 1-byte character
            if n_bytes == 0:
                continue

            # UTF-8 can have at most 4 bytes
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Continuation bytes must start with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # We decrease the number of bytes we expect
        n_bytes -= 1

    # All characters must be fully formed
    return n_bytes == 0


if __name__ == '__main__':
    data = [65]
    print(validUTF8(data))

    data = [
        80,
        121,
        116,
        104,
        111,
        110,
        32,
        105,
        115,
        32,
        99,
        111,
        111,
        108,
        33,
    ]
    print(validUTF8(data))

    data = [229, 65, 127, 256]
    print(validUTF8(data))
