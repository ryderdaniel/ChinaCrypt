def encode(m):
	"""Encodes a bytestring into a string of mostly chinese characters.

	=== Parameters ===
	m: The message in the form of bytes.

	=== Output ===
	A string of chinese characters
	"""
	if len(m) == 0:
		return ""

	from Crypto.Util.number import bytes_to_long
	
	m_split = [m[i:i+2] for i in range(0,len(m),2)]
	if len(m_split[-1]) == 1:
		m_split[-1] += b'\x00'
	
	output = ""
	for c in m_split:
		output += chr(bytes_to_long(c))
	
	return output

	

def decode(c):
	"""Decodes a ChinaCrypt encoded string. Very unlikely to work with real chinese.

	=== Parameters ===
	c: The encoded message in the form of a string.

	=== Output ===
	A bytes object of the original message.
	"""
	if len(c) == 0:
		return ""
	from Crypto.Util.number import long_to_bytes
	output = b''
	for l in c:
		output += long_to_bytes(ord(l))
	return output
