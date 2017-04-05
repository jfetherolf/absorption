#!/bin/sh  
#SBATCH --job-name=heom_100._300._100._14
#SBATCH --output=slurm_heom_100._300._100._14.log
#SBATCH --error=slurm_heom_100._300._100._14.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=32000
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

#export OMP_NUM_THREADS=1

python popeetheom.py 100. 300. 100. 14
