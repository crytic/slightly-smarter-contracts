from manticore.ethereum import ManticoreEVM
from manticore.core.smtlib import Operators
from manticore.core.smtlib import solver

m = ManticoreEVM () # initiate the blockchain

with open('contract.sol','rb') as f:
    contract_src=f.read()

user_account=m.create_account(balance=1000)
attacker_account=m.create_account(balance=1000)

contract_account=m.solidity_create_contract(contract_src,owner=user_account, balance=0)

sym_arg=m.make_symbolic_value(name='arg1')
contract_account.method(sym_arg, caller=user_account)
cond=sym_arg < 10
cond2=sym_arg > 5
m.constrain(cond)
m.constrain(cond2)
# States
# [m.all_states, m.running_states, m.terminated_states]
counter=0
for state in m.running_states:
    state.generate_testcase('test{}'.format(counter))
    counter+=1
