from sklearn.linear_model import LinearRegression, Ridge, Lasso
import numpy as np


def model_ols(x_arr, y_arr):
    ols_model = LinearRegression()  # OLS - ordinary list squares
    ols_model.fit(x_arr, y_arr)
    new_values = np.array([[-1], [1]])
    x_test_extended = np.append(x_arr, new_values, axis=0)
    y_ols_pred = ols_model.predict(x_test_extended)

    return x_test_extended, y_ols_pred


def model_ridge(x_arr, y_arr):
    ridge_model = Ridge(alpha=0.001)
    ridge_model.fit(x_arr, y_arr)
    new_values = np.array([[-1], [1]])
    x_test_extended = np.append(x_arr, new_values, axis=0)
    y_ridge_pred = ridge_model.predict(x_test_extended)

    return x_test_extended, y_ridge_pred


def model_lasso(x_arr, y_arr):
    lasso_model = Lasso(alpha=0.1)
    lasso_model.fit(x_arr, y_arr)
    new_values = np.array([[-1], [1]])
    x_test_extended = np.append(x_arr, new_values, axis=0)
    y_lasso_pred = lasso_model.predict(x_test_extended)

    return x_test_extended, y_lasso_pred



