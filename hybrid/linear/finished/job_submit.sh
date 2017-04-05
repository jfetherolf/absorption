#!/bin/bash

for omega_c in 0.1 0.3; do
    for beta in 1.0; do
        for lamda in 0.5; do
            for split in 0.5 0.3 0.2; do
                slurmsh="slurm_${omega_c}_${beta}_${lamda}_${split}.sh"
                sed "s/OMEGAC/${omega_c}/g; s/BETA/${beta}/g; s/LAMDA/${lamda}/g; s/SPLIT/${split}/g" good_slurm_template.sh > $slurmsh
                sbatch $slurmsh
            done
        done
    done
done

