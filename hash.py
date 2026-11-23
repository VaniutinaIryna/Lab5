import hashlib

def crack(hash):
    for number in range(100000):
        pin = str(number).zfill(5)
        current_hash = hashlib.md5(pin.encode()).hexdigest()
        
        if current_hash == hash:
            return pin
