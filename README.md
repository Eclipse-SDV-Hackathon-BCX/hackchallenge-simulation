
# Eclipse SDV Hackathon on BCX2022

One-Pager ([PowerPoint](./assets/BCX_Onepager_Virtual_Vehicle_Application(with_simulation).pptx), [PDF](./assets/BCX_Onepager_Virtual_Vehicle_Application(with_simulation).jpg))

# Welcome to the "Virtual Vehicle Application with Simulation" hack challenge!

## Hackchallenges - Building In-Vehicle Applications with telemetry from Carla and AirSim Simulation

In this repository we collect the content and instruction for the hackchallenge around building in-vehicle applications using telemetry data generated with simulation tools. 

As a hack challenge for Eclipse SDV, you will have the opportunity to get involved with the technology and experience some of the challenges when dealing with connected vehicles and build the next generation of software defined vehicles. You will also get to know a few more open source projects along the way.

For this hackchallenge we considered 2 simulation tools, Carla and AirSim although you are not restricted to only these. If you have experience with other simulation tools and have a great idea on how to use it in this hackchallenge please do so.

## Architecture

![](assets/Virtual_Vehicle_Application_Architecture(1).png)
![](assets/Virtual_Vehicle_Application_Architecture(2).png)

## Bill of Material (tl;dr;)

To complete the hack challenge depicted in the architecture slide you need the following content and repositories available on your machine:

