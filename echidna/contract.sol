contract Contract {
  uint sum1=0;
  uint sum2=0;
  uint sum3=0;

  uint8 constant magic1 = 1;
  uint8 constant magic2 = 2;
  uint8 constant magic3 = 3;

  function reset() public{
    sum1=0;
    sum2=0;
    sum3=0;
  }

  function get_bit(uint val, uint8 bit) public pure returns(uint){
    uint mask= uint(1) << bit;
    return (val & mask)>>bit;
  }

  function mysterious_function(uint a) public{
    uint var1 = uint(keccak256(a));
    uint var2 = uint(sha256(a));
    uint var3 = uint(ripemd160(a));


    sum1 += get_bit(var1, magic1);
    sum2 += get_bit(var2, magic2);
    sum3 += get_bit(var3, magic3);
  }


  function classify() public view returns (uint){
    if(sum1==8){
      return 1;
    }

    if(sum2==17){
      return 2;
    }

    if(sum3==19){
      return 3;
    }

    if(sum2==1 && sum3==2 ){
      return 5;
    }

    if(sum1==7 && sum2==12){
      return 6;
    }

    if(sum1==3 && sum3==9){
      return 7;
    }

    if(sum1==1 && sum2==2 && sum3==3){
      return 4;
    }

    if(sum1==3 &&sum2==2 &&sum3==1 ){
      return 8;
    }

    if(sum1==6 &&sum2==6 &&sum3==6 ){
      return 9;
    }

  }

  function echidna_do_check() public view returns (bool){

    return true;
  }


}
