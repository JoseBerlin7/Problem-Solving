'''
Problem - 2:
You would like to set a password for a bank account. However, there are three restrictions on the format of the password:

it has to contain only alphanumerical characters (a-z, A-Z, 0-9);
there should be an even number of letters;
there should be an odd number of digits.
You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and removing, the spaces. The goal is to choose the longest word that is a valid password. You can assume that if there are K spaces in string S then there are exactly K + 1 words.

For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A" and "pass007". Thus the longest password is "pass007" and its length is 7. Note that neither "test" nor "?xy1" is a valid password, because "?" is not an alphanumerical character and "test" contains an even number of digits (zero).

Write a function:

def solution(S)

that, given a non-empty string S consisting of N characters, returns the length of the longest word from the string that is a valid password. If there is no such word, your function should return −1.

For example, given S = "test 5 a0A pass007 ?xy1", your function should return 7, as explained above.

Assume that:

N is an integer within the range [1..200];
string S consists only of printable ASCII characters and spaces.
In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


'''

# Soution - 1:
def valid_pass_check(Passwords):
    longest_val_pass = -1
    for password in Passwords.split():
        if len(password) > longest_val_pass:
            if check_chars(password):
                longest_val_pass = len(password)
    return longest_val_pass


def check_chars(password):
    n_letter = 0
    n_digit = 0
    for char in password:
        if not char.isalnum():
            return False
        if char.isalpha():
            n_letter +=1
        else:
            n_digit +=1
    return n_letter%2 == 0 and n_digit%2 == 1


print("Longest valid password length = ", valid_pass_check("test 5 a0A pass007 ?xy1"))