#!/bin/sh  
#SBATCH --job-name=hybrid_noPD
#SBATCH --output=hybrid_noPD.log
#SBATCH --error=hybrid_noPD.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python hybrid2015.py

