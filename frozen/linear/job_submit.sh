#!/bin/bash
# Check for proper number of command line args.

EXPECTED_ARGS=0

if [ $# -ne $EXPECTED_ARGS ]; then
    echo "Usage: `basename $0` run"
   exit 99
fi


for omega_c in 0.1 ; do
    for beta in 1.0 ; do
        for run in `seq 0 24`; do
            slurmsh="slurm_$run.sh"
            sed "s/OMEGAC/${omega_c}/g; s/BETA/${beta}/g; s/RUN/${run}/g" good_slurm_template.sh > $slurmsh
            sbatch $slurmsh
        done
    done
done

