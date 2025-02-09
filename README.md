# Discrete Event Simulation

This project simulates the behavior of an airport over the course of a week to estimate the total time that each of the airport's runways remains idle.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Simulation Details](#simulation-details)
- [Results](#results)
- [License](#license)

## Introduction

Efficient runway utilization is crucial for airport operations. This simulation models airport activities to determine how often runways are unoccupied, providing insights into potential improvements in scheduling and resource allocation.

## Features

- Models airport operations over one week.
- Calculates the total idle time for each runway.
- Provides detailed reports on runway utilization.

## Installation

To run this simulation, ensure you have Python 3.x installed. Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/lorainemg/discrete-event-simulation.git
cd discrete-event-simulation
```

## Usage
Execute the simulation by running the main script. The program reads input parameters from a configuration file and outputs the results to the console:

```bash
python src/simulation.py
```

## Simulation Details

The simulation models various airport operations, including:

- Flight Arrivals and Departures: Scheduled and random events affecting runway usage.
- Runway Maintenance: Periodic maintenance activities that may cause runways to be unavailable.
- Weather Conditions: Randomly generated weather events impacting flight schedules and runway availability.
- The simulation uses discrete-event modeling techniques to accurately represent the sequence and timing of events.

## Results
Upon completion, the simulation provides:

- Total Idle Time per Runway: The cumulative time each runway was unoccupied during the simulation period.
- Utilization Reports: Detailed statistics on runway usage, including peak usage times and potential bottlenecks.

For a comprehensive analysis and discussion of the results, refer to the full report available in the doc directory: [report.pdf](https://github.com/lorainemg/discrete-event-simulation/blob/master/doc/report.pdf).
