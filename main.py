import json
import binascii
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Random import get_random_bytes


def block(previous_hash, transactions):
    block = {"previous_hash": previous_hash, "transactions": transactions}
    message = json.dumps(block).encode()
    h = PoW(5)
    return {"block": block, "hash": h}


def transaction(amount, sender, recipient, signer):
    transaction = {"amount": amount, "sender": sender, "recipient": recipient}
    message = json.dumps(transaction).encode()
    h = SHA.new(message)
    signature = signer.sign(h).hex()
    return {"transaction": transaction, "signature": signature}


def verify_signature(transaction, signature):
    public_key = transaction["sender"]
    signature = binascii.unhexlify(signature)
    message = json.dumps(transaction).encode()
    verifier = PKCS1_v1_5.new(RSA.import_key(public_key))
    return verifier.verify(SHA.new(message), signature)


def PoW(difficulty):
    while True:
        h = SHA.new(get_random_bytes(128)).hexdigest()
        if h[:difficulty] == "0" * difficulty:
            return h


if __name__ == "__main__":
    a = RSA.generate(1024)
    apub = a.publickey().exportKey().decode()
    asigner = PKCS1_v1_5.new(a)
    b = RSA.generate(1024)
    bpub = b.publickey().exportKey().decode()
    bsigner = PKCS1_v1_5.new(b)
    transactions = [
        transaction(5, apub, bpub, asigner),
        transaction(4, bpub, apub, bsigner),
        transaction(3, apub, bpub, asigner),
        transaction(2, bpub, apub, bsigner),
    ]
    t1 = transactions[:2]
    t2 = transactions[2:]
    genesis = SHA.new(get_random_bytes(128)).hexdigest()
    b1 = block(genesis, t1)
    b2 = block(b1["hash"], t2)
    blockchain = [b1, b2]
