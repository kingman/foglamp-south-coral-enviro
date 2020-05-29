# A FogLAMP South plugin for the [Coral Environmental Sensor Board](https://coral.ai/products/environmental)

## Prerequisites
1.  Foglamp installed on the Raspberry Pi
1.  Follow the
    [instructions for installing the Python library](https://coral.withgoogle.com/docs/enviro-board/get-started/#install-the-python-library)
    on the Coral Environmental Sensor Board official page.

## Installation
Run following commands on Raspberry Pi:

    cd "$HOME"
    git clone https://github.com/kingman/foglamp-south-coral-enviro.git
    sudo cp -R "$HOME"/foglamp-south-coral-enviro/python/foglamp/plugins/south/coral-enviro /usr/local/foglamp/python/foglamp/plugins/south/
