#!/bin/sh  
#SBATCH --job-name=hybrid_TAUC_T_LAMDA_SPLIT
#SBATCH --output=hybrid_TAUC_T_LAMDA_SPLIT.log
#SBATCH --error=slurm_hybrid_TAUC_T_LAMDA_SPLIT.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python batchdriver.py TAUC T LAMDA SPLIT
