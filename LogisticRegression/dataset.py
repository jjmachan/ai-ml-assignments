import numpy as np
import matplotlib.pyplot as plt


def create():
    N = 100 # number of points per class
    D = 2 # dimensionality
    K = 2 # number of classes
    X = np.zeros((N*K,D)) # data matrix (each row = single example)
    yhat = np.zeros(N*K, dtype='uint8') # class labels
    for j in xrange(K):
      ix = range(N*j,N*(j+1))
      r = np.linspace(0.0,1,N) # radius
      t = np.linspace(j*4,(j+1)*4,N) + np.random.randn(N)*0.2 # theta
      X[ix] = np.c_[r*np.sin(t), r*np.cos(t)]
      yhat[ix] = j


    # lets visualize the data:
    X = X.T
    yhat =yhat.reshape(1,yhat.shape[0])
    perm = np.random.permutation(X.shape[1])
    train_num = int(X.shape[1]*0.8)
    X_train = X[:,perm[:train_num]]
    yhat_train = yhat[:,perm[:train_num]]
    X_test = X[:,perm[train_num:]]
    yhat_test = yhat[:,perm[train_num:]]
    plt.figure(1)
    plt.title("Dataset for training")
    plt.scatter((X_train.T)[:,0], (X_train.T[:,1]), c=yhat_train[0,:], s=40, cmap=plt.cm.Spectral)
    plt.figure(2)
    plt.title("Dataset for testing")
    plt.scatter((X_test.T)[:,0], (X_test.T[:,1]), c=yhat_test[0,:], s=40, cmap=plt.cm.Spectral)
    plt.show()
    return X_train,yhat_train,X_test,yhat_test

def vis_classifier(X_test,yhat_test,w,b):
    # plot the resulting classifier
    h = 0.02
    x_min, x_max = X_test[0,:].min(), X_test[0,:].max()
    y_min, y_max = X_test[1,:].min(), X_test[1,:].max()
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    act = np.dot(np.c_[xx.ravel(), yy.ravel()], w) + b

    res = act >= 0.5
    res = res.reshape(xx.shape)
    plt.figure(1)
    plt.title("Classifier Visualization")
    plt.contourf(xx, yy, res, cmap=plt.cm.Spectral, alpha=0.8)
    plt.scatter(X_test.T[:, 0], X_test.T[:, 1], c=yhat_test[0,:], s=40, cmap=plt.cm.Spectral)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.show()
