import numpy as np

# fromfile didnt lead to error for me so I used formbuffer
binary_data_uint8 = np.frombuffer(b"dNAleEz ylrETsEw", dtype=np.uint8)

print("Binary data:", binary_data_uint8)

# Question 1
# Hex numbers calculated in rapid tables
# 64 4E 41 6C 65 45 7A 20 79 6C 72 45 54 73 45 77

# or use python and list comprehension

hex_list= [hex(i)for i in binary_data_uint8]

print("Hexidecimal data:", hex_list)

#Question 2a, change dtype=np.int64

binary_data_int64 = np.frombuffer(b"dNAleEz ylrETsEw", dtype=np.int64)

hex_list2a= [hex(i)for i in binary_data_int64]

print("Binary data (signed64):", binary_data_int64)
print("Hexidecimal data(signed64):", hex_list2a)

#Question 2b: same procedure

binary_data_uint32 = np.frombuffer(b"dNAleEz ylrETsEw", dtype=np.uint32)

hex_list2b= [hex(i)for i in binary_data_uint32]

print("Binary data (unsigned32):", binary_data_uint32)
print("Hexidecimal data(unsigned32):", hex_list2b)

#Question 2c: same proceedure

binary_data_flt64 = np.frombuffer(b"dNAleEz ylrETsEw", dtype=np.float64)

print("Binary data (float64):", binary_data_flt64)


#Question 3 
# after interperating the byte string as a float, I used npbyteswap() to swap the endianness of the dinary data
# Why do we swap endianness? Ans: swapping endianness ensures that data is correctly interpreted and processed regardless of the endianness of the system or device, 
# thereby improving interoperability and compatibility in diverse computing environments.


# Using a dictionary now for a simple for loop with the item() method
binary_data = {
    np.int64: np.frombuffer(b"dNAleEz ylrETsEw", dtype=np.int64),
    np.uint32: np.frombuffer(b"dNAleEz ylrETsEw", dtype=np.uint32),
    np.float64: np.frombuffer(b"dNAleEz ylrETsEw", dtype=np.float64)
}


for dtype, data in binary_data.items():
    # Explicitly set byte order to little endian for compatibility
    data = data.byteswap()
    # Label endian and print the result using f-string formatting
    print(f"Binary data ({dtype.__name__}) after byteswap :", data)

# Definiton: In a big-endian machine, the big end of the data is stored first. In the
# case of multiple bytes, the biggest byte is the first one with the lowest address. On the other hand, little endian machines store data 
# little-end first, with the first byte being the smallest in case of multiple bytes.
# based on analysis of the binary data in the terminal: 
# After byteswap: int64= Little edian, uint32= little endian, flt64= little endian
# the opposite would be true for before the byte swap


#Question 4 ** Come back To this 

ascii_characters = ''.join(chr(byte) for byte in b"dNAleEz ylrETsEw")

# Print the ASCII characters
print("ASCII characters:", ascii_characters)