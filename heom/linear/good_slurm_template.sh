#!/bin/sh
#SBATCH --job-name=HEOM_omegacOMEGAC_betaBETA_LheomL_KheomK
#SBATCH --output=HEOM_omegacOMEGAC_betaBETA_LheomL_KheomK.log
#SBATCH --error=HEOM_omegacOMEGAC_betaBETA_LheomL_KheomK.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

python batchdriver.py OMEGAC BETA heomL heomK
