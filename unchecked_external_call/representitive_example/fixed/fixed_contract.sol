
contract UncheckedCall{
  function something_somewhere(uint something){
    bool a=msg.sender.send(something);
    if(a==false){
      revert();
    }
  }
}
