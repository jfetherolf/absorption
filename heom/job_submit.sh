#!/bin/bash

#EXPECTED_ARGS=2

#if [ $# -ne $EXPECTED_ARGS ]; then
#    echo "Usage: `basename $0` heomL heomK"
#   exit 99
#fi

#heomL=$1
#heomK=$2

for heomL in 12 14; do
    for heomK in 1 2; do
        slurmsh="slurm_${heomL}_${heomK}.sh"
        sed "s/heomL/${heomL}/g; s/heomK/${heomK}/g" good_slurm_template.sh > $slurmsh
        sbatch $slurmsh
    done
done
