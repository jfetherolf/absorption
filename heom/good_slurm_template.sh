#!/bin/sh
#SBATCH --job-name=HEOM_heomL_heomK
#SBATCH --output=HEOM_heomL_heomK.log
#SBATCH --error=HEOM_heomL_heomK.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

python batchdriver.py heomL heomK
