# Solution to "crypted string" by SUSPEKT 
#
# This keygen is just a template for this type of encryption, although the behavior is the same,
# the actual mechanics differ between this implementation and the one seen inside the challenge.
#
# github.com/johnnnathan


encrypted_values = [0xffffffc4 ,0xffffff98,0xffffffc2,0xffffff95,0xffffffcc,0xffffff99,0xffffffc6,0xffffff82,0xfffffff8,0xFFFFFF61, 0xFFFFFF26, 0xFFFFFF61, 0xFFFFFF32, 0xFFFFFF61,0xFFFFFF2c , 0xFFFFFF61, 0xFFFFFF29, 0xFFFFFFB1]
result = []
length = len(encrypted_values)
half_length = int(length/2)


for i in range(half_length):
    result.append(encrypted_values[i] - encrypted_values[i + half_length])

decrypted_string = ''.join(chr(val) for val in result)
print(decrypted_string)
