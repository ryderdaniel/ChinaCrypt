def encode(m):
	"""Encodes a bytestring into a string of mostly chinese characters.

	=== Parameters ===
	m: The message in the form of bytes.

	=== Output ===
	A string of chinese characters
	"""
	if len(m) == 0:
		return ""

	from Crypto.Util.number import bytes_to_long, long_to_bytes
	reference = dict()

	for l1 in range(32,127):
		for l2 in range(32,127):
			reference[(chr(l1)+chr(l2)).encode()] = chr(bytes_to_long((chr(l1)+chr(l2)).encode()))
	for l1 in range(32,127):
		reference[(chr(l1)).encode() + b'\x00'] = chr(bytes_to_long((chr(l1)).encode() + b'\x00'))

	m_split = [m[i:i+2] for i in range(0,len(m),2)]
	if len(m_split[-1]) == 1:
		m_split[-1] += b'\x00'
	
	output = ""
	for c in m_split:
		output += reference[c]
	
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
	from Crypto.Util.number import bytes_to_long, long_to_bytes
	reference = dict()
	for l1 in range(32,127):
		for l2 in range(32,127):
			reference[chr(bytes_to_long((chr(l1)+chr(l2)).encode()))] = (chr(l1)+chr(l2)).encode()
	for l1 in range(32,127):
		reference[chr(bytes_to_long((chr(l1)).encode() + b'\x00'))] = (chr(l1)).encode() + b'\x00'
	
	output = b''
	for l in c:
		output += reference[l]
	return output
