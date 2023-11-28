def getTotCount(num):
    # Find the rightmost set bit
    rightmost_set_bit = num & (-num)

    # Flip all bits to the left of the rightmost set bit
    flipped_bits = num + rightmost_set_bit

    # Count the number of set bits
    count = 0
    while flipped_bits > 0:
        count += flipped_bits & 1
        flipped_bits >>= 1

    return count
