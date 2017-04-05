#!/bin/sh
#SBATCH --job-name=HEOM_omegacOMEGAC_betaBETA_lamdaLAMDA
#SBATCH --output=slurm_HEOM_omegacOMEGAC_betaBETA_lamdaLAMDA.log
#SBATCH --error=slurm_HEOM_omegacOMEGAC_betaBETA_lamdaLAMDA.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

python batchdriver.py OMEGAC BETA LAMDA
