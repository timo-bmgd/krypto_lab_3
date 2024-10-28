# krypto_lab_3

Implement a small application in your favorite programming language to encode and decode using a Vigenère cipher. The program will take either a keyword and a plaintext and return a cipher text in blocks of 5 characters, or it will take a keyword and a cipher text and return the plaintext.


Encode two longish messages with your algorithm. Use different keys for each message! Post the first one together with its key in the secret message forum. Post the second one without the key. Can you decode all of the other messages for which you have the key? Document which ones you can decode and which ones don't work. What problems did you have? Discuss this in your report!


Now take the messages for which you do not have the key.  Look for repeated bits. The distance between the two is probably a multiple of the key length. If you can find a number of these—the longer the better—and have a number of distances, you might use a gcd to find the length :) Or you can use the Friedman test and calculate the coincidence index. With the length you can then find an easy way to determine the key so that you can recover the plaintext.


(For the bored) Make either a web app or a mobile phone app for encoding and decoding. Send encoded messages to a friend using any popular messaging system.