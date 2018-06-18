from manticore.ethereum import ManticoreEVM
from manticore.ethereum import DetectIntegerOverflow

m = ManticoreEVM() # initiate the blockchain

overflow_detector=DetectIntegerOverflow()
m.register_plugin(overflow_detector)

with open('interger_overflow.sol','rb') as f:
    contract_src=f.read()

user_account=m.create_account(balance=1000)

contract_account=m.solidity_create_contract(contract_src,
                                            owner=user_account,
                                            balance=0)

contract_account.add(m.SValue, caller=user_account)
contract_account.add(m.SValue, caller=user_account)


print "getting report"
for i in m.all_states:
    raw_findings= overflow_detector.get_findings(i)
    for (wallet, evm_offset, text, tf) in raw_findings:
        print '{} detected at evm offset {}'.format(text,evm_offset)
