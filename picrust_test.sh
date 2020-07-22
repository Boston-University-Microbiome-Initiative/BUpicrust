# python /projectnb/talbot-lab-data/msilver/BUpicrust/create_inputs.py --biom /projectnb/talbot-lab-data/msilver/BU16s/test/intermediate/dada2/table.qza --seqs /projectnb/talbot-lab-data/msilver/BU16s/test/intermediate/dada2/representative_sequences.qza --outdir /projectnb/talbot-lab-data/msilver/BU16s/test --paramout picrust_test.sh
export BIOMFILE=/projectnb/talbot-lab-data/msilver/BU16s/test/intermediate/dada2/table.qza
export SEQSFILE=/projectnb/talbot-lab-data/msilver/BU16s/test/intermediate/dada2/representative_sequences.qza
export OUTDIR=/projectnb/talbot-lab-data/msilver/BU16s/test
export HSP=mp
export NSTI=2
export CONDA_ENV=/projectnb/talbot-lab-data/msilver/.conda/envs/qiime2-2019.10

# Load modules and inputs
module purge
module load miniconda
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8
conda activate $CONDA_ENV
