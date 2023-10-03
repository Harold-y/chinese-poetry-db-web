import os
import re
from typing import List, Tuple
import json
import pymysql


def load_sub_dir(filepath: str) -> List[str]:
    dir_list = os.listdir(filepath)
    return dir_list


def read_json(filepath: str) -> List[dict]:
    f = open(filepath, encoding="utf-8")
    data = json.load(f)
    res = []
    for i in data:
        res.append(i)
    return res


def db_get_conn() -> pymysql.connections:
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='chinese-poetry-collection', port=3306)
    return conn


# e.g., (1, 'Test1', 1, None)
def db_select(query_str: str) -> List[Tuple]:
    conn = db_get_conn()
    cur = conn.cursor()
    res_num = cur.execute(query_str)
    res = []
    for r in cur:
        res.append(r)
    cur.close()
    conn.close()
    return res


def db_exec(exe_str: str, params: Tuple = None) -> int:
    conn = db_get_conn()
    cur = conn.cursor()
    if params is not None:
        res = cur.execute(exe_str, params)
    else:
        res = cur.execute(exe_str)
    conn.commit()
    cur.close()
    conn.close()
    return res


def load_poem(title: str = None, author_id: int = None, rhythmic_id: int = None, paragraph: str = None,
              note: str = None,
              collection_id: int = None, other: str = None, img_path: str = None) -> int:
    new_paragraph = ""
    for i in range(0, len(paragraph) - 1):
        new_paragraph += paragraph[i] + "\n"
    if len(paragraph) > 0:
        try:
            new_paragraph += paragraph[len(paragraph) - 1]
        except:
            print("error of load poem", paragraph)
    query = f"INSERT INTO poetry (p_title, p_author_id, p_rhythmic_id, p_paragraph, p_note, p_collection_id, p_other,\
     p_img_path) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    res = db_exec(query, (title, author_id, rhythmic_id, new_paragraph, note, collection_id, other, img_path))
    return res


def load_author(dynasty_id: int = None, author: str = None):
    res = db_select(f"SELECT * FROM author where a_name = '{author}'")
    if len(res) >= 1:
        return res[0][0]  # return the author's id
    else:
        if dynasty_id is None:
            res = db_exec(f"INSERT INTO author (a_name) values (%s,)", (author,))
        else:
            res = db_exec(f"INSERT INTO author (a_name, a_dynasty_id) values (%s, %s)", (author, dynasty_id))
        res = db_select(f"SELECT * FROM author where a_name = '{author}'")
        if len(res) >= 1:
            return res[0][0]  # return the author's id
        else:
            print("Error insert author")


def load_rhythmic(rhythmic_name: str, r_note: str = ''):
    res = db_select(f"SELECT * FROM rhythmic where r_name = '{rhythmic_name}'")
    if len(res) >= 1:
        return res[0][0]  # return the rhythmic id
    else:
        res = db_exec(f"INSERT INTO rhythmic (r_name, r_note) values (%s, %s)", (rhythmic_name, r_note))
        res = db_select(f"SELECT * FROM rhythmic where r_name = '{rhythmic_name}'")
        if len(res) >= 1:
            return res[0][0]  # return the rhythmic id
        else:
            print("Error insert rhythmic")


def load_collection(collection_name: str, c_note: str = ''):
    res = db_select(f"SELECT * FROM collection where c_name = '{collection_name}'")
    if len(res) >= 1:
        return res[0][0]  # return the collection id
    else:
        res = db_exec(f"INSERT INTO collection (c_name, c_note) values (%s, %s)", (collection_name, c_note))
        res = db_select(f"SELECT * FROM collection where c_name = '{collection_name}'")
        if len(res) >= 1:
            return res[0][0]  # return the collection id
        else:
            print("Error insert collection")


