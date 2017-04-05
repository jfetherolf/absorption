#!/bin/bash

for tau_c in 100. 500.; do
    for T in 300.; do
        for lamda in 1./50. 1./5. 1. 5.; do
            for split in 0.25 0.5 1.0 1.5 2.0; do
                slurmsh="slurm_${omega_c}_${beta}.sh"
                sed "s/TAUC/${omega_c}/g; s/T/${beta}/g; s/LAMDA/${lamda}/g; s/SPLIT/${split}/g" good_slurm_template.sh > $slurmsh
                sbatch $slurmsh
            done
        done
    done
done

