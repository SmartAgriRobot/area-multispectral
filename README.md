# Area Multispectral
Multispectral imaging captures image data within specific wavelength ranges across the electromagnetic spectrum. The wavelengths may be separated by filters or detected with the use of instruments that are sensitive to particular wavelengths

## Features
* Live NDVI Image

## Installation
```
sudo apt update
sudo apt install python3-pip python3-gpiozero python3-serial \
	python3-opencv python3-numpy python3-matplotlib python3-sklearn \
	python3-sklearn-lib libx264-dev libjpeg-dev libgstreamer1.0-dev \
	libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev \
	gstreamer1.0-plugins-ugly gstreamer1.0-tools gstreamer1.0-gl gstreamer1.0-gtk3
```
## Compatibility
### Hardware :
* Raspberry Pi Zero 2 W
* Raspberry Pi IR-CUT Camera

### Software :
* Raspberry Pi OS (Bullseye)
* Python 3

## Usage
```
git clone https://github.com/SmartAgriRobot/area-multispectral.git
cd area-multispectral
cd sourcecode
python3 main.py
```
## Video Guide
[SmartAgriRobot Channel](https://www.youtube.com/channel/UCOgiOXJ43hnMZIsxGAZKoPQ)

## Folder structure
| Folder Name  | detail  |
| :------------ |:---------------|
| 3d            | STL file part for 3d printer |
| clip          | Operation video clip       |
| images        | Images of prototype        |
| pdf           | Specification document        |
| sourcecode    | Python source code        |

## License and Credits
The Area Multispectral is released under the MIT license.

## Disclaimer
This source and the whole package comes without warranty. It may or may not harm your computer or cell phone. Please use with care. Any damage cannot be related back to the author. The source has been tested on a virtual environment and scanned for viruses and has passed all tests.
