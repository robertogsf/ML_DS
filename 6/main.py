from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Carga el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Divide el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crea el modelo de Random Forest
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Entrena el modelo
clf.fit(X_train, y_train)

# Realiza predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Imprime el informe de clasificación
print(classification_report(y_test, y_pred))
