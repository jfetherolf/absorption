#!/bin/sh  
#SBATCH --job-name=redfield_TAUC_TT_LAMDA
#SBATCH --output=slurm_redfield_TAUC_TT_LAMDA.log
#SBATCH --error=slurm_redfield_TAUC_TT_LAMDA.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=8000
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

#export OMP_NUM_THREADS=1

python eetdriverrf.py TAUC TT LAMDA
