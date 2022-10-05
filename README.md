CVANS-RT is a modular, cross-platform AI inference engine that provides the solid foundations for building decision support systems. It's designed from the ground-up with developers and integrators in mind, providing both high and low interfaces.

![http://docs.cvedia.com/images/system_diagram.png](http://docs.cvedia.com/images/system_diagram.png)

## Supported systems[¶](http://docs.cvedia.com/#supported-systems)

CVEDIA-RT can be deployed directly onto an edge device, ran standalone on a desktop or as a dockerized container in the cloud.

Check the complete list of supported systems and platforms on the left menu.

## Use-cases[¶](http://docs.cvedia.com/#use-cases)

Due to its flexible design, CVEDIA-RT's enables the rapid prototyping and deployment of many types of applications. A few examples are:

- Perimeter security
- Object counting
- Counter UAV
- Part inspection
- Intelligent Traffic Systems

## Core Development：
python3
pyqt5
qdarkstyle
opencv

## Release notes
### Version 2022.1.0
+ Fixed a problem with Tracker not working with WebCam and ScreenCap sources
+ Improved Tracker objects metadata handling.
+ Created and exposed Clear Readahead Queue method to Lua. (It allows using readahead thread together with delays to simulate stream latency)
+ Enabled DirectX ScreenCap plugin on Windows.
+ Improvements on manual FPS mechanism for video sources.
+ Other stability improvements and bugfixes.
