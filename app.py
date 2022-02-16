import json
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from os import environ as env

from dotenv import load_dotenv
load_dotenv()
abi = env['abi']
bytecode = env['bytecode']

# print(addr);
# web3.py instance
w3 = Web3(HTTPProvider(env['RPC']))
print(w3.isConnected())

key=env['privateKey']
acct = w3.eth.account.privateKeyToAccount(key)

print(acct.address)
print(w3.eth.get_balance(acct.address))
transaction = {
  'to': Web3.toChecksumAddress("0xd6539a16aaf14de06ad26731a0fec5242d505ee2"),
  'from': Web3.toChecksumAddress(acct.address),
  'value': 0,
  'data':"0x3ccfd60b",
  'nonce': w3.eth.get_transaction_count(acct.address),
  'gas': 2000000,
  'maxFeePerGas': 2000000000,
  'maxPriorityFeePerGas': 1000000000,
  'chainId': w3.eth.chain_id
}
signed = w3.eth.account.sign_transaction(transaction, key)
signed.rawTransaction
w3.eth.send_raw_transaction(signed.rawTransaction)