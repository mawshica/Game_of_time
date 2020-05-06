# Game of Time

This is a simulation of the invention of a future-computing machine in a Conway's game of life environment

## Rules

- Standard Game of life rules apply
- A new cell - M
    - M is considered a live cell
    - M is activated when enough operators are nearby ( neighbours >= 4)
    - When M is activated, it attempts to calculate the future
        - If the future is bright ( there are cells alive in 20 more generations ), nothing happens
        - If the future is bad ( there are no cells alive in 20 more generations ), all surrounding cells will commit suicide

## Conclusion

The Game of life proceeds as usual, until the point of the machine activation.
When the machine M1 is activated it will attempt to calculate the future by invoking the same code that calculates the environment, which contains another machine M2.
This will end in an infinite recursion and ultimately a death of Python by maximum recursion depth.

This program illustrates what happens when future is dependent on now but at the same time we attempt to influence now by the future.