# chinese-poetry-db-web：一个基于chinese-poetry的数据库和网页UI

## 鸣谢
<a href="https://github.com/chinese-poetry/chinese-poetry/tree/master#chinese-poetry-%E6%9C%80%E5%85%A8%E4%B8%AD%E6%96%87%E8%AF%97%E6%AD%8C%E5%8F%A4%E5%85%B8%E6%96%87%E9%9B%86%E6%95%B0%E6%8D%AE%E5%BA%93">chinese-poetry: 最全中文诗歌古典文集数据库</a>

## 包含
- 唐宋诗
- 宋词
- 曹操诗集
- 五代 花间集
- 五代 南唐
- 元曲
- 楚辞
- 论语
- 纳兰性德

## 使用方法
1. 利用chinese-poetry-collection_start.sql导入到一个叫做"chinese-poetry-collection"的MySQL数据库
2. 安装必要依赖：flask, opencc, pymysql
3. 将db_loader.py放在<a href="https://github.com/chinese-poetry/chinese-poetry/tree/master#chinese-poetry-%E6%9C%80%E5%85%A8%E4%B8%AD%E6%96%87%E8%AF%97%E6%AD%8C%E5%8F%A4%E5%85%B8%E6%96%87%E9%9B%86%E6%95%B0%E6%8D%AE%E5%BA%93">chinese-poetry</a>仓库的主文件夹并且执行db_loader.py
```
xxx/chinese-poetry$user-1> python3 db_loader.py
```
3. 在本仓库进行：后端（flask），启动！
```
xxx/chinese-poetry-db-web$user-1> python3 server.py
```

## 数据库设计
使用MySQL
<img src="./ERM.JPG" style="height:500px; width: 9000px">

Poetry:
- p_id: 诗词Id
- p_title: 诗词标题
- p_author_id: 作者Id，连表查询时使用，对应author表a_id
- p_rhythmic_id: 词牌/旋律Id，连表查询时使用，对应rhythmic表r_id
- p_paragraph: 正文
- p_note: 注释
- p_collection_id: 诗集/文集Id，连表查询时使用，对应Collection表c_id
- p_other: 闲置
- p_img_path: 后续配图使用路径

Author:
- a_id: 作者Id
- a_name: 作者姓名（e.g., 李白）
- a_dynasty_id: 朝代Id，连表查询时使用，对应dynasty表d_id
- a_img_path: 后续配图使用路径

Dynasty:
- d_id: 朝代Id
- d_name: 朝代名称（e.g., 宋朝）
- d_img_path: 后续配图使用路径

Collection:
- c_id: 诗集/文集Id
- c_name: 诗集/文集名称（e.g., 宋词）
- c_note: 详情

Rhythmic:
- r_id: 词牌/旋律Id
- r_name: 词牌/旋律名称（e.g., 青玉案）
- r_note: 详情
- r_img_path: 后续配图使用路径

## 后端
server.py，使用Flask制成，全部方法为GET

#### /search/poem
通过字符串查询 诗词
参数：
- query_str：查询字符串
- query_type：查询模式，必须为"title"（标题查询）, "para"（正文查询）, "rhy"（词牌/韵律查询）, 或"author"（作者查询）其中一种
- items_per_pag：每页查询个数
- curr_page：目前页数（从1开始）

#### /search/author
通过字符串查询 作者
参数：
- query_str：查询字符串
- items_per_pag：每页查询个数
- curr_page：目前页数（从1开始）

#### /search/rhythmic
通过字符串查询 词牌/韵律
参数：
- r_name：查询字符串
- items_per_pag：每页查询个数
- curr_page：目前页数（从1开始）

#### /query/poem_by_id
通过poem的Id查询完整的 诗词信息
参数：
- p_id：poem的Id

#### /query/poem_by_author
通过author的Id查询 诗词列表
参数：
- a_id：author的Id
- items_per_pag：每页查询个数
- curr_page：目前页数（从1开始）

#### /query/poem_by_rhythmic
通过rhythmic的Id查询 诗词列表
参数：
- r_id：rhythmic的Id
- items_per_pag：每页查询个数
- curr_page：目前页数（从1开始）

#### /query/poem_by_collection
通过collection的Id查询 诗词列表
参数：
- c_id：collection的Id
- items_per_pag：每页查询个数
- curr_page：目前页数（从1开始）

#### /display/rhythmic
获取rhythmic 列表
参数：
- items_per_pag：每页查询个数
- curr_page：目前页数（从1开始）

#### /display/collection
获取collection 列表
参数：
- 无

