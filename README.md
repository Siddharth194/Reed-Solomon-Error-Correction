GROUP MEMBERS:
1. Siddharth Menon - IMT2022001
2. Vrajnandak Nangunoori - IMT2022527

Steps to Execute:
1. python3 main.py

Files:
-> Global_setup.py: This file includes a 'Global_Variables' object with the default values as defined in global_variable_setup.py and generates the pi_array and dumps it into 'global_vars.bin' file.
-> ReedSolomonTransmit.py: Reads the global variables from the 'global_vars.bin' file and corrupts some of the indices based on the corruption factor read from the 'global_vars.bin' file. The corrupted sequence is now dumped into the 'channel.bin' file.
-> ReedSolomonSend.py: Reads the global variables from the 'global_vars.bin' file, selects a message to be generated along with it's modulo from the pi_array. It then calls Transmit() to send it to the receiver.
-> ReedSolomonReceive: Reads the global variables from the 'global_vars.bin' file and also reads the corrupted sequence from the 'channel.bin' file. It now performs CRT on the corrupted sequence along with the pi_array. Now, it uses reconstruction to try to reconstruct the original message and prints appropriately whether the message can be reconstructed properly or not.

Utility_Files:
-> global_variable_setup.py: Has global values inside a class. They include M,nu(corruption factor),k(number of indices),pi_array
-> MillerRabin.py: Used by Global_setup.py to generate the 'k' primes.
-> EGCD_a_b.py: Used to generate the gcd(a,b) along with the appropriate s,t such that s*a+t*b=d.
-> CRT.py: Used by ReedSolomonReceive.py in order for reconstruction of the original message from the corrupted sequence.
-> EEA.py: Generates the ri,qi,si,ti sequence as ri=q(i+1)*r(i+1) + r(i+2) and similarily for si and ti.
-> Thues.py: Extracts the required r',s',t' from the sequence of ri,si,ti based on the values of r* and t*(values defined in ReedSolomonReceive.py)

Arithmetic_Operation_Files:
-> basic_ops: Has 3 files for division.py, remainder.py, and power.py files.
        a.) division.py: returns the quotient in O(log(n)) time
        b.) remainder.py: returns the remainder in O(log(n)) time
        c.) power.py: returns the value of 'a' raised to power 'b'. O(log(n)) time
