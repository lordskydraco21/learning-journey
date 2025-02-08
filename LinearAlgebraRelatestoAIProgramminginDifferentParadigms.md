
#### **1. Machine Learning (Classical AI)**
- **Vectors & Matrices** → Used to store data points, feature sets, and model parameters.
- **Dot Product** → Computes similarity between feature vectors (e.g., in NLP, recommendation systems).
- **Matrix Multiplication** → Key operation in training models (e.g., weight updates in neural networks).
- **Eigenvalues & Eigenvectors** → Used in **PCA (Principal Component Analysis)** for dimensionality reduction.
- **Least Squares & Pseudo-Inverse** → Fundamental for **linear regression** and solving overdetermined systems.

#### **2. Deep Learning (Neural Networks)**
- **Tensors** → Represent multi-dimensional data (e.g., images, sequences) in frameworks like TensorFlow/PyTorch.
- **Matrix Multiplication** → Essential for computing activations and gradients in backpropagation.
- **Singular Value Decomposition (SVD)** → Used in compression and **low-rank approximations**.
- **Norms & Regularization** → L1/L2 norms are used to prevent overfitting (e.g., Lasso, Ridge Regression).
- **Covariance Matrices** → Found in batch normalization and probabilistic modeling.

#### **3. Reinforcement Learning**
- **State Representations as Vectors** → Encodes environment observations.
- **Projection & Transformations** → Feature engineering for encoding states in lower dimensions.
- **Matrix Inversion** → Used in solving Bellman Equations (Dynamic Programming for RL).
- **Eigenvalues in Markov Processes** → Eigenvalues of transition matrices help in analyzing convergence.

#### **4. Probabilistic AI (Bayesian Learning, Generative Models)**
- **Covariance & Correlation Matrices** → Essential in **Gaussian distributions** and **Bayesian inference**.
- **Matrix Factorization** → Used in collaborative filtering (e.g., recommender systems).
- **Moore-Penrose Inverse** → Applied in probabilistic graphical models.

#### **5. Computer Vision**
- **Image as a Matrix** → Each pixel is a numerical value in a 2D or 3D array.
- **Convolution Operations** → Matrices represent filters/kernels applied over an image.
- **SVD & Eigenvectors** → Used in **face recognition (Eigenfaces)** and image compression.

#### **6. Natural Language Processing (NLP)**
- **Word Embeddings as Vectors** → Used in Word2Vec, GloVe, BERT.
- **Dot Product & Cosine Similarity** → Measures text similarity (e.g., search engines).
- **Matrix Factorization (SVD, PCA)** → Used in Latent Semantic Analysis (LSA).
- **Transformers & Attention Mechanisms** → Heavy use of matrix operations for **self-attention computations**.

Linear algebra is **everywhere** in AI, no matter the paradigm.
