#!/bin/bash
# Check for proper number of command line args.

EXPECTED_ARGS=1

if [ $# -ne $EXPECTED_ARGS ]; then
    echo "Usage: `basename $0` run"
   exit 99
fi

nrun=$1

for omega_c in 0.1 0.3 1.0; do
    for beta in 1.0 3.0; do
        for run in `seq ${nrun}`; do
            slurmsh="slurm_$run.sh"
            sed "s/OMEGAC/${omega_c}/g; s/BETA/${beta}/g; s/RUN/${run}/g" good_slurm_template.sh > $slurmsh
            sbatch $slurmsh
        done
    done
done

