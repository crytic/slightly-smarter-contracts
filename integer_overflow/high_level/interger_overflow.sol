

contract Overflow {
  uint public sellerBalance=0;

  function add(uint value) returns (bool){
    sellerBalance += value; // possible overflow
  }

}
