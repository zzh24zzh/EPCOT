## Processing DNase-seq
Since the only cell-type specific inputs of EPCOT are DNase-seq profiles, we use samtools and deeptools RPGC normalization to generate normalized bigWig files from bam files. The `effectiveGenomeSize' in RPGC is calculated using [unique-kmers.py](https://github.com/dib-lab/khmer/blob/master/scripts/unique-kmers.py).
```
#download bam files and blacklist
wget -O GM12878_rep1.bam https://www.encodeproject.org/files/ENCFF020WZB/@@download/ENCFF020WZB.bam
wget -O GM12878_rep2.bam https://www.encodeproject.org/files/ENCFF729UYK/@@download/ENCFF729UYK.bam
wget -O black_list.bed.gz https://www.encodeproject.org/files/ENCFF356LFX/@@download/ENCFF356LFX.bed.gz
gunzip black_list.bed.gz

#merge and index bam
samtools merge GM12878.bam GM12878_rep*.bam
samtools index GM12878.bam

#generalize normalized coverage track
bamCoverage --bam GM12878.bam -o GM12878_dnase.bigWig --outFileFormat bigwig --normalizeUsing RPGC --effectiveGenomeSize 2559804523 
--ignoreForNormalization chrX chrM --Offset 1 --binSize 1 --numberOfProcessors 24 --blackListFileName black_list.bed --skipNonCoveredRegions
```
