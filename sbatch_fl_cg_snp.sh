#!/bin/bash
#SBATCH --account=bphl-umbrella
#SBATCH --qos=bphl-umbrella
#SBATCH --job-name=fl_cg_snp
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=ENTER EMAIL
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=40gb
#SBATCH --time=1-00
#SBATCH --output=fl_cg_snp.%j.out
#SBATCH --error=fl_cg_snp.%j.err

module load apptainer

#Run script/command and use $SLURM_CPUS_ON_NODE
python fl_cg_snp.py --threads $SLURM_CPUS_ON_NODE
