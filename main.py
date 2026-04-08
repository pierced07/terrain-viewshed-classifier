import os
import sys
import numpy as np

# Suppress massive array prints
np.set_printoptions(threshold=10, edgeitems=3)

import perception_core
from src.terrain_generator import generate_synthetic_terrain
from src.visualize import plot_results

def main():
    print("1. Generating terrain...")
    terrain = generate_synthetic_terrain(size=256, seed=42)
    
    print("2. Running C++ viewshed & classifier...")
    obs_x, obs_y = 128, 128
    obs_height = 15.0
    
    terrain_flat = terrain.flatten().tolist()
    
    viewshed_flat = perception_core.compute_viewshed(
        terrain_flat, 256, 256, obs_x, obs_y, obs_height, 80, 360
    )
    classification_flat = perception_core.classify_terrain(
        terrain_flat, 256, 256, 10.0, 30.0
    )
    
    viewshed = np.array(viewshed_flat, dtype=np.float32).reshape(256, 256)
    classification = np.array(classification_flat, dtype=np.int32).reshape(256, 256)
    
    print("3. Plotting results...")
    plot_results(terrain, viewshed, classification, obs_x, obs_y)

if __name__ == "__main__":
    os.makedirs('demo', exist_ok=True)
    main()