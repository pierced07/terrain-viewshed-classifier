import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

def plot_results(terrain, viewshed, classification, obs_x, obs_y):
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # 1. Terrain
    im0 = axes[0].imshow(terrain, cmap='terrain')
    axes[0].plot(obs_y, obs_x, 'r*', markersize=12, label='Observer')
    axes[0].set_title('Terrain Elevation (m)')
    axes[0].axis('off')
    plt.colorbar(im0, ax=axes[0], fraction=0.046, pad=0.04)
    
    # 2. Viewshed
    axes[1].imshow(terrain, cmap='gray', alpha=0.4)
    masked = np.ma.masked_where(viewshed == 0, viewshed)
    axes[1].imshow(masked, cmap='summer', alpha=0.7)
    axes[1].plot(obs_y, obs_x, 'r*', markersize=12)
    axes[1].set_title('Line-of-Sight Viewshed')
    axes[1].axis('off')
    
    # 3. Classification
    cmap = plt.get_cmap('RdYlGn_r', 4)
    im2 = axes[2].imshow(classification, cmap=cmap, vmin=0.5, vmax=3.5)
    axes[2].plot(obs_y, obs_x, 'r*', markersize=12)
    axes[2].set_title('Terrain Classification\n(1:Flat 2:Mod 3:Steep)')
    axes[2].axis('off')
    plt.colorbar(im2, ax=axes[2], fraction=0.046, pad=0.04)
    
    plt.tight_layout()
    plt.savefig('demo/viewshed_output.png', dpi=150, bbox_inches='tight')
    print("Image saved to demo/viewshed_output.png")