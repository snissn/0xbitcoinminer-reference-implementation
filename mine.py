import sha3 # pip3 install ethereum
import codecs
from random import getrandbits

def generate_nonce():
  myhex =  b'%064x' % getrandbits(32*8)
  return codecs.decode(myhex, 'hex_codec')

def mine(challenge, public_key, difficulty):
  while True:
    nonce = generate_nonce()
    hash1 = int(sha3.keccak_256(challenge+public_key+nonce).hexdigest(), 16)
    if hash1 < difficulty:
      return nonce, hash1


def main():
  challenge_hex = 'e8b9d966e4e390b81d414df9d98ca5d7df12a262ed5317ab772272d4d33df37c' # recent challenge hex for 0xbitcoin
  challenge = codecs.decode(challenge_hex,'hex_codec')
  public_key_hex = '363b5534fb8b5f615583c7329c9ca8ce6edaf6e6' # miner ethereum public key without leading 0x
  public_key = codecs.decode(public_key_hex,'hex_codec')
  difficulty = 2**234 # example easy difficulty
  valid_nonce, resulting_hash =  mine(challenge, public_key, difficulty)
  print("Valid nonce is: ", valid_nonce)
  print("Resulting hash is: ", resulting_hash)
if __name__ == "__main__":
  main()
