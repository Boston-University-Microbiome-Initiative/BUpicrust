"""
Generate inputs for PiCrust
"""
from argparse import ArgumentParser, RawTextHelpFormatter
import os, sys

if __name__ == '__main__':
    parser = ArgumentParser(formatter_class=RawTextHelpFormatter)
    parser.add_argument('--biom', help='Path ASV biom table qiime artifact\n'
                                       '\ttable.qza from QIIME2-DADA2', required=True)
    parser.add_argument('--seqs', help='Path to representative ASV sequences\n'
                                       '\trepresentative_sequences.qza from QIIME2-DADA2', required=True)
    parser.add_argument('--outdir', help='Output directory', required=True)
    parser.add_argument('--hsp', help='Hidden state prediction method. Default: mp', choices=('mp', 'emp_prob', 'pic', 'scp',
    'subtree_average'))
    parser.add_argument('--nsti', help='Maximum distance from nearest sequence taxon. Default=2', default=2)
    parser.add_argument('--paramout', help='Path to output parameter file', required=True)

    args = parser.parse_args()

    """I/O"""
    # Inputs
    biomfile = os.path.abspath(args.biom)
    seqsfile = os.path.abspath(args.seqs)
    for f in [biomfile, seqsfile]:
        if not os.path.exists(f):
            raise IOError('%s does not exist' % f)
    # Outputs
    outdir = os.path.abspath(args.outdir)

    outpath = os.path.abspath(args.paramout)
    dir_outpath = os.path.dirname(outpath)

    for d in [outdir, dir_outpath]:
        if not os.path.exists(d):
            os.makedirs(d)
    """Collect arguments"""
    order = ['BIOMFILE',
             'SEQSFILE',
             'OUTDIR',
             'HSP',
             'NSTI',
             ]
    parameters = dict(zip(order, [biomfile, seqsfile, outdir, args.hsp, args.nsti]))
    defaults = {'CONDA_ENV': '/projectnb/talbot-lab-data/msilver/.conda/envs/qiime2-2019.10'}
    # Add defaults to user-define
    parameters.update(defaults)

    """Create parameter file"""
    # Add command as comment
    command = '# python ' + ' '.join(sys.argv) + '\n'
    exports = '\n'.join(['export %s=%s' % (k, parameters[k]) for k in order]) + '\n'
    GLOBAL_LOADS = """
# Load modules and inputs
module purge
module load miniconda
export LC_ALL=en_US.utf-8
export LANG=en_US.utf-8
conda activate $CONDA_ENV"""
    output = command + exports + GLOBAL_LOADS + '\n'
    with open(outpath, 'w') as fh:
        fh.write(output)