Fascade hides low level implementation details from the usage 



### Code smell
* Low level packages are well organised for single respondibilities 
* `main.py`'s GUI is orchestrating View and Logic function (low cohesion)
* Further it accesses a lot low level packages through a monolithic single class 


### Improvements Made
1. 