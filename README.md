# Emergency Room Simulation

<a href='https://raw.githubusercontent.com/vivibui/Emergency-Room-Simulation/main/Architecture/ModuleArchitecture.png'><img src='https://img.shields.io/badge/Architecture-View-Green'></a>  <a href='https://github.com/vivibui/Emergency-Room-Simulation/blob/main/VivianBui_ERSimulation.pdf'><img src='https://img.shields.io/badge/Paper-PDF-red'></a>

**Emergency Room Simulation** 
This is a simulation that replicates the operation of an emergency room. We develop and test results of different algorithms in prioritizing waiting patients to receive treatment in different context of congestions in the ER. 

## Demo
[![SETUP](https://github.com/vivibui/Emergency-Room-Simulation/blob/main/thumbnail.png)(https://www.youtube.com/watch?v=PPtSiwGfgzM)

## Process Data and Visualize Results
The folder Process and Visualize includes Rmarkdown files that are used to process and visualize results as seen in the paper. Detailed instruction can be found in the files. Make sure you have RStudio to open and execute the files. 

## Problem Setup
At the beginning of the simulation, the emergency room will be allocated a predetermined number of un-occupied beds for new patients. Every hour, a stochastic number of patients will arrive at the ER and require bed assignments. Upon arrival, each patient will undergo a triage process and will then be placed into a waiting queue. If a bed becomes available, a waiting patient who has been prioritized according to the selected algorithm will be assigned to the bed. Subsequently, after a duration of time has elapsed in the emergency bed, the treated patient will vacate the bed, making it available for the next waiting patient. The simulation will cease after running for the designated number of days as per the assignment.

**Treatment as Bed Assignment.** In our simulation, it is important to clarify that the assignment of an emergency bed encompasses three key components: (1) the receipt of necessary scanning procedures, (2) consultation with a doctor, and (3) receipt of treatment. We operate under the assumption that all incoming patients will require a bed, and we interchangeably utilize the terms “discharged” and “treated” to denote patients who have completed their stay in the ER. Accordingly, the term “discharge” includes any other potential outcomes that a patient may experience subsequent to their stay in the ER.

**All Patients are Approximately Unique.** All attributes pertaining to an incoming patient in our simulation are randomly generated, resulting in each patient being essentially unique. It should be noted that there may or may not be instances of “revisiting” patients, although the current version of the simulation does not account for such similarities in patient attributes.

**Assumption of Triage.** An acute level will be randomly assigned to a new patient as a way to simulate the result of triage without the need of detailing the entire triage process. Furthermore, we assume that since the first evaluation of triage, the patient’s medical condition will remain unchanged during the waiting period until they are seen by a doctor. In other words, the patient’s condition is assumed to neither improve nor deteriorate while waiting for medical attention which affects the triage result.

**Calculation of Wait Time.** Wait time calculation for a patient starts after triage has occurred and stops immediately at the time received a bed.

**Left Without Being Seen as the Floor and Ceiling Function.** The “Left Without Being Seen” (LWBS) feature in our simulation allows for customization by assuming that a patient will leave the emergency room if their wait time exceeds a predefined maximum benchmark. 

**Levels of Overcrowding.** There is no universal or national metric to measure the level of crowding in emergency departments. The estimation of “High”, “Medium”, and “Low” level of overcrowding, in fact, is made in relation to the rate of LWBS patients. As we are interested in observing how the algorithms behave in extreme overcrowding scenarios, we configure the initial conditions in a way that will result in the LWBS rate at least equal to or larger than the provided clinical data. The results are then divided into three scenarios, where the difference between levels justifies the smaller percentage of overall LWBS patients across algorithms.

For more detailed, please refer to the [Whitepaper](https://github.com/vivibui/Emergency-Room-Simulation/blob/main/VivianBui_ERSimulation.pdf)
