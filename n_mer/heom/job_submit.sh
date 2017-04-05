#!/bin/bash

for omega_c in 0.1; do
    for beta in 1.0; do
        for split in 4.0; do
            for run in `seq 0 9`; do
                slurmsh="slurm_${omega_c}_${beta}_${split}_${run}.sh"
                sed "s/OMEGAC/${omega_c}/g; s/BETA/${beta}/g; s/SPLIT/${split}/g; s/RUN/${run}/g;" good_slurm_template.sh > $slurmsh
                sbatch $slurmsh
            done
        done
    done
done

