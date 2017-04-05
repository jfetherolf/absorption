#!/bin/sh  
#SBATCH --job-name=hybrid_100._T_100._0.5_2
#SBATCH --output=slurm_hybrid_100._T_100._0.5_2.log
#SBATCH --error=slurm_hybrid_100._T_100._0.5_2.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=10000
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR
 
python eetdriver.py 100. 300. 100. 0.5 2
