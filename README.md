# Hackchallenges with Carla Simulation

In this repository we collect the content and instruction for the hackchallenge around the Carla simulation

## Setup of Carla simulation environment

For the following two Hack ideas we rely on the simulation with [Carla](carla.org).

## Routing and Map Challenge

## Getting VSS-Data Challenge

Carla allows to interact with the simulation through a [Python API](https://carla.readthedocs.io/en/latest/python_api/) which allows to extract telemetry data about a specific vehicle in the simulation. So one can use this API to get data for other applications which are then controlled and influenced by the simulation. The [Velocitas project](https://eclipse-velocitas.github.io/velocitas-docs/) enables the development of Vehicle specific apps. Part of this approach is to consume the vehicle specific data from the [Kuksa.val Data Broker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) which abstracts the specifics of the vehicle internal data sources and sinks by using the data model of the [Vehicle Signal Specification (VSS)](https://covesa.github.io/vehicle_signal_specification/). 

One benefit of using the same data model in the Velocitas-App for consuming vehicle specific data is that one can easily port the application from the simulation environment to a vehicle which provides data in the same format.

So to realize a use case by writting a Velocitas-App, you need to find a way to consume the data from the Carla simulation, convert it to VSS, and then write it into the Kuksa Data Broker from which the Velocitas-App can then gets its data. 

