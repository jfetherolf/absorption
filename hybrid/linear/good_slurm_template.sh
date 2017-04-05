#!/bin/sh  
#SBATCH --job-name=hybrid_OMEGAC_BETA_SPLIT_RUN
#SBATCH --output=hybrid_OMEGAC_BETA_SPLIT_RUN.log
#SBATCH --error=slurm_hybrid_OMEGAC_BETA_SPLIT_RUN.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python heomspec2015.py 
