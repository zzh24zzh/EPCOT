# Chromatin contact map prediction task

## Data preparing

In the downstream task of chromatin contact map prediction, the chromatin contact maps are downloaded from 4DN, which are OE-normalized using Juicebox. For example, we download 'GM12878.hic' file of GM12878 Hi-C contact map with 4DN accession number [4DNFI1UEG1HD](https://data.4dnucleome.org/files-processed/4DNFI1UEG1HD/), we use the following python code to obtain the OE-normalized contact maps. 
```
import os,straw
os.system('mkdir GM12878_Hi-C')
resolution=5000
chrs = [str(i) for i in range(1, 23)] + ['X']
for chr in chrs:
    f = open('GM12878_Hi-C/chr%s_%s.txt' % (chr,resolution), 'w')
    result = straw.straw('oe', 'NONE','GM12878.hic', chr, chr,
                             'BP', resolution)
    for i in range(len(result)):
        f.write("{0}\t{1}\t{2}\n".format(result[i].binX, result[i].binY, result[i].counts))
    f.close()
```

## Download trained models
```
pip install gdown
#5kb-resolution Hi-C 
!gdown 1ia-ZoSoiZGDFPnZcySzMpirovHhulRfH --output models/hic_HFF_transformer.pt
!gdown 1EXm2AjqqO-UtLi2pprbDEb1gPXrxI3aW --output models/hic_GM12878_transformer.pt
!gdown 1ofkpS526gXpnusGpRWVHgIFFFpTSW4Rm --output models/hic_IMR-90_transformer.pt

#1kb-resolution Micro-C
```
