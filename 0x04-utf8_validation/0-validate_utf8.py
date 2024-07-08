#!/usr/bin/python3
def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the leading bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Iterate over each byte in the data
    for byte in data:
        mask = 1 << 7
        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1
            if num_bytes == 0:
                continue
            # If the character is only 1 byte long, it's already valid
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # Check that the byte starts with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False
        num_bytes -= 1

# If we finish processing
    return num_bytes == 0
