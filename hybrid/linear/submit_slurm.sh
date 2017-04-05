#!/bin/sh  
#SBATCH --job-name=heom_spec
#SBATCH --output=slurm_heom_spec.log
#SBATCH --error=slurm_heom_spec.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python heom2015.py 
