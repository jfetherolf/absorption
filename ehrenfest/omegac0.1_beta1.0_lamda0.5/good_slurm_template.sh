#!/bin/sh  
#SBATCH --job-name=ehrenfest_RUN
#SBATCH --output=ehrenfest_RUN.log
#SBATCH --error=slurm_ehrenfest_RUN.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python driver.py RUN

