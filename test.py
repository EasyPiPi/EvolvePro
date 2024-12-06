#### test scripts on local computer

from evolvepro.src.process import generate_wt, generate_single_aa_mutants
generate_wt('MNTINIAKNDFS', 'output_path/dataset_WT.fasta')
generate_single_aa_mutants('output_path/dataset_WT.fasta', 'output_path/dataset.fasta')

from evolvepro.src.process import process_dataset
process_dataset(
    file_path='output/Source.xlsx',
    dataset_name='dataset_WT',
    wt_fasta_path='output_path/dataset_WT.fasta',
    activity_column='DMS_SCH',
    cutoff_value=2.5,
    output_dir='output/dms',
    sheet_name='MAPK1',
    cutoff_rule='greater_than',
    cutoff_percentiles=[90, 95]
)

# this works
python evolvepro/plm/esm/extract.py esm1b_t33_650M_UR50S /content/output/kelsic.fasta /content/output/kelsic_esm1b_t33_650M_UR50S --toks_per_batch 512 --include mean --concatenate_dir /content/output

# this doesn't work, maybe too large?
python evolvepro/plm/esm/extract.py esm2_t48_15B_UR50D /content/output/kelsic.fasta /content/output/kelsic_esm2_t48_15B_UR50D --toks_per_batch 512 --include mean --concatenate_dir /content/output

# this works, larger model but smaller dataset
python evolvepro/plm/esm/extract.py esm2_t48_15B_UR50D output_path/dataset.fasta output_path/dataset_esm2_t48_15B_UR50D --toks_per_batch 512 --include mean --concatenate_dir output_path

#### test scripts on server ####
# Process
from evolvepro.src.process import generate_wt, generate_single_aa_mutants
generate_wt('MAKEDNIEMQGTVLETLPNTMFRVELENGHVVTAHISGKMRKNYIRILTGDKVTVELTPYDLSKGRIVFRSR', output_file='output/kelsic_WT.fasta')
generate_single_aa_mutants('output/kelsic_WT.fasta', output_file='output/kelsic.fasta')

from evolvepro.src.process import suggest_initial_mutants
suggest_initial_mutants('output/kelsic.fasta', num_mutants=12, random_seed=42)

# PLM
python evolvepro/plm/esm/extract.py esm1b_t33_650M_UR50S output/kelsic.fasta output/kelsic_esm1b_t33_650M_UR50S --toks_per_batch 512 --include mean --concatenate_dir output

python evolvepro/plm/esm/extract.py esm2_t48_15B_UR50D output/kelsic.fasta output/kelsic_esm2_t48_15B_UR50D --toks_per_batch 512 --include mean --concatenate_dir output

## Run EVOLVEpro
from evolvepro.src.evolve import evolve_experimental

protein_name = 'kelsic'
embeddings_base_path = 'output'
# embeddings_file_name = 'kelsic_esm1b_t33_650M_UR50S.csv'
embeddings_file_name = 'kelsic_esm2_t48_15B_UR50D.csv'
round_base_path = 'colab/rounds_data'
wt_fasta_path = "output/kelsic_WT.fasta"
number_of_variants = 12
output_dir = 'output/'
rename_WT = False

round_name = 'Round1'
round_file_names = ['kelsic_Round1.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

round_name = 'Round2'
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

round_name = 'Round3'
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx', 'kelsic_Round3.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

round_name = 'Round4'
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx', 'kelsic_Round3.xlsx', 'kelsic_Round4.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

round_name = 'Round5'
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx', 'kelsic_Round3.xlsx', 'kelsic_Round4.xlsx', 'kelsic_Round5.xlsx']

this_round_variants, df_test, df_sorted_all = evolve_experimental(
    protein_name,
    round_name,
    embeddings_base_path,
    embeddings_file_name,
    round_base_path,
    round_file_names,
    wt_fasta_path,
    rename_WT,
    number_of_variants,
    output_dir
)

from evolvepro.src.plot import read_exp_data, plot_variants_by_iteration

round_base_path = 'colab/rounds_data'
round_file_names = ['kelsic_Round1.xlsx', 'kelsic_Round2.xlsx', 'kelsic_Round3.xlsx', 'kelsic_Round4.xlsx', 'kelsic_Round5.xlsx']
wt_fasta_path = "output/kelsic_WT.fasta"

df = read_exp_data(round_base_path, round_file_names, wt_fasta_path)
plot_variants_by_iteration(df, activity_column='activity', output_dir=output_dir, output_file="kelsic")
