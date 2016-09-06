#!/bin/bash

for omega_c in 0.1 0.3 1.0; do
    for beta in 1.0 3.0; do
        for split in 1.0 5.0 10.0; do
            slurmsh="slurm_${omega_c}_${beta}.sh"
            sed "s/OMEGAC/${omega_c}/g; s/BETA/${beta}/g; s/SPLIT/${split}/g" good_slurm_template.sh > $slurmsh
            sbatch $slurmsh
        done
    done
done

