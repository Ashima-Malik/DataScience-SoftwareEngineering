import numpy as np
class NaiveBayes():
    def fit(self,X,y):
        n_samples, n_features = X.shape
        self._classes = np.unique(y)
        n_classes = len(self._classes)
        self._mean = np.zeros((n_classes, n_features), dtype=np.float64)
        self._var = np.zeros((n_classes, n_features), dtype=np.float64)
        self._priors = np.unique(n_classes, dtype = np.float64)

        for idx, c in enumerate(self._classes):
            X_c = X[y==c]
            self._mean[idx,:] = X_c.mean(axis=0)
            self._var[idx,:] = X_c.mean(axis=0)
            self._priors[idx] = X_c.shape[0]/float(n_samples)

    def predict(self,X):
        y_pred = [self._predict(x) for x in X]
        return np.array(y_pred)

    def _predict(self,x):
        posteriors = []
        for idx, c in enumerate(self._classes):
            prior = np.log(self._priors[idx])
            posterior = np.sum(np.log(self._pdf(idx,x)))
            posterior = posterior+prior
            posteriors.append(posterior)
        return self._classes[np.argmax(posteriors)]

    def _pdf(self, class_idx, x):
        mean = self._mean[class_idx]
        var = self._var[class_idx]
        numerator = np.exp(-(x-mean)**2/(2*var))
        denominator = np.sqrt(2*np.pi*var)
        return  numerator/denominator






from sklearn.datasets import make_blobs
# generate 2d classification dataset
X, y = make_blobs(n_samples=10, centers=2, n_features=2, random_state=1)
# summarize
# print(X.shape, y.shape)
# print(X)
# print(y)

nb = NaiveBayes()
nb.fit(X,y)


# from sklearn.datasets import make_blobs
# from scipy.stats import norm
# from numpy import mean
# from numpy import std
#
#
# # fit a probability distribution to a univariate data sample
# def fit_distribution(data):
#     # estimate parameters
#     mu = mean(data)
#     sigma = std(data)
#     print(mu, sigma)
#     # fit distribution
#     dist = norm(mu, sigma)
#     return dist
# def probability(X, prior, dist1, dist2):
#     return prior * dist1.pdf(X[0]) * dist2.pdf(X[1])
#
# # generate 2d classification dataset
# X, y = make_blobs(n_samples=10, centers=2, n_features=2, random_state=1)
# print(X)
# print(y)
# # sort data into classes
# Xy0 = X[y == 0]
# Xy1 = X[y == 1]
# print(Xy0)
# print(Xy0.shape, Xy1.shape)
# # calculate priors
# priory0 = len(Xy0) / len(X)
# priory1 = len(Xy1) / len(X)
# print(priory0, priory1)
# # create PDFs for y==0
#
# X1y0 = fit_distribution(Xy0[:, 0])
# # X1y0=Xy0[:, 0]
# # print(X1y0)
# X2y0 = fit_distribution(Xy0[:, 1])
# # create PDFs for y==1
# X1y1 = fit_distribution(Xy1[:, 0])
# X2y1 = fit_distribution(Xy1[:, 1])
# Xsample, ysample = X[0], y[0]
# # py0 = probability(Xsample, priory0, distX1y0, distX2y0)
# # py1 = probability(Xsample, priory1, distX1y1, distX2y1)
# # print('P(y=0 | %s) = %.3f' % (Xsample, py0*100))
# # print('P(y=1 | %s) = %.3f' % (Xsample, py1*100))
# # print('Truth: y=%d' % ysample)