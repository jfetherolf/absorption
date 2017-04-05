#!/bin/bash

for tau_c in 100.; do
    for T in 300.; do
        for lamda in 100.; do
            for split in 4.0; do
                for run in $(seq 0 9); do
                    slurmsh="slurm_${tau_c}_${T}_${lamda}_${split}_${run}.sh"
                    sed "s/TAUC/${tau_c}/g; s/TT/${T}/g; s/LAMDA/${lamda}/g; s/SPLIT/${split}/g; s/RUN/${run}/g;" good_slurm_template.sh > $slurmsh
                    sbatch $slurmsh
                done
            done
        done
    done
done

