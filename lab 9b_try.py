# lab 9b
import numpy as np

class Agent:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def move(self, empty_spaces):
        if empty_spaces:  # Check if there are any empty spaces available
            self.x, self.y = empty_spaces.pop(0)  # Move the agent to the first available empty space

class World:
    def __init__(self, size, num_agents):
        self.size = size
        self.grid = np.full((size, size), None)  # Initialize grid as None
        self.agents = []
        for i in range(num_agents):
            while True:
                x, y = np.random.randint(0, size, size=2)
                if self.grid[x, y] is None:
                    self.grid[x, y] = i
                    self.agents.append(Agent(i, x, y))
                    break

    def find_empty_patches(self):
        empty_spaces = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i, j] is None]
        return empty_spaces

    def run_simulation(self, steps):
        for _ in range(steps):
            empty_spaces = self.find_empty_patches()
            for agent in self.agents:
                agent.move(empty_spaces)
            # Add more detailed simulation behavior here if needed

# Simulation parameters
world_size = 10  # Small grid
num_agents = 5   # Small number of agents
simulation_steps = 10  # Small number of loops

# Initialize and run the world
world = World(world_size, num_agents)
world.run_simulation(simulation_steps)
