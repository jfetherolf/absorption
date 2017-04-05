#!/bin/sh
#SBATCH --job-name=HEOM_omegac0.01_beta1.0_L24_K0
#SBATCH --output=slurm_HEOM_omegac0.01_beta1.0_L24_K0.log
#SBATCH --error=slurm_HEOM_omegac0.01_beta1.0_L24_K0.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 36:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

python heomdriver.py 0.01 1.0 1.0 24 0
