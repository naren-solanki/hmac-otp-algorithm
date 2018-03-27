#!/usr/bin/python3
__author__ = "Narendra Solanki"

from hashlib import sha1
import hmac
import time

"""
This method will generate a HMAC based one-time-password (OTP) for dual factor authentication
@secretKey: string
    A shared secret key provided by the caller
@otp_length: integer
    Length of the OTP required, default value is 6
@time_window: integer
    Length of period in seconds for which the same OTP will be generated
    For example with default value of 30 seconds, code will generate same value at 1:00:00 PM to 1:00:29 PM
"""
def generateOTP(secretKey, otp_length=6, time_window=30):
    OTP_LENGTH = otp_length
    TIME_WINDOW = time_window
    key = secretKey.encode()

    #get the current time
    t = time.time()

    #truncate time to 30 seconds boundary
    t = t - t%TIME_WINDOW

    #get time as byte array
    msgTime = str(t)[:-2].encode()

    #convert hexdigest number to byte array
    #get HMAC string using SHA1 (160 bits or 20 bytes for SHA1)
    hmac_result = hmac.new(key, msgTime, sha1).hexdigest().encode()

    #get the last nibble(4-bit) from the hex number
    #we will use it as a dynamic index to get 4-byte number from 20 bytes number
    offset   =  hmac_result[len(hmac_result)-1] & 0xf;

    #get the bytes at index = offset, offset+1, offset+2 and offset+3
    #create a 31 bit number from these 4 bytes

    #mask first byte with 0x7f to drop 32nd bit
    bin_code = (hmac_result[offset]  & 0x7f) << 24

    #extract second byte and add to the number
    bin_code|= (hmac_result[offset+1] & 0xff) << 16

    #extract third byte and add to the number
    bin_code|= (hmac_result[offset+2] & 0xff) << 8

    #extract last byte and add to the number
    bin_code|= (hmac_result[offset+3] & 0xff)

    #now bin_code contains a 31-bit integer number

    #get a 6 digit decimal number from bin_code
    otp = str(bin_code%(10**OTP_LENGTH))

    #append leading zeros to make OTP length equal to OTP_LENGTH
    while len(otp) < OTP_LENGTH:
        otp = "0"+otp

    if __name__ == '__main__':
        generateOTP("SECRET_KEY")
