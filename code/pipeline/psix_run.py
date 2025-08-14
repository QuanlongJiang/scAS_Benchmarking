import pandas as pd
import psix

# Parameters definition
cell_list_path = 'result/psix/dataset1/cell_list_file.tab'  # e.g. 'dataset1/cell_list_file.tab'
tpm_matrix_path = 'result/psix/dataset1/tpm_matrix.tab'     # e.g. 'dataset1/tpm_matrix.tab'
sj_raw_dir = 'result/dataset1/StarSolo_mapping/dataset1_StarSolo_mapping/SJ/raw'                   # e.g. 'dataset1/SJ/raw'
intron_annotation_file = 'genome/gencode_v31.tab.gz'  # e.g. 'genome/gencode_v31.tab.gz'
output_dir = 'result/psix/dataset1/'                   # e.g. 'dataset1/output/'

# Filtering parameters
min_jr = 1
min_psi = 0.0
min_observed = 0.01
min_cell = 1
solo = True

# Load cell list from file
cell_list = pd.read_table(cell_list_path, index_col=0).index.to_list()

# Load TPM matrix
df = pd.read_table(tpm_matrix_path)
df['gene_id'] = [gene.split('.')[0] for gene in df['gene_id']]

# Initialize psix object
psix_object = psix.Psix()

# Run junctions2psi function with parameters
psix_object.junctions2psi(
    sj_dir=sj_raw_dir,
    intron_file=intron_annotation_file,
    tpm_file=tpm_matrix_path,
    save_files_in=output_dir,
    cell_list=cell_list,
    minJR=min_jr,
    minPsi=min_psi,
    min_observed=min_observed,
    minCell=min_cell,
    solo=solo
)
