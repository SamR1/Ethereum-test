import requests
import json

host = 'localhost'
host = 'http://' + host + ':8545'
headers = {'Content-Type': 'application/json', }

# last block
data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
result = requests.post(host, headers=headers, data=data)
parsed_json = json.loads(result.text)

blockNumber = parsed_json['result']
bNumber = str(int(parsed_json['result'], 0))

# block description
data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["' + blockNumber + '", true],"id":1}'
result = requests.post(host, headers=headers, data=data)
parsed_json = json.loads(result.text)

print('Block Description (n° ' + bNumber + ') :')
print('   - difficulty = ' + str(parsed_json['result']['difficulty']))
print('   - extraData = ' + str(parsed_json['result']['extraData']))
print('   - gasLimit = ' + str(parsed_json['result']['gasLimit']))
print('   - gasUsed = ' + str(parsed_json['result']['gasUsed']))
print('   - hash = ' + str(parsed_json['result']['hash']))
print('   - logsBloom = ' + str(parsed_json['result']['logsBloom']))
print('   - miner = ' + str(parsed_json['result']['miner']))
print('   - mixHash = ' + str(parsed_json['result']['mixHash']))
print('   - nonce = ' + str(parsed_json['result']['nonce']))
print('   - parentHash = ' + str(parsed_json['result']['parentHash']))
print('   - receiptsRoot = ' + str(parsed_json['result']['receiptsRoot']))
print('   - sha3Uncles = ' + str(parsed_json['result']['sha3Uncles']))
print('   - size = ' + str(parsed_json['result']['size']))
print('   - stateRoot = ' + str(parsed_json['result']['stateRoot']))
print('   - timestamp = ' + str(parsed_json['result']['timestamp']))
print('   - totalDifficulty = ' + str(parsed_json['result']['totalDifficulty']))
print('   - transactions = ' + str(parsed_json['result']['transactions']))
print('   - transactionsRoot = ' + str(parsed_json['result']['transactionsRoot']))
print('   - uncles = ' + str(parsed_json['result']['uncles']))
