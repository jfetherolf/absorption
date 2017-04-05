#!/bin/sh  
#SBATCH --job-name=hybrid_OMEGAC_BETA_SPLIT
#SBATCH --output=hybrid_OMEGAC_BETA_SPLIT.log
#SBATCH --error=slurm_hybrid_OMEGAC_BETA_SPLIT.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python batchdriver.py OMEGAC BETA SPLIT

