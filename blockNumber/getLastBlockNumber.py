import requests
import json

host = '192.168.0.49'
host = 'http://' + host + ':8545'
headers = {'Content-Type': 'application/json',}
data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
result = requests.post(host, headers=headers, data=data)

print(int(parsed_json['result'], 0))
