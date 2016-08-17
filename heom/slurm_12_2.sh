#!/bin/sh
#SBATCH --job-name=HEOM_12_2
#SBATCH --output=HEOM_12_2.log
#SBATCH --error=HEOM_12_2.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

python batchdriver.py 12 2