#!/usr/bin/python
#coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import select
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import Column
from sqlalchemy import BigInteger, SmallInteger, DateTime

Base = declarative_base()

class News(Base):
     
    __tablename__ = 'news'
    nid = Column(BigInteger, primary_key=True)
    uid = Column(BigInteger)
    is_delete = Column(SmallInteger)
    create_time = Column(DateTime)
    reply_time = Column(DateTime)


def _create_engine(user, password, host, port, db, autocommit=False, pool_recycle=60):
    engine = create_engine('mysql://%s:%s@%s:%s/%s?charset=utf8&use_unicode=1' % (
         user, password,
         host, port,
         db),
         pool_size=10,
         max_overflow=-1,
         pool_recycle=pool_recycle,
         connect_args={'connect_timeout': 1, 'autocommit': 1 if autocommit else 0})
    return engine


def _query(engine, sql):
     connection = engine.connect()
     result = connection.execute(sql)
     connection.close()
     return result


if __name__ == '__main__':
    engine = _create_engine('root', 'root', '127.0.0.1', '3306', 'gossip_test')
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    '''
    sql = 'select nid, uid from news limit 10'
    result = db_session.execute(sql)
    '''
    nids = [61L, 103L]
    news = db_session.query(News.nid)\
                .filter(News.nid.in_(nids))\
                .all()
    wrapper = set(news)   
    print wrapper
    print 103L in wrapper
    '''
    sql = 'select * from news limit 10'
    result = _query(engine, sql)
    for row in result:
        print row
    '''
