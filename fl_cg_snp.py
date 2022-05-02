#!/usr/bin/env python

#Sarah Schmedes
#Email: sarah.schmedes@flhealth.gov

'''
The FL Core-Genome SNP  pipeline generates a core-genome SNP maximum liklihood tree
using the following tools: roary, snp-sites, snp-dist, iqtree.

Assumes the installion of python3.7+, Singularity, and installation of the StaPH-B Toolkit.
Accepts a group of .gff files as input. Run script in same directory as .gff files.
'''

import sys
import subprocess
import argparse

#Parse arguments, get path for fastqs
parser = argparse.ArgumentParser(usage='fl_cg_snp.py [options]')
parser.add_argument('--threads', default=10, dest='threads', help='specify number of threads, (default: %(default)s)')

if len(sys.argv[1:]) == 0:
    parser.print_help()
    parser.exit()

args = parser.parse_args()

threads = str(args.threads)

#Run roary
subprocess.run('singularity exec -B $(pwd):/data /apps/staphb-toolkit/containers/roary_3.12.0.sif roary -p ' + threads + ' -i 90 -e --mafft --dont_delete_files -v *.gff', shell=True, check=True)

#Run snp-sites
subprocess.run('singularity exec -B $(pwd):/data /apps/staphb-toolkit/containers/snp-sites_2.3.3.sif snp-sites -o SNPs.fasta -c core_gene_alignment.aln', shell=True, check=True)

#Run snp-dist
subprocess.run('singularity exec -B $(pwd):/data /apps/staphb-toolkit/containers/snp-dists_0.6.2.sif snp-dists core_gene_alignment.aln > pairwise_matrix.tsv', shell=True, check=True)

#Run iq-tree
subprocess.run('singularity exec -B $(pwd):/data /apps/staphb-toolkit/containers/iqtree_1.6.7.sif iqtree -s SNPs.fasta -m MFP+ASC -nt AUTO -bb 1000 -alrt 1000 -pre SNPs_boot -ntmax ' + threads, shell=True, check=True)
