import hashlib
import json
from time import time
from urllib.parse import urlparse
from uuid import uuid4

import requests
from flask import Flask, jsonify, request

class Blockchain:


    def __init__(self):
        #Initialising a block chain
        #1>Current Transactions - List
        #2>Chain - List
        #3>Nodes - Set
        # Creating genesis block

    def new_block(self, proof, previous_hash):

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset transactions
        # append block to chain
        

    def register_node(self, address):
        

    def valid_chain(self, chain):


    def resolve_conflicts(self):


    def new_transaction(self, sender, recipient, amount):


    def last_block(self):


    def hash(block):


    def proof_of_work(self, last_block):


    def valid_proof(last_proof, proof, last_hash):


# Instantiate the Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():

@app.route('/transactions/new', methods=['POST'])
def new_transaction():


@app.route('/chain', methods=['GET'])
def full_chain():


@app.route('/nodes/register', methods=['POST'])
def register_nodes():


@app.route('/nodes/resolve', methods=['GET'])
def consensus():


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)
