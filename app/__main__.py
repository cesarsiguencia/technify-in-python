from __init__ import create_app
import pymysql

pymysql.install_as_MySQLdb()

create_app()
