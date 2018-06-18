from manticore.ethereum import ManticoreEVM
from manticore.core.smtlib import Operators
from manticore.core.smtlib import solver


m = ManticoreEVM () # initiate the blockchain

with open('interger_overflow.sol','rb') as f:
    contract_src=f.read()

user_account=m.create_account(balance=1000)

contract_account=m.solidity_create_contract(contract_src,owner=user_account, balance=0)


contract_account.add(m.SValue, caller=user_account)
contract_account.add(m.SValue, caller=user_account)
contract_account.sellerBalance(caller=user_account)

for state in m.running_states:
    # Check if input0 > sellerBalance

    last_return = state.platform.last_transaction.return_data
    # First input (first call to add)
    input0 = state.input_symbols[0]

    # retrieve last_return and input0 in a similar format
    last_return = Operators.CONCAT(256, *last_return)
    # starts at 4 to skip function id
    input0 = Operators.CONCAT(256, *input0[4:36])

    state.constrain(Operators.UGT(input0, last_return))

    if solver.check(state.constraints):
        print "Overflow found! see %s"%m.workspace
        m.generate_testcase(state, 'OverflowFound')
