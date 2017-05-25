# FUSTr
Families Under Selection in Transcriptomes
# Introduction  
Fuster is a pipeline that clusters coding sequences from transcriptomes into protein families, and then analyzes those families for positive selection.

# Getting started 

First you will need [pip3](http://stackoverflow.com/questions/6587507/how-to-install-pip-with-python-3/6587528#6587528) installed.
Using pip3 you can install miniconda3 in order to get conda so that you can set up the environment with all other dependencies.
```bash
pip3 install miniconda3
```
This program works by analyzing transcriptome assemblies.


Once you have conda installed,change in to the directory that has your transcriptomes and clone into this repository.

```bash
git clone https://github.com/tijeco/Fuster.git
```


Using conda, you can set up an environment that installs all dependencies in a local session

```bash
cd Fuster
conda create --name Fuster -c bioconda --file Fuster.requirements.txt
source activate Fuster
```

In this directory you should have the amino acid sequence files and nucleotide sequences from transdecoder, make sure that the amino acid sequences end in **.pep** </br>
After that all you have to do is type the following command with the path to the directory containing all transcriptome assemblies (ending in .fasta) and the Snakefile will do the rest of the work!

```
snakemake -d <path_to_fastas>
```
Once that finishes you can end the conda session using

```bash
source deactivate  
```
