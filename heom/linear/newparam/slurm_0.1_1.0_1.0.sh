#!/bin/sh
#SBATCH --job-name=HEOM_omegac0.1_beta1.0_lamda1.0
#SBATCH --output=slurm_HEOM_omegac0.1_beta1.0_lamda1.0.log
#SBATCH --error=slurm_HEOM_omegac0.1_beta1.0_lamda1.0.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

python batchdriver.py 0.1 1.0 1.0
