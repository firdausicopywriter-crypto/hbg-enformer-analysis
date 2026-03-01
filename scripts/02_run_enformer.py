
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from pyfaidx import Fasta

# Load Enformer
enformer = hub.load("https://tfhub.dev/deepmind/enformer/1").model
print("Enformer loaded successfully!")

# One-hot encode DNA sequence
def one_hot_encode(sequence):
    seq = sequence.upper()
    mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    one_hot = np.zeros((len(seq), 4), dtype=np.float32)
    for i, nucleotide in enumerate(seq):
        if nucleotide in mapping:
            one_hot[i, mapping[nucleotide]] = 1
    return one_hot

# Load sequence
genome = Fasta('hg38.fa')
chrom = 'chr11'
gene_center = 5269000
sequence_length = 393216
start = gene_center - sequence_length // 2
end = start + sequence_length
sequence = str(genome[chrom][start:end]).upper()

# Encode and predict
seq_one_hot = one_hot_encode(sequence)
seq_one_hot = seq_one_hot[np.newaxis, ...]
print("Running Enformer prediction...")
predictions = enformer.predict_on_batch(seq_one_hot)
human_predictions = predictions['human'][0]
print(f"Success! Predictions shape: {human_predictions.shape}")

# Save results
np.save('results/hbg1_predictions.npy', human_predictions)
print("Results saved!")
