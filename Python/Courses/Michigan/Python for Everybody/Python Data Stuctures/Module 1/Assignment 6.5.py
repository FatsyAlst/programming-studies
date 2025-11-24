# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

start_pos = text.find(':')
x_dscpam_confidence = text[start_pos + 1 :]
x_dscpam_confidence = x_dscpam_confidence.strip()
x_dscpam_confidence = float(x_dscpam_confidence)

print(x_dscpam_confidence)