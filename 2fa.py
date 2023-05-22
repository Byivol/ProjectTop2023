import pyotp
import qrcode

key = pyotp.random_base32()

uri = pyotp.TOTP(key).provisioning_uri(name="ExampleItTopProject", issuer_name="ExampleAPP")
qrcode.make(uri).save("totp.png")
totp = pyotp.TOTP(key)
while True:
    input_2facode = totp.verify(input("Введите 2FA код: "))
    print(input_2facode)
