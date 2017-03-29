import csv
import requests
import json


host = 'localhost'
host = 'http://' + host + ':8545'
headers = {'Content-Type': 'application/json', }

# last block
data = '{"jsonrpc":"2.0","method":"eth_blockNumber","params":[],"id":1}'
result = requests.post(host, headers=headers, data=data)
parsed_json = json.loads(result.text)
lastBlock = int(parsed_json['result'], 0)

c = csv.writer(open("/tmp/listEthereumBlocks.csv", "w"))
c.writerow(['Block Number',
            'Number of transactions',
            'Transaction Index',
            'From',
            'To',
            'Value',
            'gasPrice',
            'gas',
            'Input'])

i = 0
# tested on local blockchain (21.000 blocks)
while i <= lastBlock:

    # number of transactions
    data = '{"jsonrpc":"2.0","method":"eth_getBlockTransactionCountByNumber","params":["' + hex(i) + '"],"id":1}'
    result = requests.post(host, headers=headers, data=data)
    parsed_json = json.loads(result.text)
    nbTransactions = int(parsed_json['result'], 0)

    # block and trasactions description
    data = '{"jsonrpc":"2.0","method":"eth_getBlockByNumber","params":["' + hex(i) + '", true],"id":1}'
    result = requests.post(host, headers=headers, data=data)
    parsed_json = json.loads(result.text)

    if nbTransactions > 0:
        transactions = parsed_json['result']['transactions']
        for transaction in transactions:
            blockNumber = str(int(parsed_json['result']['number'], 0))
            indexTransaction = str(int(transaction['transactionIndex'], 0))
            c.writerow([blockNumber,
                        str(nbTransactions),
                        indexTransaction,
                        str(transaction['from']),
                        str(transaction['to']),
                        str(int(transaction['value'], 0)),
                        str(int(transaction['gasPrice'], 0)),
                        str(int(transaction['gas'], 0)),
                        str(transaction['input'])
                        ])
            print('block: ' + blockNumber + ', transaction index: ' + indexTransaction + ' OK')

    i += 1
