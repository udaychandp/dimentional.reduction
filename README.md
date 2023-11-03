# Dimensionality Reduction using t-SNE
t-Distributed Stochastic Neighbor Embedding (t-SNE) is a dimensionality reduction technique commonly employed in machine learning and data visualization. Developed by Laurens van der Maaten and Geoffrey Hinton, t-SNE is particularly effective in capturing complex relationships within high-dimensional data and representing them in a lower-dimensional space, often two or three dimensions. Unlike linear methods, t-SNE preserves local similarities, making it adept at revealing clusters and patterns in the data. It operates by modeling pairwise similarities between data points in the original and reduced spaces, using a probability distribution that emphasizes maintaining the relative distances between nearby points. This non-linear approach makes t-SNE especially useful for visualizing intricate structures and discerning meaningful patterns in complex datasets, contributing to its widespread use in exploratory data analysis and pattern recognition tasks.

Basically, we are considering the data-set of mnist which is multi-dimension data set with a shape of (60000,784) so our intension is to reduce the dimension to understandable form like 2D or 3D


> libraries required 
```
from keras.datasets import mnist
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
```

where you can install all of them from requirements.txt
```
pip install requirements.txt
```

here initially we considered the data-set called keras-datasets library and we imported mnist and we fit_transformed by Taking only 10k samples for quick results and you can run the data with respect to your preference of the CPU and GPU cores and you can go for the CUDA toolkit for quick responsesit and plot it with sklearn.manifold 

![output](https://github.com/udaychandp/dimentional.reduction/assets/114306402/ee94e78b-9ac5-4d28-936c-18082176bb28)
