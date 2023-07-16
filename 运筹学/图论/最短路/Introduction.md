## 单源最短路求解：

- Dijkstra算法：适用于边权值非负的图
- Bellman-Ford算法：适用于边权值为任意实数的图

```python
for k:=1 to n-1 do
  for 每条边(u,v) do
    if ($dist(u)<INFINITY$) and ($dist(v)>dist(u)+w(u,v)$) then
      dist(v):=dist(u)+w(u,v)
```
## 多源最短路问题求解：

- Floyd-warshall算法
- Johnson算法

