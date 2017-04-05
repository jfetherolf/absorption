#!/bin/bash

#EXPECTED_ARGS=2

#if [ $# -ne $EXPECTED_ARGS ]; then
#    echo "Usage: `basename $0` heomL heomK"
#   exit 99
#fi

for omega_c in 1.0; do
    for beta in 1.0; do
        for run in 0; do
            slurmsh="slurm${omega_c}_${beta}_${split}_${run}.sh"
            sed "s/OMEGAC/${omega_c}/g; s/BETA/${beta}/g; s/RUN/${run}/g" good_slurm_template.sh > $slurmsh
            sbatch $slurmsh
        done
    done
done
