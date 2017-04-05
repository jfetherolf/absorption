#!/bin/bash

for tau_c in 100.; do
    for T in 300.; do
        for lamda in 100.; do
            for L in 14; do
                slurmsh="slurm_${tau_c}_${T}_${lamda}_${L}.sh"
                sed "s/TAUC/${tau_c}/g; s/TT/${T}/g; s/LAMDA/${lamda}/g; s/LL/${L}/g" good_slurm_template.sh > $slurmsh
                sbatch $slurmsh
            done
        done
    done
done

