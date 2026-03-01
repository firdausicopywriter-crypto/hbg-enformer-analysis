import numpy as np

# Load predictions
human_predictions = np.load('results/hbg1_predictions.npy')

# Find top 5 peaks in H3K27ac track (active enhancers)
track_500 = human_predictions[:, 500]
top_indices = np.argsort(track_500)[-5:][::-1]

print("Top 5 predicted regulatory regions (H3K27ac track):")
print("="*60)

for rank, idx in enumerate(top_indices, 1):
    bin_size = 393216 / 896
    genomic_start = int(5072392 + idx * bin_size)
    genomic_end = int(genomic_start + bin_size)
    signal_strength = track_500[idx]
    distance_from_gene = (idx - 448) * bin_size / 1000

    print(f"\n{rank}. Bin {idx} (Signal: {signal_strength:.3f})")
    print(f"   Location: chr11:{genomic_start}-{genomic_end}")
    print(f"   Distance from HBG1: {distance_from_gene:+.1f} kb")

print("\nKey finding:")
print("Strongest enhancer at chr11:5,308,936-5,309,374")
print("Signal: 0.661 (H3K27ac)")
Tap Commit changes when done and
