#!/bin/sh
#SBATCH --job-name=HEOM_omegacOMEGAC_betaBETA_LheomL_KheomK
#SBATCH --output=slurm_HEOM_omegacOMEGAC_betaBETA_LheomL_KheomK.log
#SBATCH --error=slurm_HEOM_omegacOMEGAC_betaBETA_LheomL_KheomK.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 36:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

python heomdriver.py OMEGAC BETA Vcoup heomL heomK
