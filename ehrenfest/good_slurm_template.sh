#!/bin/sh  
#SBATCH --job-name=ehrenfest_OMEGAC_BETA_runRUN
#SBATCH --output=ehrenfest_OMEGAC_BETA_runRUN.log
#SBATCH --error=slurm_ehrenfest_OMEGAC_BETA_runRUN.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python batchdriver.py OMEGAC BETA RUN

