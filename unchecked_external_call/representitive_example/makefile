all: contract

contract: contract.sol
	solc --bin --bin-runtime --asm --ast-json contract.sol -o out

clean:
	rm -rf out
