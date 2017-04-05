#!/bin/sh
#SBATCH --job-name=hybrid_offdiag_omegac1.0_beta1.0_splitSPLIT_run0
#SBATCH --output=slurm_hybrid_offdiag_omegac1.0_beta1.0_splitSPLIT_run0.log
#SBATCH --error=slurm_hybrid_offdiag_omegac1.0_beta1.0_splitSPLIT_run0.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

python frozendriver.py 1.0 1.0 0
