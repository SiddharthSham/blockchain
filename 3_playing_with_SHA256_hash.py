import hashlib

def hash(obj):
    return hashlib.sha256(str(obj).encode('utf-8')).hexdigest()

if __name__ == '__main__' :
    data1 = ['hello', 'world']
    data2 = 3
    data3 = 12892803140938.12329831
    data4 = """A blockchain, originally block chain, is a growing
 list of records, called blocks, which are linked using cryptography. Each
 block contains a cryptographic hash of the previous block, a timestamp, and
 transaction data (generally represented as a merkle tree root hash).

By design, a blockchain is resistant to modification of the data. It is "an open,
 distributed ledger that can record transactions between two parties efficiently
 and in a verifiable and permanent way". For use as a distributed ledger, a
 blockchain is typically managed by a peer-to-peer network collectively adhering
 to a protocol for inter-node communication and validating new blocks. Once
 recorded, the data in any given block cannot be altered retroactively without
 alteration of all subsequent blocks, which requires consensus of the network
 majority. Although blockchain records are not unalterable, blockchains may be
 considered secure by design and exemplify a distributed computing system with
 high Byzantine fault tolerance. Decentralized consensus has therefore been
 claimed with a blockchain.

Blockchain was invented by Satoshi Nakamoto in 2008 to serve as the public
 transaction ledger of the cryptocurrency bitcoin. The invention of the blockchain
 for bitcoin made it the first digital currency to solve the double-spending
 problem without the need of a trusted authority or central server. The bitcoin
 design has inspired other applications, and blockchains which are readable by the
 public are widely used by cryptocurrencies. Private blockchains have been
 proposed for business use. Some marketing of blockchains has been called "snake
 oil". """
    data5 = { "key1":"value1",
              "key2":"value2",
              "key3":"value3",
              "key4":"value4",
              "key5":"value5" }
    data6 = set([1,8,2,4,5,6])

    print(hash(data1)+":"+str(data1)+"\n")
    print(hash(data2)+":"+str(data2)+"\n")
    print(hash(data3)+":"+str(data3)+"\n")
    print(hash(data4)+":"+str(data4)+"\n")
    print(hash(data5)+":"+str(data5)+"\n")
    print(hash(data6)+":"+str(data6)+"\n")
