#!/bin/bash

#EXPECTED_ARGS=2

#if [ $# -ne $EXPECTED_ARGS ]; then
#    echo "Usage: `basename $0` heomL heomK"
#   exit 99
#fi

#heomL=$1
#heomK=$2
for omega_c in 3.0 5.0 10.0; do
    for beta in 1.0 3.0; do
        for heomL in 14 16; do
            for heomK in 1; do
                slurmsh="slurm${omega_c}_${beta}_${heomL}_${heomK}.sh"
                sed "s/OMEGAC/${omega_c}/g; s/BETA/${beta}/g; s/heomL/${heomL}/g; s/heomK/${heomK}/g" good_slurm_template.sh > $slurmsh
                sbatch $slurmsh
            done
        done
    done
done
