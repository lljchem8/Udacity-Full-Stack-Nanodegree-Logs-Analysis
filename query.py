#!/usr/bin/env python3

import psycopg2

dbName = "news"

query_one_desc = "What are the most popular three articles of all time?"
query_one = """select articles.slug, count(*) as view
from log join articles
 on log.path like concat('%', articles.slug, '%')
 group by articles.slug
 order by view desc
 limit 3;"""

qeury_two_desc = "Who are the most popular article authors of all time?"
query_two = """
select authors.name, count(*) as num
 from authors join articles
 on authors.id = articles.author
 join log on log.path like concat('%', articles.slug, '%')
 group by authors.name
 order by num desc;
"""

query_three_desc = "On which days did more than 1% of requests lead to errors?"
query_three = """
select *
from (select date(time), round(100*sum(case when status like concat('200', '%')
    then 0 else 1 end)/round(count(date(time)), 2), 1)
    as error_perc
    from log
    group by date(time)
    order by error_perc desc)
as sub_table
where error_perc > 1
"""


def connect_db(dbName):
    try:
        db = psycopg2.connect(database=dbName)
        return db
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


def close_db(db):
    if (db):
        db.close()


def get_query(cursor, query, query_desc):
    print("%s\n" % (query_desc))
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    return results


def output_format1(results):
    """
    format: var1(string) --- var2(int)
    """
    for row in results:
        print("%s  --  %d views" % (row[0], row[1]))
    print('\n')


def output_format2(results):
    """
    format example: 2016-07-17 --- 2.3 %
    """
    for row in results:
        print(str(row[0]) + ' --- ' + str(row[1]) + ' %')
    print('\n\n\n')


if __name__ == '__main__':
    db = connect_db(dbName)

    results = get_query(db, query_one, query_one_desc)
    output_format1(results)

    results = get_query(db, query_two, qeury_two_desc)
    output_format1(results)

    results = get_query(db, query_three, query_three_desc)
    output_format2(results)

    close_db(db)
