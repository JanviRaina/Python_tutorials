text = "X-DSPAM-Confidence:    0.8475";
f=text.find('0')
l=text[f:]
print(float(l))
