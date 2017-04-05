#!/bin/sh  
#SBATCH --job-name=hybrid_TAUC_T_LAMDA_SPLIT_RUN
#SBATCH --output=slurm_hybrid_TAUC_T_LAMDA_SPLIT_RUN.log
#SBATCH --error=slurm_hybrid_TAUC_T_LAMDA_SPLIT_RUN.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=10000
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python eetdriver.py TAUC TT LAMDA SPLIT RUN
