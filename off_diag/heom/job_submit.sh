#!/bin/bash

#EXPECTED_ARGS=2

#if [ $# -ne $EXPECTED_ARGS ]; then
#    echo "Usage: `basename $0` heomL heomK"
#   exit 99
#fi

for omega_c in 0.01; do
    for beta in 1.0; do
        for v in 1.0; do
            for heomL in 24 25; do
                for heomK in 0; do
                    slurmsh="slurm${omega_c}_${beta}_${v}_${heomL}_${heomK}.sh"
                    sed "s/OMEGAC/${omega_c}/g; s/BETA/${beta}/g; s/Vcoup/${v}/g; s/heomL/${heomL}/g; s/heomK/${heomK}/g" good_slurm_template.sh > $slurmsh
                    sbatch $slurmsh
                done
            done
        done
    done
done
