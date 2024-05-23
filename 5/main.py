import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt
import matplotlib

# Genera datos sintéticos
np.random.seed(42)
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]

# Genera algunas anomalías regulares
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))

# Entrena el modelo
clf = svm.OneClassSVM(nu=0.1, kernel="rbf", gamma=0.1)
clf.fit(X_train)

# Predice los datos de entrenamiento y las anomalías
y_pred_train = clf.predict(X_train)
y_pred_outliers = clf.predict(X_outliers)

# Dibuja la línea, los puntos y el vector más cercano al plano
xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.title("Detección de anomalías con One-Class SVM")
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu)
a = plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
plt.contourf(xx, yy, Z, levels=[0, Z.max()], colors='palevioletred')

s = 40
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c='white', s=s, edgecolors='k')
b2 = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c='blueviolet', s=s, edgecolors='k')
plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend([a.collections[0], b1, b2],
           ["superficie de decisión", "observaciones de entrenamiento",
            "anomalías"],
           loc="upper left",
           prop=matplotlib.font_manager.FontProperties(size=11))
plt.savefig("./5/svm_plot.png")
