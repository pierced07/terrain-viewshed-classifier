import numpy as np

def generate_synthetic_terrain(size=256, seed=42):
    """Generates realistic terrain with hills, valleys, and flat regions"""
    rng = np.random.default_rng(seed)
    terrain = np.zeros((size, size))
    
    # Base large-scale features (mountains/hills)
    for _ in range(5):
        cx, cy = rng.integers(0, size, 2)
        radius = rng.integers(30, 80)
        amplitude = rng.uniform(30, 60)
        
        y, x = np.ogrid[:size, :size]
        dist = np.sqrt((x - cx)**2 + (y - cy)**2)
        terrain += amplitude * np.exp(-dist**2 / (2 * radius**2))
    
    # Add medium-scale variation
    for _ in range(10):
        cx, cy = rng.integers(0, size, 2)
        radius = rng.integers(10, 30)
        terrain += rng.uniform(-15, 15) * np.exp(-dist**2 / (2 * radius**2))
    
    # Smooth everything
    from scipy.ndimage import gaussian_filter
    terrain = gaussian_filter(terrain, sigma=3)
    
    # Add some flat regions (plains)
    for _ in range(3):
        cx, cy = rng.integers(20, size-20, 2)
        size_flat = rng.integers(20, 40)
        terrain[cy-size_flat:cy+size_flat, cx-size_flat:cx+size_flat] *= 0.3
    
    # Normalize to 0-100m
    t_min, t_max = terrain.min(), terrain.max()
    terrain = (terrain - t_min) / (t_max - t_min) * 100
    
    return terrain