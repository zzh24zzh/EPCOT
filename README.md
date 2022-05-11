# EPCOT


EPCOT (jointly predicting <ins>EP</ins>igenome, <ins>C</ins>hromatin <ins>O</ins>rganization and <ins>T</ins>ranscription) is a comprehensive model to jointly predict epigenomic features, gene expression, high-resolution chromatin contact maps, and enhancer activities from DNA sequence and cell-type specific chromatin accessibility data. 

<img
  src="Profiles/model.png"
  title=""
  style="display: inline-block; margin: 0 auto; max-width: 300px">
  
 ## Dependencies
* einops (0.3.2)
* kipoiseq (0.5.2)
* numpy (1.19.5)
* torch (1.10.1)
* scipy (1.7.3)
* scikit-learn (1.0.2)

You can use ```conda``` to install the required packages
```
conda create -n epcot python=3.9
conda activate epcot
pip install -r requirements.txt
```
  

 ## Usage
Please see [Data/](https://github.com/zzh24zzh/EPCOT/tree/master/Data) for how to generate the inputs to EPCOT (one-hot repsentations of DNA sequences and DNase-seq).

You can download our pre-training model from Google Drive
```
pip install gdown
!gdown 1_YfpNSv-2ABQV2qSyBxem-y7aJFyRNzz --output models/pretrain_dnase.pt
```

For the trained downstream models and data used in downstream tasks, you can go to each correspoding directories [GEP/](https://github.com/zzh24zzh/EPCOT/tree/master/gex), [COP/](https://github.com/zzh24zzh/EPCOT/tree/master/chrom_organization), and .

We also prepare a Google Colab Notebook [EPCOT_usage.ipynb](https://github.com/zzh24zzh/EPCOT/blob/master/EPCOT_usage.ipynb) to introduce how to use EPCOT to predict multiple modalities and train logistic regression model using the predicted values of epigenomic features from the pre-training model
