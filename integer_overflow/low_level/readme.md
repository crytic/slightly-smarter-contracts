# Low Level Integer Overflow Detection

Sometimes bad states can't be discovered by interpreting calls to a contract. Here, the `sellerBalance` variable is private and therefore has no getter. To get around this limitation we can move our analysis directly onto the EVM bytecode with a `Detector` plugin.
