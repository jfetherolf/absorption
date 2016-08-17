#!/bin/sh  
#SBATCH --job-name=ehrenfest
#SBATCH --output=pyrhojob.out
#SBATCH --error=pyrhojob.err
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH -t 24:00:00

WORKDIR=$SLURM_SUBMIT_DIR
cd $WORKDIR

export OMP_NUM_THREADS=2

COUNTER=0
while [  $COUNT -lt 10 ]; do
fout="ehrenfest$COUNT.log";
python -u driver.py ${$COUNT} >> $fout     
    let COUNTER=COUNTER+1 
    done

