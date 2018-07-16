contract Simple {
  function f(uint a) payable public returns(uint){
    uint b=0;
    uint counter=0;
    while(counter<a){
      b+=1;
      counter+=1;
    }
    return b;
  }
}