def load_tang_song_poems(parent: str = "./全唐诗/"):
    sub_files = load_sub_dir(parent)
    tang_jsons = []
    song_jsons = []
    for file_name in sub_files:
        tang_json = re.findall(r"(^poet\.tang\.\d+\.json$)", file_name)
        song_json = re.findall(r"(^poet\.song\.\d+\.json$)", file_name)
        if len(tang_json) > 0:
            tang_jsons.append(tang_json[0])
        if len(song_json) > 0:
            song_jsons.append(song_json[0])
    tang_jsons.sort()
    song_jsons.sort()
    d_id = 1
    for tang_json in tang_jsons:
        print(f"Processing {tang_json}")
        list_res = read_json(parent + tang_json)
        c_id = load_collection("唐宋诗")
        for poem in list_res:
            a_id = load_author(d_id, poem['author'])
            paragraphs = poem['paragraphs']
            try:
                if len(paragraphs) == 1 and paragraphs[0] == "。":
                    continue
            except:
                print("error when determine garbage")
            title = poem['title']
            load_poem(author_id=a_id, paragraph=paragraphs, title=title, collection_id=c_id)
    d_id = 2
    for song_json in song_jsons:
        print(f"Processing {song_json}")
        list_res = read_json(parent + song_json)
        c_id = load_collection("唐宋诗")
        for poem in list_res:
            a_id = load_author(d_id, poem['author'])
            paragraphs = poem['paragraphs']
            try:
                if len(paragraphs) == 1 and paragraphs[0] == "。":
                    continue
            except:
                print("error when determine garbage")
            title = poem['title']
            load_poem(author_id=a_id, paragraph=paragraphs, title=title, collection_id=c_id)


def load_song_ci(parent: str = "./宋词/"):
    sub_files = load_sub_dir(parent)
    song_jsons = []
    for file_name in sub_files:
        song_json = re.findall(r"(^ci\.song\.\d+\.json$)", file_name)
        if len(song_json) > 0:
            song_jsons.append(song_json[0])
    song_jsons.sort()
    d_id = 2
    for song_json in song_jsons:
        print(f"Processing {song_json}")
        list_res = read_json(parent + song_json)
        c_id = load_collection("宋词")
        for poem in list_res:
            a_id = load_author(d_id, poem['author'])
            paragraphs = poem['paragraphs']
            r_id = load_rhythmic(rhythmic_name=poem['rhythmic'])
            try:
                if len(paragraphs) == 1 and paragraphs[0] == "。":
                    continue
            except:
                print("error when determine garbage")

            load_poem(author_id=a_id, paragraph=paragraphs, rhythmic_id=r_id, collection_id=c_id)


def load_shijing(parent: str = "./诗经/"):
    shijing_json = "shijing.json"
    print(f"Processing {shijing_json}")
    list_res = read_json(parent + shijing_json)
    c_id = load_collection("诗经")
    for poem in list_res:
        title = poem['title']
        chapter = poem['chapter']
        section = poem['section']
        paragraphs = poem['content']
        r_id = load_rhythmic(rhythmic_name=chapter + "·" + section)
        try:
            if len(paragraphs) == 1 and paragraphs[0] == "。":
                continue
        except:
            print("error when determine garbage")

        load_poem(title=title, paragraph=paragraphs, rhythmic_id=r_id, collection_id=c_id, note=chapter + "·" + section)


def load_caocao(parent: str = "./曹操诗集/"):
    caocao_json = "caocao.json"
    print(f"Processing {caocao_json}")
    list_res = read_json(parent + caocao_json)
    c_id = load_collection("曹操诗集")
    d_id = 5
    for poem in list_res:
        title = poem['title']
        paragraphs = poem['paragraphs']
        a_id = load_author(d_id, "曹操")
        try:
            if len(paragraphs) == 1 and paragraphs[0] == "。":
                continue
        except:
            print("error when determine garbage")

        load_poem(title=title, paragraph=paragraphs, collection_id=c_id, author_id=a_id)


def load_wudai_huajianji(parent: str = "./五代诗词/huajianji/"):
    sub_files = load_sub_dir(parent)
    huajianji_jsons = []
    for file_name in sub_files:
        huajianji_json = re.findall(r"(^huajianji-\w+-juan\.json$)", file_name)
        if len(huajianji_json) > 0:
            huajianji_jsons.append(huajianji_json[0])
    huajianji_jsons.sort()
    d_id = 4
    for huajianji_json in huajianji_jsons:
        print(f"Processing {huajianji_json}")
        list_res = read_json(parent + huajianji_json)
        c_id = load_collection("五代 花间集")
        for poem in list_res:
            a_id = load_author(d_id, poem['author'])
            title = poem['title']
            paragraphs = poem['paragraphs']
            r_id = load_rhythmic(rhythmic_name=poem['rhythmic'])
            notes = poem['notes']
            new_notes = ""
            for i in range(0, len(notes) - 1):
                new_notes += notes[i] + "\n"
            if len(notes) > 0:
                try:
                    new_notes += notes[len(notes) - 1]
                except:
                    print("error of load poem", notes)
            try:
                if len(paragraphs) == 1 and paragraphs[0] == "。":
                    continue
            except:
                print("error when determine garbage")

            load_poem(author_id=a_id, paragraph=paragraphs, rhythmic_id=r_id, collection_id=c_id, title=title,
                      note=new_notes)


