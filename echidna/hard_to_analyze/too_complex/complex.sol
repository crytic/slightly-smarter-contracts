contract complex{
  uint sum=0;
  function inc()public{
    sum+=1;
  }
  function dec()public{
    sum-=1;
  }

  function echidna_check()public returns(bool){
    return sum!=11;
  }

}
