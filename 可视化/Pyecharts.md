  [Pyecharts 文档](https://05x-docs.pyecharts.org/#/)

```python
from pyecharts.charts import Bar
from pyecharts import options as opts
```

- global_opts()：全局配置项
- series_opts()：系列配置项:文字、标签等等

## 地理空间可视化

```python
from pyecharts.charts import Geo
from pyecharts import options as opts

data = [('广州', 100), ('北京', 200), ('上海', 300), ('深圳', 400), ('香港', 500), ('澳门', 600)]

chart = (
    Geo()
    .add_schema(maptype="china") # 地图类型
    .add("geo", data) # 添加图表名称，传入数据集，选择geo图类型，调整图例...
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False)) # 系列配置
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="Geo-基本示例"),
    ) # 全局配置
)

chart.render('geo.html')
```

map 和 bmap 差不多

