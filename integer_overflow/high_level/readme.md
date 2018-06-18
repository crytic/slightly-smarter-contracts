# High Level Integer Overflow Detection

This contract has a straightforward integer overflow that makes it possible for the `sellerBalance` to wrap back to zero. Is it possible to detect this bad state by observing function returns?
