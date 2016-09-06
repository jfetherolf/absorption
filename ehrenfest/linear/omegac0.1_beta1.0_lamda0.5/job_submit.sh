#!/bin/bash
# Check for proper number of command line args.

EXPECTED_ARGS=1

if [ $# -ne $EXPECTED_ARGS ]; then
    echo "Usage: `basename $0` nrun"
   exit 99
fi

nrun=$1
for run in `seq ${nrun}`; do
    slurmsh="slurm_$run.sh"
    sed "s/RUN/${run}/g" good_slurm_template.sh > $slurmsh
    sbatch $slurmsh
done

