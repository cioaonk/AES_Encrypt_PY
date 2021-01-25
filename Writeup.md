Questions

Q1: What happens if you encrypt the same input data twice using this program? Is the output the same? Why or why not?
  
1. After encrypting a message twice, the output was not the same. 
It looks similar, however the results vary from one encryption to another.
This makes sense because if the results were the exact same each time,
then the encryption would be much less secure and more vulnerable to being cracked. 

Q2: What happens if the input length in bytes is not an integer multiple of the 16? What is the significance of the number 16 for this algorithm?

2. So when I ran my program with an input file of 21 bytes, it returned a ValueError
which stated that the length of my provided data is not a multiple of the block length.
This means that the encryption algorithm is being told to encrypt in blocks of 16 bytes 
and any thing more or less than that will not be properly encrypted and thus return an error. 
I believe this is set in relation to the initialization vector or the nature of AES encryption itself. 

Q3: What happens if the length of the key is not 32 bytes? What is the significance of this length for the encryption key?

3. If the key is not 32 bytes, it returns an error, after running a key size verification program. 
The significance of 32 bytes from what i understand is from a fixed block length of 16 bytes and based off the algorithm as 
a subset of Rijndael algorithm determines that it can use a key of 16, 24 or 32 bytes only. 

Q4: Why do you think we ask you to submit the source code encrypted? 

4. I believe you asked for the source code to be encrypted because the source code contains the key variable
and if one was able to find out what key was used to encrypt via AES, that would make this encryption program vulnerable 
and pretty much useless. 
