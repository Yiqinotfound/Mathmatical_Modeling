# 在python包statsmodels中有以holtwinters命名的module，支持一次、二次、三次平滑。
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

# 创建时间序列数据
dates = pd.date_range('20210101', periods=12, freq='M')
data = np.array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32])
noise = np.random.normal(0, 2, 12)
data = data + noise
# 创建指数平滑模型
model = ExponentialSmoothing(data, trend='add', seasonal=None)

# 拟合模型并进行预测
fit = model.fit()
forecast = fit.forecast(2)
fitted = fit.fittedvalues
all_data = np.append(fitted, forecast)
forecast_dates = pd.date_range('20210101', periods=14, freq='M')
# 绘制时间序列图
# plt.plot(dates, data, label='Actual')
# plt.plot(dates,fit.fittedvalues, label='Fitted')
# plt.plot(forecast_dates, forecast, label='Forecast')
plt.plot(dates,data,label = 'Actual')
plt.plot(forecast_dates,all_data,label = 'Forecast')
plt.legend()
plt.show()