# Keygen for jeFF0Falltrades' "x86_Demystified"
# Solution coming soon 
#
# Have a great day :)
# github.com/johnnnathan


stringA = 0x97e7c606 # mast
stringB = 0xb6d3f786 # erOf
stringC = 0xe7465695 # This
stringD = 0xd08636d3 # One

strings = [stringA, stringB, stringC, stringD]

final_result = ""

def process_string(input_string):
    result = []
    for counter in range(16):
        byte = (input_string >> (counter * 8)) & 0xFF
        shifted = ((byte >> 4) | (byte << 4)) & 0xFF
        result_byte = shifted ^ 0xD
        result.append(chr(result_byte))
    return ''.join(result).replace("\r", "")

for string in strings:
    final_result += process_string(string)

print(final_result)

