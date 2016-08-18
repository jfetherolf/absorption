#!/bin/sh  
#SBATCH --job-name=ehrenfest_1.0_3.0_run5
#SBATCH --output=ehrenfest_1.0_3.0_run5.log
#SBATCH --error=slurm_ehrenfest_1.0_3.0_run5.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python batchdriver.py 1.0 3.0 5
