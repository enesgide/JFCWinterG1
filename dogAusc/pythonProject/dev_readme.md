### Vet Sci Dog Auscultation App
* Built in Python 3.12.4
* Required Python Libs
  * tkinter 
  * customtkinter
  * asyncio
  * pygame 
  * bleak 
  * Pillow
  * async_tkinter_loop
* may need "sudo apt install libsdl1.2-dev" "sudo apt install libsdl-mixer1.2-dev" for pygame if you get an import error for libsdl

The application is built using a Model-View-Controller structure for modularity and separation of concerns.
* The Model class handles the business logic
* The View class instantiates the UI elements and binds them to event handling methods
* The Controller class defines these event handling methods and reflects changes to the model and view according to user interaction.

The files are setup as follows:
* DogAuscModel.py - Model
* DogAuscView, DogAuscPopup.py - View
* DogAuscController, PopupController.y - Controller

All of the files are commented and describe the functionality of each class and method.

A potential requirement may be to modify the app to accomodate multiple models. Currently, the app is built to home into and connect to a specific Arduino module, whose UUID and device name can be found in the DogAuscModel and DogAuscController classes. This can be achieved by doing the following (or following a similar line of thinking):
* Create a popup for the connection process.
* Once BleakClient.discover is called, list all of the identified devices in a TK listbox widget.
* Establish a connection with any verified Arduino module (will probably require to have a list of approved model names to refer to)
* The existing disconnection logic should still work for this implementation of connection.
