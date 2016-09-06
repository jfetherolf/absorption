#!/bin/bash
# Check for proper number of command line args.

EXPECTED_ARGS=2

if [ $# -ne $EXPECTED_ARGS ]; then
    echo "Usage: `basename $0` nstart nrun"
   exit 99
fi

nstart=$1
nrun=$2


for run in `seq ${nstart} ${nrun}`; do
    slurmsh="slurm_$run.sh"
    sed "s/RUN/${run}/g" good_slurm_template.sh > $slurmsh
    sbatch $slurmsh
done

