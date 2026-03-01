import numpy as np
import matplotlib.pyplot as plt

# Load predictions
human_predictions = np.load('results/hbg1_predictions.npy')

# Plot regulatory landscape
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(human_predictions[:, 500], linewidth=2, label='H3K27ac (enhancers)')
ax.axvline(x=448, color='red', linestyle='--', linewidth=2, label='HBG1 center')
ax.plot(539, 0.661, 'ro', markersize=12, label='Strongest enhancer')
ax.set_xlabel('Genomic Position (bins)')
ax.set_ylabel('H3K27ac Signal')
ax.set_title('HBG1 Regulatory Landscape')
ax.legend()
plt.savefig('results/hbg1_regulatory_landscape.png', dpi=150)
print("Plot saved!")
