from flask import Flask, jsonify
import flask
from flask_cors import CORS, cross_origin

from db_backend import *

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return "<p>Backend Active</p>"


@app.route("/search/poem", methods=['GET'])
@cross_origin()
def search_poem_controller():
    args = dict(flask.request.args)
    query_str = args['query_str']
    query_type = args['query_type']
    items_per_page = int(args.get('items_per_page', 100))
    curr_page = int(args.get('curr_page', 1))

    return jsonify(search_poem(query_str, query_type, items_per_page, curr_page))


@app.route("/query/poem_by_id", methods=['GET'])
@cross_origin()
def query_poem_by_id_controller():
    args = dict(flask.request.args)
    p_id = int(args['p_id'])

    return jsonify(query_poem_by_id(p_id))


@app.route("/search/author", methods=['GET'])
@cross_origin()
def search_author_controller():
    args = dict(flask.request.args)
    query_str = args['query_str']
    items_per_page = int(args.get('items_per_page', 100))
    curr_page = int(args.get('curr_page', 1))

    return jsonify(search_author(query_str, items_per_page, curr_page))


@app.route("/query/poem_by_author", methods=['GET'])
@cross_origin()
def query_poem_by_author_controller():
    args = dict(flask.request.args)
    a_id = args['a_id']
    items_per_page = int(args.get('items_per_page', 100))
    curr_page = int(args.get('curr_page', 1))

    return jsonify(query_poem_by_author(a_id, items_per_page, curr_page))


@app.route("/display/author", methods=['GET'])
@cross_origin()
def display_author_controller():
    args = dict(flask.request.args)
    items_per_page = int(args.get('items_per_page', 100))
    return jsonify(display_author(items_per_page))


@app.route("/display/rhythmic", methods=['GET'])
@cross_origin()
def display_rhythmic_controller():
    args = dict(flask.request.args)
    items_per_page = int(args.get('items_per_page', 100))

    return jsonify(display_rhythmic(items_per_page))


@app.route("/search/rhythmic", methods=['GET'])
@cross_origin()
def search_rhythmic_controller():
    args = dict(flask.request.args)
    r_name = args['r_name']
    items_per_page = int(args.get('items_per_page', 100))
    curr_page = int(args.get('curr_page', 1))

    return jsonify(search_rhythmic(r_name, items_per_page, curr_page))


@app.route("/query/poem_by_rhythmic", methods=['GET'])
@cross_origin()
def query_poem_by_rhythmic_controller():
    args = dict(flask.request.args)
    r_id = int(args['r_id'])
    items_per_page = int(args.get('items_per_page', 100))
    curr_page = int(args.get('curr_page', 1))

    return jsonify(query_poem_by_rhythmic(r_id, items_per_page, curr_page))


@app.route("/display/collection", methods=['GET'])
@cross_origin()
def display_collection_controller():
    return jsonify(display_collection())


@app.route("/query/poem_by_collection", methods=['GET'])
@cross_origin()
def query_poem_by_collection_controller():
    args = dict(flask.request.args)
    c_id = int(args['c_id'])
    items_per_page = int(args.get('items_per_page', 100))
    curr_page = int(args.get('curr_page', 1))

    return jsonify(query_poem_by_collection(c_id, items_per_page, curr_page))


@app.route("/query/random_poem", methods=['GET'])
@cross_origin()
def query_random_poem_controller():
    return jsonify(query_random_poem())


if __name__ == '__main__':
    app.run()
