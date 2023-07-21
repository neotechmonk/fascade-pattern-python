Fascade hides low level implementation details from the usage 



### Code smell
* Low level packages are well organised for single respondibilities 
* `main.py`'s GUI is orchestrating View and Logic function (low cohesion)
* Further it accesses a lot low level packages through a monolithic single class 


### Improvements Made
1. Separate `main.py` into `gui.py` and `main.py`
1. seperate logic from `main.py` into `iot_controllers.py` by refactoring `display_status`(`get_status`)  and `toggle`(`power_speaker`) 
1. Change `SmartApp` contructor to get `get_status()` and `power_speaker()`
1. Refactor controller related logging from `gui.py`
1. Refactor `toggle()` and `display_status()` to use the `iot_controller.py` functions
1. create a Fascade class and copy over controller functions from `iot_controller.py` for further refactoring. 
1. refactor `main.py` to deal with lower level details using the Fascade class 
