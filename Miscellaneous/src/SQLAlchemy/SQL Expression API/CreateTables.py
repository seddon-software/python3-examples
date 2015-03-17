from Setup import *


connection = engine.connect()

sequenceSQL =    """
    CREATE SEQUENCE "JAVA"."USERS_SEQ" MINVALUE 1000 MAXVALUE 999999999999999
    """
dropSequenceSQL =    """
    DROP SEQUENCE "JAVA"."USERS_SEQ"
    """
tableSQL = """
    CREATE TABLE "JAVA"."USERS"
    (
        "USER_ID"  NUMBER(*,0) NOT NULL ENABLE,
        "NAME"     VARCHAR2(40 CHAR),
        "AGE"      NUMBER(*,0),
        "PASSWORD" VARCHAR2(20 CHAR),
        PRIMARY KEY ("USER_ID") USING INDEX
    )
    """
dropTableSQL = """
    DROP TABLE "JAVA"."USERS"
    """

def executeSQL(SQL):
    try:
        connection.execute(SQL)
    except Exception, e:
        print e

executeSQL(dropSequenceSQL)
executeSQL(dropTableSQL)
executeSQL(sequenceSQL)
executeSQL(tableSQL)

connection.close()

1
