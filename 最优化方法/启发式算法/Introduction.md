- 爬山法：该算法每次从当前解的临近解空间中选择一个最优解作为当前解，直至达到一个局部最优解。

- 模拟退火：模拟退火算法与爬山法类似，但是它没有选择最佳的移动，而是选择随机的移动。如果该移动使情况得到改善，那么接受该移动；否则，算法以某个概率接受该移动。因此有可能会跳出这个局部的最优解，达到全局的最优解。

- 禁忌搜索：禁忌搜索算法通过引入一个灵活的存储结构和相应的禁忌准则来避免迂回搜索，并通过藐视准则来赦免一些被禁忌的优良状态，进而保证多样化的有效探索以最终实现全局优化。

- 遗传算法等：该算法通过数学的方式,利用计算机仿真运算,将问题的求解过程转换成类似生物进化中的染色体基因的交叉、变异等过程。在求解较为复杂的组合优化问题时,相对一些常规的优化算法,通常能够较快地获得较好的优化结果。