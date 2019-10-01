# Program 2
# Input: One string of integers to decrypt
#
# Output: One string message
#
#
# Test the algorithm to make sure that it runs as expected. Give 3 examples.

# Functions to find inverse modulo from LAB 3


def inverse_mod(i, j):

    i = i % j

    for x in range(1, j):

        if (i * x) % j == 1:
            return x

    return 1


# Assuming the message was encrypted using the following keys
p = 43
q = 59
n = p * q
e = 13

user_decryption_msg = input("\nEnter a string of integers to decrypt: ")

# Put the integers into a list
user_decryption_msg = list(user_decryption_msg)

# Determine the block size
block_size = len(str(n))

# Break the integers into the "block_size" digits
blocked_decrypted_msg = [user_decryption_msg[i * block_size:(i + 1) * block_size] for i in range((len(user_decryption_msg) + block_size - 1) // block_size)]

print(blocked_decrypted_msg)

# To store decrypted message
decrypted_messages = []

for msg_integers in blocked_decrypted_msg:

    # If the block does not have block_size digits in it
    if len(msg_integers) != block_size:
        # Add zeroes at the end if necessary
        for i in range(1, (block_size-len(msg_integers)) + 1):
            msg_integers.append(0)

    # If the first digits of the list was zero, ignore it for calculation purposes
    if msg_integers[0] == 0:
        del msg_integers[0]

    integers_string = ''
    for msg_int in msg_integers:
        integers_string += str(msg_int)

    # Decrypted integers by using the RSA decryption function
    num = (int(integers_string) ** inverse_mod(e, (p - 1) * (q - 1))) % n

    # Saving each digits as characters to make it easier to translate to alphabets
    for num_char in list(str(num)):
        decrypted_messages.append(num_char)

print(decrypted_messages)


# Add zero at the first position if necessary
if len(decrypted_messages) < len(user_decryption_msg):
    decrypted_messages.insert(0, 0)


# Before translating back, break the decryped integers into a block of 2 for easier translation
messages = [decrypted_messages[i * 2:(i + 1) * 2] for i in range((len(decrypted_messages) + 2 - 1) // 2)]

print(messages)

# For translating the integers back to letters
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l',
               'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

decrypted_string = ''

for message in messages:
    # Remove 0 again before matching
    if message[0] == 0:
        del message[0]

    print(message)
    two_digits_num = ' '
    for m in message:
        two_digits_num += str(m)

    # Translation back to letters
    decrypted_string += alphabets[int(two_digits_num)]


print("Decrypted Message : " + decrypted_string.upper())




