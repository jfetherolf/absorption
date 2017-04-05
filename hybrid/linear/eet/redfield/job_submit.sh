#!/bin/bash

for tau_c in 100. 500.; do
    for T in 300.; do
        for lamda in 2. 20. 100. 500.; do
    #       slurmsh="slurm_${tau_c}_${T}_${lamda}.sh"
            sed "s/TAUC/${tau_c}/g; s/TT/${T}/g; s/LAMDA/${lamda}/g" good_script.sh > $slurmsh
    #       sbatch $slurmsh
        done
    done
done

