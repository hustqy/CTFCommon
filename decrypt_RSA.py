def decrypt_RSA(private_key_loc, package):
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    from base64 import b64decode
    key = open(private_key_loc, "r").read()
    rsakey = RSA.importKey(key)
    rsakey = PKCS1_OAEP.new(rsakey)
    decrypted = rsakey.decrypt(b64decode(package))
    return decrypted
key = "Zc2LYzlDHW6fEwMqqey8d6uCYWXEcUWt0LMvx3fMA/YMezn7jkXoUOkZD8pQyH5DBhJFCzSIoIUMaV+rJzyUooAIfxCG87Ej9CDDOb1CB+bxY2fH4Xr0D2iJMyKCgN9WwLggfJheJEcLsjhNx32lhJ81WGX/yQpk9HEDAaIBu1ds5BP0Cfy+aUOp9JDH9+b+9jjTgJpccBfh4uCG2XusQ7SDVMbejBIH/rGKNVlg8aSasOjDQ0PErHwzMVp4ewEk0va4NBJYhilxeTZyO+m2f/tw63LmTHmVxFzmzcCvAYv5M9wsACqi8BkCaSqwRHKXmN96eeLJE0qyEUvgSM+i9w=="
print decrypt_RSA('private.pem', key)
