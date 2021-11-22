import pymysql
import json
import logging

import middleware.context as context

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def _get_db_connection():

    db_connect_info = context.get_db_info()

    logger.info("RDBService._get_db_connection:")
    logger.info("\t HOST = " + db_connect_info['host'])

    db_info = context.get_db_info()
    db_connection = pymysql.connect(
       **db_info
    )
    return db_connection


def get_by_prefix(db_schema, table_name, column_name, value_prefix):

    conn = _get_db_connection()
    cur = conn.cursor()

    sql = "select * from " + db_schema + "." + table_name + " where " + \
        column_name + " like " + "'" + value_prefix + "%'"
    print("SQL Statement = " + cur.mogrify(sql, None))

    res = cur.execute(sql)
    res = cur.fetchall()

    conn.close()

    return res


def create_order(db_schema, table_name, order_id, product_id, price, customer_id, customer_name, date):

    conn = _get_db_connection()
    cur = conn.cursor()

    sql = "INSERT INTO " + db_schema + "." + table_name + "(order_id, product_id, price, customer_id, customer_name, date) \
    VALUES (" + order_id + ", '" + product_id + "', '" + price + "', '" + customer_id + "', '" + customer_name + "', '" + date + "');"
    print(sql)

    res = cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res


def _get_where_clause_args(template):

    terms = []
    args = []
    clause = None

    if template is None or template == {}:
        clause = ""
        args = None
    else:
        for k,v in template.items():
            terms.append(k + "=%s")
            args.append(v)

        clause = " where " +  " AND ".join(terms)


    return clause, args


def find_by_template(db_schema, table_name, template, field_list):

    wc,args = _get_where_clause_args(template)

    conn = _get_db_connection()
    cur = conn.cursor()

    sql = "select * from " + db_schema + "." + table_name + " " + wc
    res = cur.execute(sql, args=args)
    res = cur.fetchall()

    conn.close()

    return res


def delete_order(db_schema, table_name, order_id):

    conn = _get_db_connection()
    cur = conn.cursor()

    sql = "DELETE FROM " + db_schema + "." + table_name + " WHERE order_id = " + order_id

    res = cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res


def update_order(db_schema, table_name, order_id, product_id, price, customer_id, customer_name, date):

    conn = _get_db_connection()
    cur = conn.cursor()

    sql = "UPDATE " + db_schema + "." + table_name + " SET product_id = " + product_id + ", price = " + price + ", customer_id = " + customer_id + ", customer_name = " + customer_name + ", date = " + date + " WHERE order_id = " + order_id + ";"
    print(sql)

    res = cur.execute(sql)
    res = cur.fetchall()
    conn.commit()
    conn.close()
    return res