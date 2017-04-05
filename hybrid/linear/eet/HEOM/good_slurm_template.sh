#!/bin/sh  
#SBATCH --job-name=heom_TAUC_TT_LAMDA_LL
#SBATCH --output=slurm_heom_TAUC_TT_LAMDA_LL.log
#SBATCH --error=slurm_heom_TAUC_TT_LAMDA_LL.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=32000
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

#export OMP_NUM_THREADS=1

python popeetheom.py TAUC TT LAMDA LL