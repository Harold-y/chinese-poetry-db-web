import opencc
import pymysql
from typing import List, Tuple


def s2t(chars: str) -> str:
    converter_s2t = opencc.OpenCC('s2t.json')
    return converter_s2t.convert(chars)


def t2s(chars: str) -> str:
    converter_t2s = opencc.OpenCC('t2s.json')
    return converter_t2s.convert(chars)


def db_get_conn(host='127.0.0.1', user='root', passwd='root', db='chinese-poetry-collection',
                port=3306) -> pymysql.connections:
    conn = pymysql.connect(host=host, user=user, passwd=passwd, db=db, port=port)
    return conn


def db_select(query_str: str) -> Tuple[int, List[dict]]:
    conn = db_get_conn()
    cur = conn.cursor(pymysql.cursors.DictCursor)
    res_num = cur.execute(query_str)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return res_num, data


def search_poem(query_str: str = None, query_type: str = "title", items_per_page: int = 100,
                curr_page: int = 1) -> dict:
    res = {
        'num_res': 0,
        'result': [],
        'code': 0,
        'msg': ''
    }
    added_ids = set()
    if query_str is None or query_str == '' or query_str == ' ':
        res['code'] = -1
        res['msg'] = 'Empty Query'
        return res
    simplified = t2s(query_str)
    traditional = s2t(query_str)
    str_choice = [simplified, traditional]
    for chars in str_choice:
        if query_type == "title":
            query_s = f"SELECT p.p_id, p.p_title, a.a_id, a.a_name, r.r_id, r.r_name, p.p_paragraph " \
                      f"FROM poetry as p " \
                      f" LEFT JOIN author as a ON p.p_author_id = a.a_id " \
                      f" LEFT JOIN rhythmic as r ON p.p_rhythmic_id = r.r_id " \
                      f"WHERE p.p_title like '%{chars}%' LIMIT {(curr_page - 1) * items_per_page}, {items_per_page}"
        elif query_type == "para":
            query_s = f"SELECT p.p_id, p.p_title, a.a_id, a.a_name, r.r_id, r.r_name, p.p_paragraph " \
                      f"FROM poetry as p " \
                      f" LEFT JOIN author as a ON p.p_author_id = a.a_id " \
                      f" LEFT JOIN rhythmic as r ON p.p_rhythmic_id = r.r_id " \
                      f"WHERE p.p_paragraph like '%{chars}%' LIMIT {(curr_page - 1) * items_per_page}, {items_per_page}"
        elif query_type == "rhy":
            query_s = f"SELECT p.p_id, p.p_title, a.a_id, a.a_name, r.r_id, r.r_name, p.p_paragraph " \
                      f"FROM poetry as p " \
                      f" LEFT JOIN author as a ON p.p_author_id = a.a_id " \
                      f" LEFT JOIN rhythmic as r ON p.p_rhythmic_id = r.r_id " \
                      f"WHERE r.r_name like '%{chars}%' LIMIT {(curr_page - 1) * items_per_page}, {items_per_page}"
        elif query_type == "author":
            query_s = f"SELECT p.p_id, p.p_title, a.a_id, a.a_name, r.r_id, r.r_name, p.p_paragraph " \
                      f"FROM poetry as p " \
                      f" LEFT JOIN author as a ON p.p_author_id = a.a_id " \
                      f" LEFT JOIN rhythmic as r ON p.p_rhythmic_id = r.r_id " \
                      f"WHERE a.a_name like '%{chars}%' LIMIT {(curr_page - 1) * items_per_page}, {items_per_page}"
        else:
            res['code'] = -1
            res['msg'] = 'Unsupported Query Type'
            return res
        res_s = db_select(query_s)
        for poem in res_s[1]:
            if poem['p_id'] in added_ids:
                pass
            else:
                res['result'].append(poem)
                res['num_res'] += 1
                added_ids.add(poem['p_id'])
    return res


def query_poem_by_id(p_id: int) -> dict:
    query_s = f"SELECT p.p_id, p.p_title, a.a_id, a.a_name, d.d_name, r.r_id, r.r_name, c.c_name, p.p_paragraph, p.p_note, p.p_img_path " \
              f"FROM poetry as p " \
              f"LEFT JOIN author as a ON p.p_author_id = a.a_id " \
              f"LEFT JOIN rhythmic as r ON p.p_rhythmic_id = r.r_id " \
              f"LEFT JOIN dynasty as d ON a.a_dynasty_id = d.d_id " \
              f"LEFT JOIN collection as c ON p.p_collection_id = c.c_id " \
              f"WHERE p.p_id = {p_id}"
    res_s = db_select(query_s)
    return res_s[1][0]


