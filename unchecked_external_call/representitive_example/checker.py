#!/usr/bin/env python
# -*- coding: utf-8 -*-

from manticore.ethereum import *
from manticore.core.smtlib import *


class DetectUncheckedExternalCall(Detector):
    # '''
    #     Detects when the result of an external call is unchecked
    # '''
    def __init__(self):
        Detector.__init__(self)
        self.taint_label="CALL_RETURN"

    def _save_current_location(self, state):
        address = state.platform.current_vm.address
        pc = state.platform.current_vm.pc
        at_init = state.platform.current_transaction.sort == 'CREATE'
        location = (address, pc, finding, at_init, condition)
        hash_id = hashlib.sha1(str(location)).hexdigest()
        state.context.setdefault('{:s}.locations'.format(self.name), {})[hash_id] = location
        return hash_id


    def _handle_calls(self, state, instruction, arguments, result_ref):
        #Each call has a uniqe return.
        #Apply taint at every call site.

        print "inside call instruction"
        # print type(instruction), instruction
        # print type(instruction.semantics), instruction.semantics
        # print type(result_ref), result_ref
        # print type(result_ref.value), result_ref.value
        print arguments
        result=result_ref.value
        result_ref.value=taint_with(result, self.taint_label)



    def did_evm_execute_instruction_callback(self, state, instruction, arguments, result_ref):
        mnemonic = instruction.semantics

        print mnemonic
        if any(map(lambda a: istainted(a,self.taint_label),arguments)):
            print "{} found in {}".format(self.taint_label, instruction.semantics)


        calls=['CALL','CALLCODE','DELEGATECALL','CALLBLACKBOX','STATICCALL']
        if mnemonic in calls:
            return self._handle_calls(state, instruction, arguments, result_ref)
        reads=['MLOAD','POP']



m = ManticoreEVM() # initiate the blockchain

ucec_detector=DetectUncheckedExternalCall()
m.register_plugin(ucec_detector)




contract='contract.sol'
with open(contract,'rb') as f:
    contract_src=f.read()

########################################
# Create some accounts
########################################

user_account_balance=1000
user_account=m.create_account(balance=user_account_balance)


########################################
# Create representation of the contract
########################################

# The contract's constructor gets invoked here.
contract_account=m.solidity_create_contract(contract_src,
                                            owner=user_account)


########################################
# Do some stuff with the contract
########################################


m.transaction(caller=user_account,address=contract_account, value=m.SValue, data=m.SByte(164))


# m.finalize()

########################################
# Do some checking
########################################

for state in m.all_states:
    print "getting report"
    print ucec_detector.get_findings(state)
