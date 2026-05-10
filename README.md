# Machine Workload Optimization

This project implements a workload distribution algorithm to assign manufacturing orders to different machines (A, B, and C) in a way that minimizes the total completion time.

## Overview

The system processes 100,000 randomly generated orders, each with a specific size. For every order, the algorithm calculates the processing time for each machine using specific efficiency formulas and assigns the order to the machine that will finish it earliest, taking into account the current workload.

### Machine Efficiency Formulas

- **Machine A**: Suitable for smaller orders. Time = `0.05 * size^2 + 5`
- **Machine B**: Optimized for medium-sized orders (around 50). Time = `0.1 * (size - 50)^2 + 15`
- **Machine C**: Best for large orders. Time = `(2000 / size) + 10`

## How It Works

1.  **Data Generation**: Generates 100,000 random orders with sizes between 1 and 100 which are saved to `data.csv`.
2.  **Processing**: The script reads the orders and iteratively assigns each one to the machine that offers the earliest finish time (current workload + new processing time).
3.  **Result**: The final assignment, processing time, and completion time for each order are saved to `results.csv`. The total workload for each machine is printed to the console.

## Usage

Run the script using Python:

```bash
python algorithm_project.py
```

## Requirements

- Python 3.x
- pandas
- numpy