def search_author(query_str: str = None, items_per_page: int = 100, curr_page: int = 1) -> dict:
    res = {
        'num_res': 0,
        'result': [],
        'code': 0,
        'msg': ''
    }
    if query_str is None or query_str == '' or query_str == ' ':
        res['code'] = -1
        res['msg'] = 'Empty Query'
        return res
    added_ids = set()
    simplified = t2s(query_str)
    traditional = s2t(query_str)
    str_choice = [simplified, traditional]
    for chars in str_choice:
        query_s = f"SELECT a.a_id, a.a_name, d.d_id, d.d_name " \
                  f"FROM author as a LEFT JOIN dynasty as d ON d.d_id = a.a_dynasty_id WHERE " \
                  f"a.a_name like '%{chars}%' LIMIT {(curr_page - 1) * items_per_page}, {items_per_page}"
        res_s = db_select(query_s)
        for item in res_s[1]:
            if item['a_id'] in added_ids:
                pass
            else:
                res['result'].append(item)
                res['num_res'] += 1
                added_ids.add(item['a_id'])
    return res


def query_poem_by_author(a_id: int, items_per_page: int = 100, curr_page: int = 1) -> List[dict]:
    query_s = f"SELECT p.p_id, p.p_title, a.a_id, a.a_name, r.r_id, r.r_name, p.p_paragraph " \
              f"FROM poetry as p " \
              f" LEFT JOIN author as a ON p.p_author_id = a.a_id " \
              f" LEFT JOIN rhythmic as r ON p.p_rhythmic_id = r.r_id " \
              f"WHERE a.a_id = {a_id} LIMIT {(curr_page - 1) * items_per_page}, {items_per_page}"
    res_s = db_select(query_s)
    return res_s[1]


def display_author(items_per_page: int = 100) -> List[dict]:
    query_s = f"SELECT a.a_id, a.a_name, d.d_id, d.d_name " \
              f"FROM author as a LEFT JOIN dynasty as d ON d.d_id = a.a_dynasty_id " \
              f"ORDER BY RAND() LIMIT {items_per_page}"
    res_s = db_select(query_s)
    return res_s[1]


def display_rhythmic(items_per_page: int = 100, curr_page: int = 1) -> List[dict]:
    query_s = f"SELECT r.r_id, r.r_name, r.r_note, r.r_img_path FROM rhythmic as r " \
              f"LIMIT {(curr_page - 1) * items_per_page}, {items_per_page}"
    res_s = db_select(query_s)
    return res_s[1]


def search_rhythmic(r_name: str = None, items_per_page: int = 100, curr_page: int = 1) -> dict:
    res = {
        'num_res': 0,
        'result': [],
        'code': 0,
        'msg': ''
    }
    if r_name is None or r_name == '' or r_name == ' ':
        res['code'] = -1
        res['msg'] = 'Empty Query'
        return res
    simplified = t2s(r_name)
    traditional = s2t(r_name)
    added_ids = set()
    str_choice = [simplified, traditional]
    for chars in str_choice:
        query_s = f"SELECT r.r_id, r.r_name, r.r_note, r.r_img_path FROM rhythmic as r " \
                  f"WHERE r.r_name like '%{chars}%' " \
                  f"LIMIT {(curr_page - 1) * items_per_page}, {items_per_page}"
        res_s = db_select(query_s)
        for item in res_s[1]:
            if item['r_id'] in added_ids:
                pass
            else:
                res['result'].append(item)
                res['num_res'] += 1
                added_ids.add(item['r_id'])
    return res


def query_poem_by_rhythmic(r_id: int, items_per_page: int = 100, curr_page: int = 1) -> List[dict]:
    query_s = f"SELECT p.p_id, p.p_title, a.a_id, a.a_name, r.r_id, r.r_name, p.p_paragraph " \
              f"FROM poetry as p " \
              f" LEFT JOIN author as a ON p.p_author_id = a.a_id " \
              f" LEFT JOIN rhythmic as r ON p.p_rhythmic_id = r.r_id " \
              f"WHERE r.r_id = {r_id} LIMIT {(curr_page - 1) * items_per_page}, {items_per_page}"
    res_s = db_select(query_s)
    return res_s[1]


def display_collection() -> List[dict]:
    query_s = f"SELECT c_id, c_name, c_note FROM collection"
    res_s = db_select(query_s)
    return res_s[1]


def query_poem_by_collection(c_id: int, items_per_page: int = 100, curr_page: int = 1) -> List[dict]:
    query_s = f"SELECT p.p_id, p.p_title, a.a_id, a.a_name, r.r_id, r.r_name, p.p_paragraph " \
              f"FROM poetry as p " \
              f" LEFT JOIN author as a ON p.p_author_id = a.a_id " \
              f" LEFT JOIN rhythmic as r ON p.p_rhythmic_id = r.r_id " \
              f" LEFT JOIN collection as c ON p.p_collection_id = c.c_id " \
              f"WHERE c.c_id = {c_id} LIMIT {(curr_page - 1) * items_per_page}, {items_per_page}"
    res_s = db_select(query_s)
    return res_s[1]


def query_random_poem() -> dict:
    query_s = f"SELECT p.p_id FROM poetry as p ORDER BY RAND() LIMIT 1"
    p_id = db_select(query_s)[1][0]["p_id"]
    return query_poem_by_id(p_id)
