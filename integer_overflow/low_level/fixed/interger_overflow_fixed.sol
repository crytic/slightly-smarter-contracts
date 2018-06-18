contract Overflow {
  uint private sellerBalance=0;

  function add(uint value) public returns (bool){
    assert(overflow_uint_add(sellerBalance,value)==false);

    sellerBalance += value; // possible overflow

  }

  function overflow_uint_add(uint lhs, uint rhs) public pure returns (bool){
    //Check that doesn't overflow
    ~lhs > rhs;
  }

  function safe_add(uint value) public returns (bool){
    //Integer overflow, but as part of a check
    require(value + sellerBalance >= sellerBalance);
    sellerBalance += value;
  }
}
