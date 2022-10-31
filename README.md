# Hackchallenges - Building In-Vehicle Applications with telemetry from Carla and AirSim Simulation

In this repository we collect the content and instruction for the hackchallenge around building in-vehicle applications using telemetry data generated with simulation tools. For this hackchallenge we considered 2 simulation tools, Carla and AirSim although you are not restricted to only these. If you have experience with other simulation tools and have a great idea on how to use it in this hackchallenge please do so.
 
## Setup of simulation environment

Both Carla and AirSim require a GPU in order to run. If your computer does not have a GPU, you can setup an Azure Virtual Machine.  

### Link and Information about Carla simulation environment

You can find detailed information about [Carla](carla.org).

### Link and Information about AirSim simulation environment

You can find detailed information about [AirSim](https://microsoft.github.io/AirSim/).

## Links and Information about Eclipse Software Defined Vehicle Projects

* The Eclipse Chariott project aims to simplify and enhance in-vehicle software developer productivity by providing a metadata-driven middleware/abstraction layer that allows modern application programming models to target in-vehicle functions through a digital representation of vehicle state and capabilities and provides an extensible and dynamic architecture to access the vehicle hardware and sensors.
You can find additional information here [Chariott](https://github.com/eclipse/chariott)

* KUKSA.val provides in-vehicle software components for working with in-vehicle signals modelled using the COVESA VSS data model.
You can find additional information here [Kuksa](https://github.com/eclipse/kuksa.val)

* Eclipse Velocitas provides a development toolchain to create containerized in-vehicle applications (Vehicle Apps) that offers a comfortable, fast and efficient development experience to increase the velocity of a development team. 
You can find additional information here [Velocitas](https://github.com/eclipse-velocitas) 

## Architecture



## Routing and Map Challenge

## Getting VSS-Data Challenge

Carla allows to interact with the simulation through a [Python API](https://carla.readthedocs.io/en/latest/python_api/) which allows to extract telemetry data about a specific vehicle in the simulation. So one can use this API to get data for other applications which are then controlled and influenced by the simulation. The [Velocitas project](https://eclipse-velocitas.github.io/velocitas-docs/) enables the development of Vehicle specific apps. Part of this approach is to consume the vehicle specific data from the [Kuksa.val Data Broker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) which abstracts the specifics of the vehicle internal data sources and sinks by using the data model of the [Vehicle Signal Specification (VSS)](https://covesa.github.io/vehicle_signal_specification/). 

One benefit of using the same data model in the Velocitas-App for consuming vehicle specific data is that one can easily port the application from the simulation environment to a vehicle which provides data in the same format.

So to realize a use case by writting a Velocitas-App, you need to find a way to consume the data from the Carla simulation, convert it to VSS, and then write it into the Kuksa Data Broker from which the Velocitas-App can then gets its data. 

