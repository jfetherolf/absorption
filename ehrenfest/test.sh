#!/bin/sh  
#SBATCH --job-name=ehrenfest_test
#SBATCH --output=ehrenfest_test.log
#SBATCH --error=slurm_ehrenfest_test.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python batchdriver.py 0.3 3.0 1

