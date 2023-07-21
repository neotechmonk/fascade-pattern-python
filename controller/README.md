Fascade hides low level implementation details from the usage 



### Code smell
* Low level packages are well organised for single respondibilities 
* `main.py`'s GUI is orchestrating View and Logic function (low cohesion)
* Further it accesses a lot low level packages through a monolithic single class 


### Improvements Made
1. Separate `main.py` into `gui.py` and `main.py`
1. seperate logic from `main.py` into `iot_controllers.py` by refactoring `display_status`(`get_status`)  and `toggle`(`power_speaker`) 
1. Change `SmartApp` contruction to get `get_status()` and `power_speaker()`