contract Pointfunction{
  bool always_true=true;

  function foo(uint secret)public{
    if(secret==1997){
      always_true=false;
    }
  }

  function echidna_checker()public returns(bool){
    return always_true;
  }
}
