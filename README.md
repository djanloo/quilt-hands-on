# Parameters (`spiking_data`, `brain_data`)

These folders contain data and configuration files used by the simulation.  
File names and locations are not fixed, since they are specified directly in the Python scripts.

## Neural mass & sensor data (`brain_data`)

This folder contains a heterogeneous mix of different data types:

- **Connectivity**: connectivity between neural masses (weights, delays)
- **Sensors**: EEG-related information (channels, channel positions, etc.)
- **Lead Field Matrices**: mapping from neural mass activity to EEG signals
- **Surfaces**: cortical surface (~16k vertices) from TVB
- **Mappings**: geodesic-distance-from-centroid mapping of surface vertices

**NOTE:** Not all of these data are required for a valid simulation.  
During my thesis work, surface data, lead field data, and region mappings were collapsed into a single *Node Lead Field Matrix*, which produces EEG signals directly from the neural mass network dynamics (`nlfm_pathological.pkl`).

## Spiking network configuration files (`spiking_data/spiking_config`)

These are [YAML](https://it.wikipedia.org/wiki/YAML) files containing parameter definitions (each file includes its own description):

- **neurons.yaml**: defines neuron properties (membrane capacitance, recovery variables, etc.)
- **network.yaml**: defines network properties (synaptic weights in nS, connectivity, etc.)
- **parametric.yaml**: defines parametric dependencies (e.g. dopamine modulation)

## Supersynapse configuration files (`spiking_data/supsyn_config`)

These are also [YAML](https://it.wikipedia.org/wiki/YAML) files used to configure supersynapses (a term introduced by L.G.A. to indicate an inhomogeneous Poisson process driven by the collective firing rate of a group of neural masses).

- **supersynapses.yaml**: defines supersynapses and their properties (synaptic strength and other technical parameters)
- **supsyn_connectivity.yaml**: defines the connectivity between supersynapses and neural masses
