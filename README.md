# ChinaCrypt

ChinaCrypt is a toy encoding scheme where one can encode ascii strings in the form of bytes into a string of chinese characters and back.

## Functions

* `encode`: Converts a bytestring into "chinese" characters.
* `decode`: Converts a string of "chinese" characters into a bytestring.

## Usage:
```
>>> import ChinaCrypt
>>> ChinaCrypt.encode(b'Hello!')
'䡥汬漡'
>>> ChinaCrypt.decode("䡥汬漡")
b'Hello!'
```
## Notes

* Encoding doesn't work so well with lots of spaces (low ascii value). As an alternative, you could use underscores (_) which may yield much better results (looks more chinese).
* There are occasional bad characters that may not render properly.

