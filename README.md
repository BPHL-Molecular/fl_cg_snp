# FL-cgSNP (Florida - core genome SNP)
FL BPHL's core genome SNP pipeline for the identification of clusters of closely related bacterial isolates to support public health surveillance and outbreak investigations.

## About
FL-cgSNP was developed to calculate pairwise cgSNP distances between a group of bacterial isolates to help identify outbreak clusters. The pipeline uses .gff files generated from our [FLAQ-AMR pipeline](https://github.com/BPHL-Molecular/flaq_amr) as input. Final outputs include a pairwise cgSNP distance matrix and a maximum likelihood phylogenetic tree. The current version will run only on [HiPerGator](https://www.rc.ufl.edu/about/hipergator/)(HPG) using local Singularity containers for each pipeline process.

Stay tuned for FL-cgSNP's upgrade to [Talbot](https://github.com/BPHL-Molecular/Talbot), a platform agnostic [Nextflow](https://www.nextflow.io/) workflow. Talbot is currently under active development.

## Dependencies
- Python3
- Singularity/Apptainer
- Git

To load python3 into your current environment on HiPerGator, either use `module load python` to get the lastest version of python or activate your base conda environment. For more information on how to set up your base conda environment on HPG, see the [HiPerGator Analysis Reference Guide](https://github.com/StaPH-B/southeast-region/tree/master/hipergator)).

Singularity/Apptainer will be loaded as a module during your job execution on HPG using the sbatch job script in this repository. 

Git is already installed in your HPG environment upon login.

## Usage

For first time use, clone this repository to a directory in blue on HPG, such as in /blue/bphl-\<state\>/\<user\>/repos/bphl-molecular/.
```
cd /blue/bphl-<state>/<user>/repos/bphl-molecular/
git clone https://github.com/BPHL-Molecular/fl_cg_snp.git
```
For future use, update any changes to your local repository on HPG by navigating to the fl_cg_snp repository and pulling any changes.
```
cd fl_cg_snp/
git pull
```
To run the FL-cgSNP pipeline, copy all files from the fl_cg_snp local repository to your analysis folder.
```
mkdir <analysis_dir>
cd <analysis_dir>
cp /blue/bphl-<state>/<user>/repos/bphl-molecular/fl_cg_snp/* .
cp /path/to/gffs/*.gff .
```

Edit your sbatch job submission script to include your email to receive an email notification upon job END or FAIL. Replace ENTER EMAIL in `#SBATCH --mail-user=ENTER EMAIL` with your email address. Make sure there is no space between = and your email address. Edit additional sbatch parameters as needed to run your job succesfully, such as the length of time the job will run.

Submit your job.
```
sbatch sbatch_fl_cg_snp.sh
```

## Main processes
- [roary](https://github.com/sanger-pathogens/Roary)
- [snp-sites](https://github.com/sanger-pathogens/snp-sites)
- [snp-dist](https://github.com/tseemann/snp-dists)
- [iqtree](http://www.iqtree.org/)

## Primary outputs

The main outputs include: pairwise_matrix.tsv; SNPs_boot.treefile.



## Developed by:
[@SESchmedes](https://www.github.com/SESchmedes)<br />

Please email bphl16BioInformatics@flhealth.gov for questions and support.
