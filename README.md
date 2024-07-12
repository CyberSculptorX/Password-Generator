# Secrets-Password-Generator
The Password Generator ensures secure passwords with a minimum length of 16 characters, preventing manual input by using buttons for adjustments. High-entropy passwords are generated with the secrets module from a diverse character set. Users can exit with the 'Esc' key, and passwords are saved to the Downloads folder without revealing the path.

Steps taken to increase security in password generation.

1) Ensure no data entry box is included, so numbers can not be entered manually.
The label displaying the current password length does not allow direct data input, this ensures the lowest length the password can ever be is 16 characters in length.

2) Controlled length with buttons by setting a minimum limit in the decrease function.
When the "▼" button is pressed, the decrease_length function is called.
This function checks the current password length.
If the current length is greater than 16, it decreases the length by 1.
If the length is 16 or less, it doesn't decrease further, ensuring all passwords generated are 16 characters in length or longer.

The password length starts at 16.
Clicking "▲" increases the length by 1.
Clicking "▼" decreases the length by 1, but only if the current length is greater than 16.
Users cannot type any number; they can only use the buttons.

3) 'import secrets' is used in the code as deemed more secure as it is less predictable because it is using a higher entropy, the measure of randomness. The password string will consist of ascii_letters + digits + punctuation. The more diverse the character set and the longer the password, the higher the entropy.

The variable used was created to contain lowercase and uppercase letters, digits, and punctuation. By including a large variety of characters, we increase the entropy. 

More possible characters mean more possible combinations for the password, making it harder to guess.

Each character is chosen independently, contributing to the overall randomness and unpredictability of the password. The secrets module is specifically designed to generate cryptographically secure random numbers. 

The randomness cannot be easily predicted or reproduced, which is crucial for this project.

The secrets, string and os module are all part of Python's standard library, so you do not need to install these.

Install Python.
Install tkinter.

'main.py' to run.
'Esc' on keyboard to close the program.
