#!/bin/sh  
#SBATCH --job-name=hybrid_0.3_1.0_0.5_0.3
#SBATCH --output=slurm_hybrid_0.3_1.0_0.5_0.3.log
#SBATCH --error=slurm_hybrid_0.3_1.0_0.5_0.3.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python batchdriver.py 0.3 1.0 0.5 0.3

