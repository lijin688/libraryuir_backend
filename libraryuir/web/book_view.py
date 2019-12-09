from flask import request, redirect, url_for, abort, Blueprint, make_response
from flask import Blueprint, request, jsonify, abort, g
from libraryuir.manager.book_manager import BookManager

import logging
logger = logging.getLogger('uir')
views = Blueprint('app', __name__)


@views.route('/user/listpage', methods=['GET'])
def query_book():
    logger.info('请求url:{}, data:{}'.format(request.url, request.json))
    params = request.args

    book_name = params.get('book_name')
    all = BookManager.query_book(book_name)
    books = []
    for one in all:
        books.append({
            'id': one.id,
            'name': one.book_name,
            'addr': one.pub_addr,
            'resNum': one.res_num,
            'inLibDate': one.in_time,
            'ctg': one.category
        })
    data = {
        'total': len(all),
        'users': books
    }
    return jsonify({'code': 0, 'message': '操作成功', 'data': data})

@views.route('/user/remove', methods=['POST'])
def remove_book():
    print('请求url:{}, data:{}'.format(request.url, request.json))

    params = request.get_json()
    id = params.get('id')
    # BookManager.delete_book(id)
    print("删除成功")
    return jsonify({'code': 0, 'message': '操作成功', 'data': {}})


@views.route('/user/edit', methods=['POST'])
def edit_book():
    print('请求url:{}, data:{}'.format(request.url, request.json))

    params = request.get_json()
    id = params.get('id')
    book_name = params.get('name')
    category = params.get('ctg')
    res_num = params.get('resNum')
    pub_addr = params.get('addr')
    in_time = params.get('inLibDate')

    BookManager.update_book(id, book_name, category, res_num, pub_addr, in_time)
    print("更新成功")
    return jsonify({'code': 0, 'message': '操作成功', 'data': {}})


@views.route('/user/add', methods=['POST'])
def add_book():
    print('请求url:{}, data:{}'.format(request.url, request.json))

    params = request.get_json()
    book_name = params.get('name')
    category = params.get('ctg')
    res_num = params.get('resNum')
    pub_addr = params.get('addr')
    in_time = params.get('inLibDate')

    BookManager.add_book(book_name, category, res_num, pub_addr, in_time)
    print("新增成功")
    return jsonify({'code': 0, 'message': '操作成功', 'data': {}})


@views.route('/login', methods=['POST'])
def user_login():
    print('请求url:{}, data:{}'.format(request.url, request.json))

    params = request.get_json()
    username = params.get('username')
    password = params.get('password')

    resp = jsonify({'code': 200, 'message': '操作成功', 'user': {
        'avatar': "http://sc.07fly.net/uploads/allimg/160129/214145J54-0.png",
        'id': 1,
        'name': "张某某",
        'username': "admin"
    }})

    if username == 'admin' and password == '123456':
        return resp
    else:
        resp.status_code = 401
        return resp