- **Simulation Environment (one of the below)**:
    - Carla: Setup Instruction as described in the ["Let’s Play OpenStreepMap and CARLA"](https://github.com/Eclipse-SDV-Hackathon-BCX/hackchallenge-lets-play-osm-and-carla/blob/main/docs/step-1-first-contact.md) documentation)
    - Airsim: Setup Instructions and Binaries as described in [precompiled binaries](https://github.com/Microsoft/AirSim/releases)
- **Kuksa Data Broker (on of the below)**:
    - [Kuksa.val GitHub](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker#build-and-run-databroker)
    - [Kuksa.val Data Broker Docker Container](https://github.com/eclipse/kuksa.val/pkgs/container/kuksa.val%2Fdatabroker)
- **Chariott Application Programming Model**:
    - [Chariott](https://github.com/eclipse/chariott)
- **Fork of Velocitas Template Repository for your application**
    - [Velocitas Template Repository](https://github.com/eclipse-velocitas/vehicle-app-python-template)
    - [Velocitas Quickstart Documentation](https://eclipse-velocitas.github.io/velocitas-docs/docs/tutorials/quickstart/)
 
## Setup of simulation environment

Both Carla and AirSim require a GPU in order to run. 

If your computer does not have a GPU, you can setup an [GPU optimized virtual machine on Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes-gpu). We have pre-tested both Carla and AirSim on [NVv4-series](https://learn.microsoft.com/en-us/azure/virtual-machines/nvv4-series).

Each hack challenge team have access to an Azure Pass to use during the Hackathon. Talk to your hack coach to get yours.
You will need to activate it before you can use. See [Redeeming a Microsoft Azure Pass Promo Code](https://www.microsoftazurepass.com/Home/HowTo?Length=5).

### Link and Information about Carla simulation environment

You can find detailed information about [Carla](carla.org).

### Link and Information about AirSim simulation environment

AirSim is a simulator for drones, cars and more, built on Unreal Engine (we now also have an experimental Unity release). It is open-source, cross platform, and supports software-in-the-loop simulation with popular flight controllers such as PX4 & ArduPilot and hardware-in-loop with PX4 for physically and visually realistic simulations. It is developed as an Unreal plugin that can simply be dropped into any Unreal environment. Similarly, we have an experimental release for a Unity plugin.

In this hack challenge you will use it to generate telemetry data. See [Your mission](#Your-mission-should-you-choose-to-accept-it) 

Although you can setup your own Unreal environment, we recommend you to download one of the [precompiled binaries](https://github.com/Microsoft/AirSim/releases) and run to get started immediately.

You can find more about [AirSim](https://microsoft.github.io/AirSim/).

## Links and Information about Eclipse Software Defined Vehicle Projects

* The Eclipse Chariott project aims to simplify and enhance in-vehicle software developer productivity by providing a metadata-driven middleware/abstraction layer that allows modern application programming models to target in-vehicle functions through a digital representation of vehicle state and capabilities and provides an extensible and dynamic architecture to access the vehicle hardware and sensors.
You can find additional information here [Chariott](https://github.com/eclipse/chariott)

* KUKSA.val provides software components for working with in-vehicle signals modelled using the [COVESA VSS data model](https://covesa.github.io/vehicle_signal_specification/).
You can find additional information here [Kuksa.val](https://github.com/eclipse/kuksa.val)

* Eclipse Velocitas provides a development toolchain to create containerized in-vehicle applications (Vehicle Apps) that offers a comfortable, fast and efficient development experience to increase the velocity of a development team. 
You can find additional information here [Velocitas](https://github.com/eclipse-velocitas) 

## Your mission, should you choose to accept it...

Carla and AirSim allows to interact with the simulation through data recording and API's.  

AirSim has a [Recording](https://microsoft.github.io/AirSim/settings/#recording) feature to easily collect data and images. The [Recording APIs](https://microsoft.github.io/AirSim/apis/#recording-apis) also allows starting and stopping the recording using API.

The Carla [Python API](https://carla.readthedocs.io/en/latest/python_api/) allows to extract telemetry data about a specific vehicle in the simulation. 

So one can use both methods to get data for other applications which are then controlled and influenced by the simulation. 

Part of this approach is to consume the vehicle specific data in your application from the [Kuksa.val Data Broker](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker) which abstracts the specifics of the vehicle internal data sources and sinks by using the data model of the [Vehicle Signal Specification (VSS)](https://covesa.github.io/vehicle_signal_specification/).

The [Velocitas project](https://eclipse-velocitas.github.io/velocitas-docs/) enables the development of Vehicle specific apps. By integrating with the [Chariott project](https://github.com/eclipse/chariott), a modern application programming model built on [Rust](https://www.rust-lang.org/), it exposes a gRPC service that provides a common interface for interacting with applications and vehicle hardware, enabling application lifecycle management between applications and the vehicle.

The [Dog Mode Application](https://github.com/eclipse/chariott/blob/main/examples/applications/README.md) is an example of such an in-vehicle application built with Chariott.   

One benefit of using the same data model in the Velocitas-App for consuming vehicle specific data is that one can easily port the application from the simulation environment to a vehicle which provides data in the same format.

So to realize a use case by writing a Velocitas/Chariott Application, you need to find a way to consume the data from the Carla and/or AirSim simulation, convert it to VSS, and then write it into the Kuksa Data Broker from which the Velocitas/Chariott Application can then consume and use. 

### interacting with Kuksa.val

As mentioned above the Kuksa.val project provides artifacts for handling and storing in-vehicle data based on the COVESA VSS specification. The idea is to abstract the specifics of the deeply-embedded part within a vehicle for other applications which consume the data from Kuksa.val. To enable this, one needs so-called ["Feeders"](https://github.com/eclipse/kuksa.val.feeders) which convert the data from the embedded systems (e.g., CAN or SOME/IP) to VSS, write it into the Kuksa.val data broker, and vice-versa. 

Part of this challenge is to write a custom feeder for transfering data being relevant for your application between the simulation and the Kuksa.val data broker. One can access the data broker through a [gRPC API](https://github.com/eclipse/kuksa.val/tree/master/kuksa_databroker#test-the-broker---run-clientcli) which allows to [subscribe with specific queries](https://github.com/eclipse/kuksa.val/blob/master/kuksa_databroker/doc/QUERY.md). 

Note, that an alternative approach achiving a similar goal would be to use the Kuksa.val server. However, for the remainder of this hack challenge we focus on the Kuksa.val data broker since it is part of the default Velocitas Dev-Container. 

## This README will self-destruct in five seconds. Good luck.