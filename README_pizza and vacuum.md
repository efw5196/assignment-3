# Models Documentation

## Overview
This documentation describes the functionality and usage of the PizzaBuilder and VacuumAgent models.

## PizzaBuilder
This model allows the creation of different pizzas based on declarative memory.

### Usage
1. Initialize the PizzaBuilder.
2. Add different types of pizzas and their ingredients to the memory.
3. Create pizzas based on the type.

## VacuumAgent
This model represents an agent that can detect dirty blocks, remember their locations, and clean them.

### Usage
1. Initialize the VacuumAgent.
2. Detect and store dirty blocks.
3. Move to and clean the stored dirty blocks.

## Possible Issues
- VacuumAgent does not handle obstacles.
- PizzaBuilder does not verify the validity of ingredients.
