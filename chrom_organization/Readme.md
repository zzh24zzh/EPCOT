# Chromatin contact map prediction task

## Data preparing

In the downstream task of chromatin contact map prediction, the chromatin contact maps are downloaded from 4DN, which are OE-normalized using Juicebox. For example, we download 'GM12878.hic' file of GM12878 Hi-C contact map with 4DN accession number [4DNFI1UEG1HD](https://data.4dnucleome.org/files-processed/4DNFI1UEG1HD/) 
```
mkdir GM12878_contact_map

```

## Download trained models in Hi-C prediction of three cell lines
```
pip install gdown
!gdown 1ia-ZoSoiZGDFPnZcySzMpirovHhulRfH --output models/hic_HFF_transformer.pt
!gdown 1EXm2AjqqO-UtLi2pprbDEb1gPXrxI3aW --output models/hic_GM12878_transformer.pt
!gdown 1ofkpS526gXpnusGpRWVHgIFFFpTSW4Rm --output models/hic_IMR-90_transformer.pt
```
