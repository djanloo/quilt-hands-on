# PARAMETERS FOLDERS
This folder contains data and configuration files for the simulation. 
The file position and name are not mandatory, as they are specified in the python script.

## Spiking network config files (spiking_data/spiking_config)

These are [YAML](https://it.wikipedia.org/wiki/YAML) files for the parameters (description is inside)

- **neurons.yaml**: defines neuron properties (membrane capacity, recovery variables etc.)
- **network.yaml**: defines network properties (weights in nS of the synapses, connectivity, etc.)
- **parametric.yaml**: defines the parametric dependencies (i.e. dopamine modulation)

## Neural mass & sensor data (brain data)

Here is contained an heterogeneous mixture of stuff:

- **Connectivity**: the connectivity between neural masses (weights, delays)
- **Sensors**: data about the EEG (channels, channel position etc)
- **Lead Field Matrices**: neural mass activity to EEG
- **Surfaces**: the ~16k vertices surface of the cortex from TVB
- **Mappings**: geodesic-distance-fro-centroid mapping of the surface vertices

NOTE: not all these data are necessary for a proper simulation. During the thesis I collapsed Surface data, Lead field data and region mapping to a single "Node Lead Field Matrix", that gives the EEG starting from the dynamics of the neural mass network (`nlfm_pahological.pkl`).


## Supersynapses config files (spiking_data/supsyn_config)

Again [YAML](https://it.wikipedia.org/wiki/YAML) files for configuring the supersynapses (fancy name given by L.G.A. for a Inhomogeneous Poisson Process linked to the collective rate of a group of neural masses).

- **supersynapses.yaml**: declares the supersynapses and their properties (synaptic strength and other technical stuff)
- **suspsyn_connectivity.yaml**: defines the connectivity of each supersynapse with the neural masses

