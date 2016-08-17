#!/bin/sh
#SBATCH --job-name=HEOM_14_1
#SBATCH --output=HEOM_14_1.log
#SBATCH --error=HEOM_14_1.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

python batchdriver.py 14 1