def load_wudai_nantang(parent: str = "./五代诗词/nantang/"):
    nantang_json = "poetrys.json"
    print(f"Processing {nantang_json}")
    list_res = read_json(parent + nantang_json)
    c_id = load_collection("五代 南唐")
    d_id = 4
    for poem in list_res:
        a_id = load_author(d_id, poem['author'])
        title = poem['title']
        paragraphs = poem['paragraphs']
        r_id = load_rhythmic(rhythmic_name=poem['rhythmic'])
        notes = poem['notes']
        new_notes = ""
        for i in range(0, len(notes) - 1):
            new_notes += notes[i] + "\n"
        if len(notes) > 0:
            try:
                new_notes += notes[len(notes) - 1]
            except:
                print("error of load poem", notes)
        try:
            if len(paragraphs) == 1 and paragraphs[0] == "。":
                continue
        except:
            print("error when determine garbage")

        load_poem(title=title, paragraph=paragraphs, collection_id=c_id, author_id=a_id, rhythmic_id=r_id,
                  note=new_notes)


def load_yuan_qu(parent: str = "./元曲/"):
    yuanqu_json = "yuanqu.json"
    print(f"Processing {yuanqu_json}")
    list_res = read_json(parent + yuanqu_json)
    c_id = load_collection("元曲")
    d_id = 3
    for poem in list_res:
        a_id = load_author(d_id, poem['author'])
        title = poem['title']
        paragraphs = poem['paragraphs']
        try:
            if len(paragraphs) == 1 and paragraphs[0] == "。":
                continue
        except:
            print("error when determine garbage")

        load_poem(title=title, paragraph=paragraphs, collection_id=c_id, author_id=a_id)


def load_chu_ci(parent: str = "./楚辞/"):
    chuci_json = "chuci.json"
    print(f"Processing {chuci_json}")
    list_res = read_json(parent + chuci_json)
    c_id = load_collection("楚辞")
    d_id = 6
    for poem in list_res:
        a_id = load_author(d_id, poem['author'])
        title = poem['title']
        paragraphs = poem['content']
        note = poem['section']
        try:
            if len(paragraphs) == 1 and paragraphs[0] == "。":
                continue
        except:
            print("error when determine garbage")

        load_poem(title=title, paragraph=paragraphs, collection_id=c_id, author_id=a_id, note=note)


def load_lun_yu(parent: str = "./论语/"):
    lunyu_json = "lunyu.json"
    print(f"Processing {lunyu_json}")
    list_res = read_json(parent + lunyu_json)
    c_id = load_collection("论语")
    d_id = 6
    for poem in list_res:
        a_id = load_author(d_id, "孔子及其弟子")
        title = poem['chapter']
        paragraphs = poem['paragraphs']
        try:
            if len(paragraphs) == 1 and paragraphs[0] == "。":
                continue
        except:
            print("error when determine garbage")

        load_poem(title=title, paragraph=paragraphs, collection_id=c_id, author_id=a_id)

def load_na_lan_xing_de(parent: str = "./纳兰性德/"):
    nalan_json = "纳兰性德诗集.json"
    print(f"Processing {nalan_json}")
    list_res = read_json(parent + nalan_json)
    c_id = load_collection("纳兰性德诗集")
    d_id = 7
    for poem in list_res:
        a_id = load_author(d_id, poem['author'])
        title = poem['title']
        paragraphs = poem['para']
        try:
            if len(paragraphs) == 1 and paragraphs[0] == "。":
                continue
        except:
            print("error when determine garbage")

        load_poem(title=title, paragraph=paragraphs, collection_id=c_id, author_id=a_id)


if __name__ == '__main__':
    load_tang_song_poems()
    load_song_ci()
    load_shijing()
    load_caocao()
    load_wudai_huajianji()
    load_wudai_nantang()
    load_yuan_qu()
    load_chu_ci()
    load_lun_yu()
    load_na_lan_xing_de()
    
