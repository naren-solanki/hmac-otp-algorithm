# hmac-otp-algorithm
This is Python script to generate HMAC based one-time-password(OTP) for dual factor authentication using SHA1 algorithm

Please visit below links for more understanding of HMAC based OTP algorithms:

[RFC 4226: HOTP: An HMAC-Based One-Time Password Algorithm](https://tools.ietf.org/html/rfc4226)

[RFC 6238: TOTP: Time-Based One-Time Password Algorithm](https://tools.ietf.org/html/rfc6238)

## How to use this script with Google Authenticator
1. Open the Google Authenticator app on your smartphone
2. Click on '+' icon to add new account details
3. Select 'Enter a provided key' to enter secret key manually
4. Add 'Account Name' of your choice and 'Your key'
5. A new entry will be added in Google Authenticator app
6. Use the same secret key to generate OTP by this script
