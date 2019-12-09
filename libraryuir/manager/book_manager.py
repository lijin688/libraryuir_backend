from libraryuir.model.storage import SessionMaker
from libraryuir.model.book import Book
from libraryuir.common.utils import get_one


class BookManager:

    @classmethod
    def query_book(cls, book_name=None):
        with SessionMaker() as session:
            query = session.query(Book)
            if book_name:
                query = query.filter(Book.book_name == book_name)
            return query.all()

    @classmethod
    def add_book(cls, book_name, category, res_num, pub_addr, in_time):
        metric = get_one(cls.query_book(book_name=book_name))
        if metric is not None:
            raise Exception(400, '已存在')
        c = Book()
        c.book_name = book_name
        c.category = category
        c.res_num = res_num
        c.pub_addr = pub_addr
        c.in_time = in_time
        c.add()
        return c.id

    @classmethod
    def delete_book(cls, id):
        with SessionMaker() as session:
            session.query(Book).filter(Book.id == id).delete()

    @classmethod
    def update_book(cls, id, book_name, category, res_num, pub_addr, in_time):
        with SessionMaker() as session:
            b = session.query(Book).get(id)
            b.book_name = book_name
            b.category = category
            b.res_num = res_num
            b.pub_addr = pub_addr
            b.in_time = in_time
            b.add()

if __name__ == '__main__':
    # r = BookManager.query_book('测试')
    BookManager.add_book('book_3', '2', 4, '吉林', '2019-11-20')
    # BookManager.update_book(2, 'book_1', 2, 4, '山东', '2019-11-20')
    # print(r)
