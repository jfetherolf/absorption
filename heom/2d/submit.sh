#!/bin/sh  
#SBATCH --job-name=heom_2d
#SBATCH --output=heom_2d.log
#SBATCH --error=heom_2d.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

python peakosc.py
