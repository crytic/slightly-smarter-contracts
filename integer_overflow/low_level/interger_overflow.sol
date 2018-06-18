

contract Overflow {
  uint private sellerBalance=0;

  function add(uint value) returns (bool){
    sellerBalance += value; // possible overflow
  }

  function safe_add(uint value) returns (bool){
    require(value + sellerBalance >= sellerBalance);
    sellerBalance += value;
  }
}
