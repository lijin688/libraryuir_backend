from libraryuir.model.storage import *
from libraryuir.model import storage
import datetime
from sqlalchemy.orm import relationship


class Book(storage.ORMBase, storage.Base):
    __tablename__ = 'book'
    id = Column("id", Integer(unsigned=True), primary_key=True, autoincrement=True)
    book_name = Column("book_name", INTEGER(256), doc='书名')
    category = Column("category", String(256), doc='类别')
    res_num = Column("res_num", Integer(256), doc='剩余数量')
    pub_addr = Column("pub_addr", String(256), doc='出版地')
    in_time = Column("in_time", DateTime, doc='入管时间')

    created_time = Column("created_time", DateTime, default=datetime.datetime.now, doc='创建时间')
    modified_time = Column("modified_time", DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, doc='修改时间')
    # created_by = Column("created_by", String(256), doc='创建人')
    # modified_by = Column("modified_by", String(256), doc='修改人')

    def __repr__(self):
        return '<book:{}-[{}]>'.format(self.book_name, self.id)

    def to_dict(self):
        return {c.name: getattr(self, c.name, None) for c in self.__table__.columns}


