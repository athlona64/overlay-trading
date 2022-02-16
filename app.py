import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from mnemonic import Mnemonic
from coincurve import PrivateKey
from bip44 import Wallet
from bip44.utils import get_eth_addr
from os import environ as env

from dotenv import load_dotenv
load_dotenv()


mnemo = Mnemonic("english")

# words = mnemo.generate(strength=256)
# words = mnemo.generate();
# print(words);



w = Wallet(env['MNEMONIC'])
sk, pk = w.derive_account("eth", account=0)
# print(pk);
sk = PrivateKey(sk)
sk.public_key.format() == pk
addr = get_eth_addr(pk)

print(addr);
# web3.py instance
# apiKey = "xeXhUjdEEpBfAFuCDwRftiCr0xx_hHFy";
# w3 = Web3(HTTPProvider("https://eth-kovan.alchemyapi.io/v2/" + apiKey))
# print(w3.isConnected())

# key="<Private Key here with 0x prefix>"