#!/bin/sh  
#SBATCH --job-name=frozen_OMEGAC_BETA_runRUN
#SBATCH --output=slurm_frozen_OMEGAC_BETA_runRUN.log
#SBATCH --error=slurm_frozen_OMEGAC_BETA_runRUN.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python driver.py OMEGAC BETA RUN

