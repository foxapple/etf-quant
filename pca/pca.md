# 股票型态研究
## 型态分析数据源

整体实验结构，找到多种处理后的数据源
基础数据源：每日日线数据 开盘 收盘，最高，最低
处理方式

- 5天为一组
- 周一到周五为一行，如果周一到周五不够的就过滤掉
- 只计算每年 一个月的数据，周一到周五为一行

就按照这三个数据维度来进行计算


