#!/bin/sh  
#SBATCH --job-name=frozen_0.1_1.0_run24
#SBATCH --output=slurm_frozen_0.1_1.0_run24.log
#SBATCH --error=slurm_frozen_0.1_1.0_run24.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python driver.py 0.1 1.0 24

