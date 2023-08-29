#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid UTF-8 encoding
    """

    # Number of bytes in the current UTF-8 character
    number_bytes = 0

    # Bit masks for UTF-8 byte validation
    mask_1 = 1 << 7
    mask_2 = 1 << 6

    for i in data:
        mask_byte = 1 << 7

        if number_bytes == 0:
            # Determine the number of bytes in the current UTF-8 character
            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            # Check for invalid number of bytes
            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            # Check if the byte follows the format 10xxxxxx
            if not (i & mask_1 and not (i & mask_2)):
                return False

        number_bytes -= 1

    # If all bytes have been processed and there are
    # no remaining incomplete UTF-8 characters
    if number_bytes == 0:
        return True

    return False
