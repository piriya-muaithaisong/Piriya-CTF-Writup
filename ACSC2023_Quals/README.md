# ACSC Qualification Round 2023
## Table of Content
- [Merkle Hellman](#Merkle-Hellman)



## Merkle Hellman (Crypto)

I solved this challenge by implementing the decryption algorithm from Wikipedia.

[image]

However, because this challenge did not provide me with the r parameter, I attempted to brute-force it using my python code.

[Link]

After a few minutes, I got the flag.

```
flag [image]
```

## pcap-1 (Forensic)

First, I tried using the Wireshark filter to list all of the keystrokes.
```
((usb.transfer_type == 0x01) && (frame.len == 72)) && !(usb.capdata == 00:00:00:00:00:00:00:00)
```
And exported them to JSON file (usb.json)

[image]

Then, I used the Python code below to extract keystrokes

[Link]

And using this Python code to decode all keystroke payloads

[Link]

After decoding, I received quite an strange flag.

```
strange flag
```
So I tried to transform it back into the real flag.
```
real flag
```
