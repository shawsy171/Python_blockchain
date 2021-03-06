genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Damien'
participants = {'Damien'}


def hash_block(block):
    """ creates a hash for the block """
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0

    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]

    tx_receiver = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0

    for tx in tx_receiver:
        if len(tx) > 0:
            amount_received += tx[0]

    return amount_received - amount_sent


def get_last_blockchain_value():
    """ Returns the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new as value as well as the last blockchain value to the blockhain

        Arguments:
            :sender: The sender of the coins.
            :recipient: The recipient of the coins.
            :amount: The amount of coins sent  with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)


def mine_block():
    """ Create a new hash """
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)
    print(hashed_block)


def get_transaction_value():
    """ Return input of the user (a new transaction amount) as a float"""
    tx_recipient = input('Enter the recipient of the transaction: ')
    # Get the user input, transform it from a string to a float and store it in user_input
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    """ get user input """
    user_input = input('Your choice ')
    return user_input


def print_blockchain_elements():
    """output the blockchain list to the console"""
    for block in blockchain:
        print("------ Outputing Block-------")
        print(block)


def verify_chain():
    """ checks if the first block of the current blockchain equal to the previous blockchain"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue

        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False

    return True


waiting_for_input = True

# user choice
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: mine a new block')
    print('3: Output the blockchain')
    print('4: Output participants')
    print('h: maniulate my blockchain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
        print(open_transactions)

    elif user_choice == '2':
        mine_block()

    elif user_choice == '3':
        print_blockchain_elements()

    elif user_choice == '4':
        print(participants)

    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{
                    'sender': 'Chris',
                    'recipient': 'John',
                    'amount': 100
                }]
            }

    elif user_choice == 'q':
        waiting_for_input = False

    else:
        print('===================================================')
        print('Input is invalid, please pick a value from the list')
        print('===================================================')

    print("<------------------------------------------------------------------------>")

    if not verify_chain():
        print_blockchain_elements()
        print('invalid blockchain')
        # Break out of the loop
        break

    print(get_balance('Damien'))

print('Done!')
