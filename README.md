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
`
1. Execute the chinese-poetry-collection_start.sql to generate a DB named "chinese-poetry-collection"
2. Move the db_loader.py inside the main folder of <a href="https://github.com/chinese-poetry/chinese-poetry/tree/master#chinese-poetry-%E6%9C%80%E5%85%A8%E4%B8%AD%E6%96%87%E8%AF%97%E6%AD%8C%E5%8F%A4%E5%85%B8%E6%96%87%E9%9B%86%E6%95%B0%E6%8D%AE%E5%BA%93">chinese-poetry</a> repository
`

## 数据库设计
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

