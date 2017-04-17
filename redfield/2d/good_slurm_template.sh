#!/bin/sh  
#SBATCH --job-name=tcl2_2d
#SBATCH --output=slurm_tcl2_2d.log
#SBATCH --error=slurm_tcl2_2d.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 36:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python driver.py 
