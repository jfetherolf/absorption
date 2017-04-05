#!/bin/sh  
#SBATCH --job-name=hybrid_1.0_1.0_2.0
#SBATCH --output=hybrid_1.0_1.0_2.0.log
#SBATCH --error=slurm_hybrid_1.0_1.0_2.0.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python batchdriver.py 1.0 1.0 2.0

