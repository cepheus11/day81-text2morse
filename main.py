from morse_dict import MORSE_CODE

input_text = input("Enter text to translate into morse code: ").lower()
output_code = ''
omitted_count = 0
for c in input_text:
    if MORSE_CODE.__contains__(c):
        output_code += MORSE_CODE[c]
    else:
        omitted_count += 1
    output_code += ' '
print(f"The text in Morse Code is: {output_code}")
if omitted_count > 0:
    print(f"{omitted_count} characters were omitted.")
