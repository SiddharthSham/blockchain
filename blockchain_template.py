class Blockchain:

    def __init__(self):
        

    def new_block(self, proof, previous_hash):

        block = {
            'index': ,
            'timestamp': ,
            'transactions': ,
            'proof': ,
            'previous_hash': ,
        }


    def register_node(self, address):
        

    def valid_chain(self, chain):


    def resolve_conflicts(self):


    def new_transaction(self, sender, recipient, amount):
        {
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        }


    def last_block(self):


    def hash(block):


    def proof_of_work(self, last_block):


    def valid_proof(last_proof, proof, last_hash):



app = Flask(__name__)


node_identifier = #Big unique number


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
    app.run()
