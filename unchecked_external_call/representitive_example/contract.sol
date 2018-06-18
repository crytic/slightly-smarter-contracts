pragma solidity ^0.4.1;
contract UncheckedCall{

    function something_somewhere(uint something){
      bool a=msg.sender.send(something);
      }
}
