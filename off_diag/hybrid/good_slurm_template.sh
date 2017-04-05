#!/bin/sh
#SBATCH --job-name=hybrid_offdiag_omegacOMEGAC_betaBETA_splitSPLIT_runRUN
#SBATCH --output=slurm_hybrid_offdiag_omegacOMEGAC_betaBETA_splitSPLIT_runRUN.log
#SBATCH --error=slurm_hybrid_offdiag_omegacOMEGAC_betaBETA_splitSPLIT_runRUN.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

python frozendriver.py OMEGAC BETA RUN
