# Program to check how effective is Java's String's Hash Collision
# for generating hash codes for Indian Phone No.s

import random
from pprint import pprint

SAMPLE_SPACE = 10000

def genJavaHashCode(phone: str) -> int:
    """
    s[0]*31^(n-1) + s[1]*31^(n-2) + … + s[n-1]
    where :
    s[i] – is the ith character of the string
    n – is the length of the string, and
    ^ – indicates exponentiation
    """
    return sum( ord(phone[i]) * 31**(len(phone)-i-1) for i in range(len(phone)))

def genPhoneNo():
    """
    Indian Phone No.s usually begin with 7, 8, or 9.
    ( This doesn't include the country code +91. )
    Others are usually scam calls or from other countries.
    They are 10 digits long.
    """
    return str(random.randint(7, 9)) + ''.join(str(random.randint(0, 9)) for _ in range(9))

phone_nos = set([genPhoneNo() for _ in range(SAMPLE_SPACE)])
hash_to_phone = {}
hashCollisions = 0

def populateHashMap():
    for phone in phone_nos:
        hashCode = genJavaHashCode(phone)
        if hashCode in hash_to_phone.keys():
            hashCollisions += 1
        else:
            hash_to_phone[hashCode] = phone

if __name__ == '__main__':
    # pprint(phone_nos)
    populateHashMap()
    print(f"Hash Collisions: {hashCollisions}")
    print(f"hashCollisions rate = {hashCollisions / len(phone_nos)}")
