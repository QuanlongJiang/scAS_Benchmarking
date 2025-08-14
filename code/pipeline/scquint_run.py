from scquint.data import load_adata_from_starsolo, add_gene_annotation, group_introns
from scquint.data import filter_min_cells_per_feature, filter_min_cells_per_intron_group, calculate_PSI
from scquint.differential_splicing import run_differential_splicing, run_differential_splicing_for_each_group, find_marker_introns, mask_PSI
from scquint.dimensionality_reduction.pca import run_pca

import scanpy as sc
import pandas as pd
import numpy as np

import scquint


starloso_raw_path = "result/dataset1/StarSolo_mapping/dataset1_StarSolo_mapping/SJ/raw"
gtf_annotation_path = "genome/gencode.v31/gencode.v31.annotation.gtf"
output_raw_h5ad = "result/scquint/dataset1.h5ad"
output_filtered_h5ad = "result/scquint/dataset1.filtered.h5ad"
min_cells_ratio = 0.05  # Filtering threshold: 5% of total cells

# Load data from StarSolo output directory
adata = load_adata_from_starsolo(path=starloso_raw_path)

# Add gene annotation from GTF file
adata = add_gene_annotation(adata=adata, gtf_path=gtf_annotation_path)

# Group introns by 3' splice site
adata = group_introns(adata=adata, by="three_prime")
print("adata shape after grouping introns:", adata.shape)

# Calculate PSI values with smoothing and without smoothing
adata.layers["PSI_smooth"] = calculate_PSI(adata=adata, smooth=True)
adata.layers["PSI_raw"] = calculate_PSI(adata=adata, smooth=False)

# Save intermediate results
adata.write_h5ad(output_raw_h5ad)

# Calculate minimum cells threshold for filtering
num_cells = adata.shape[0]
min_cells_threshold = int(num_cells * min_cells_ratio)

# Filter features and intron groups by minimum cells
adata = filter_min_cells_per_feature(adata=adata, min_cells=min_cells_threshold)
adata = filter_min_cells_per_intron_group(adata=adata, min_cells=min_cells_threshold)
print("adata shape after filtering:", adata.shape)

# Save filtered data
adata.write_h5ad(output_filtered_h5ad)