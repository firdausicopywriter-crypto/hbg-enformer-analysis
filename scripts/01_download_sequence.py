from pyfaidx import Fasta
import numpy as np

# Load genome
genome = Fasta('hg38.fa')

# HBG1 gene location
chrom = 'chr11'
gene_center = 5269000

# Enformer needs 393,216 bp
sequence_length = 393216
start = gene_center - sequence_length // 2
end = start + sequence_length

# Extract sequence
sequence = str(genome[chrom][start:end]).upper()
print(f"Extracted {len(sequence)}
