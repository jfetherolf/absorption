#!/bin/sh  
#SBATCH --job-name=pyrho-ehrenfest
#SBATCH --output=pyrhojob.out
#SBATCH --error=pyrhojob.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

export OMP_NUM_THREADS=2

python -u driver.py 1 >> pyrhoehrenjob.log
