# Prompt: Create a program in python that takes in a string from the user
# and encrypts the message using RSA encryption. You can choose your own p and q.
# Also create a companion program that takes in an encrypted message and decrypts
# it into a string.

# Program 1
# Input: One string message to encrypt

# Output: One string of integers

# Key to encrypt the message
p = 43
q = 59
n = p * q
e = 13

user_message = input("\nEnter your message: ").upper()

# Make the string into an array of characters
user_messages = list(user_message)

print(user_messages)

# Convert the string into numbers
msg_integers = []

for um in user_messages:

    for number in str(ord(um) - ord('A')):
        msg_integers.append(number)

print(msg_integers)

# Break down the message_integers into blocks of "block_size" digits.

block_size = len(str(n))
print("Block Size : " + str(block_size))

# Using list comprehension
blocked_msg_integers = [msg_integers[i * block_size:(i + 1) * block_size] for i in range((len(msg_integers) + block_size - 1) // block_size)]

print(blocked_msg_integers)

# Encrypting the messages using the RSA encryption function
encrypted_messages = []

for msg_integers in blocked_msg_integers:

    if len(msg_integers) != block_size:
        # Add zeroes at the end if necessary
        for i in range(1, (block_size-len(msg_integers)) + 1):
            msg_integers.append(0)

    integers_string = ''
    for msg_int in msg_integers:
        integers_string += str(msg_int)

    encrypted_messages.append((int(integers_string)**e) % n)


print(encrypted_messages)

# Outputting the string of integers that is encrypted

encrypted_int_string = ''
for encrypted_message in encrypted_messages:
    encrypted_int_string += str(encrypted_message)

print("\nEncrypted Messages : " + encrypted_int_string)




