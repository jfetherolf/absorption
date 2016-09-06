#!/bin/sh  
#SBATCH --job-name=TCL2
#SBATCH --output=TCL2.log
#SBATCH --error=TCL2.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python driver.py

