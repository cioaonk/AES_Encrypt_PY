# AES_Encrypt_PY
AES encryption program using python3


Assignment details: 
```
Python encryption program


In this lab you will create a program in Python to encrypt data

 

Requirements for the Encryption program:

Must run at the command line. 
Must encrypt input data using the AES algorithm in CBC mode.
Inputs to the program are
Data to be encrypted (to be read from STDIN)
Output of the program
Encrypted data (to be written to STDOUT)
Defined variables (or constants) within the program
Encryption key
Initialization Vector
 

Prerequisites:

The following must be in place on your test machine:

Functional Python interpreter, at least version 3
Installed cryptography library within your version of Python.
(Instructions here: https://cryptography.io/en/latest/installation.html. Note that building from source is not required)
 

Steps

Create a file containing a message to be encrypted. Make this file exactly 16 bytes in length.
Using the sample code given separately, create a program to encrypt data based on the requirements given above. (Note that the characters “XXX” in the program must be replaced with appropriate code for the program to execute properly. See the reference below for code reference.)
Assign the key variable in the program to a value that is 32 bytes in length. Do not have this value randomly generated. Just make up your own key. 
Using pipes, run the program.
For example: cat {filename} | python3 {programname} > {outputfile1} 2> {outputfile2}
(Note that > redirects STDOUT while 2> redirects STDERR)
Run the program a second time, but this time redirecting the output to different files. 
Compare the results of the second run to the results of the first run. Answer question 1 below.
Create another input file, this one with the input file of a length more than 16 bytes but less than 32 bytes.
Run the program again using the new file as input. Compare the outputs generated by the latest run against the previous two runs of the program. Answer question number 2 below.
Modify the program variable for the encryption key. Make the length of the variable something more than 32 bytes but less than 48 bytes.
Run the program again, redirecting the output to different files. 
Compare the outputs of the latest run of the program to the output from the first run. Answer question number 3 below.
Modify the program variable for the encryption key to make the key 32 bytes again.
Run the program again to confirm correct operation.
Encrypt your source code the instructor’s public key, in ASCII armor format.
Answer question 4 below.

```
resources used:
- https://mothereff.in/byte-counter
- https://cryptography.io/en/latest/hazmat/primitives/symmetric-encryption.html
