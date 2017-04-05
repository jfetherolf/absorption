#!/bin/bash

for omega_c in 0.1 0.3; do
    for beta in 1.0; do
        for lamda in 1.0; do
            slurmsh="slurm_${omega_c}_${beta}_${lamda}.sh"
            sed "s/OMEGAC/${omega_c}/g; s/BETA/${beta}/g; s/LAMDA/${lamda}/g;" good_slurm_template.sh > $slurmsh
            sbatch $slurmsh
        done
    done
done

