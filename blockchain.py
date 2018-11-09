genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Damien'


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


def mine_block():
    """ Create a new hash """
    last_block = blockchain[-1]
    hash_block = ''
    for key in last_block:
        value = last_block[key]
        hash_block = hash_block + str(value)

    print(hash_block)
    block = {
        'previous_hash': 'XYZ',
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


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
    is_valid = True

    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue

        elif blockchain[block_index][0] == blockchain[block_index - 1]: # is the first block of the current blockchain equal to the previous blockchain
            is_valid = True

        else:
            is_valid = False
            break

        block_index += 1

    return is_valid


waiting_for_input = True

# user choice 
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: mine a new block')
    print('3: Output the blockchain')
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

    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]

    elif user_choice == 'q':
        waiting_for_input = False

    else:
        print('===================================================')
        print('Input is invalid, please pick a value from the list')
        print('===================================================')

    print("<------------------------------------------------------------------------>")

    # if not verify_chain():
    #     print_blockchain_elements()
    #     print('invalid blockchain')
    #     break

print('Done!')
