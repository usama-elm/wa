# Morphogenesis

There is a series of PDE that can model the patterns of animals and fishes. In an old TIPE project the objective was to take a picture of a fish (or another few select animals) and to extract the pattern, create a database of variables and linked patterns so we could output the variables of the fish.

Due to time contraints and moving the project was never finished. I recovered an old presentation and a few code snippets from which I will rebuild the project again.

## Objectives
- You input a fish image
- It isolates the fish and its patterns
- It calculates a sort of hash, that it will compare to the nearest hash in a database already created
- Outputs the exact variables to use in the Gray-Scott formula (OPTIONAL: It gives the type of fish)
- Optional: Create a website where you can input the image and it gives you the result, and also lets you play with the Gray-Scott formula (using WASM or WebGP)