import psycopg2


class DB:
    def __init__(self):
        self.conn = None
        try:
            # connect to the PostgreSQL server
            print('Connecting to the PostgreSQL database...')
            self.conn = psycopg2.connect(host="localhost", database="testcase", user="postgres", password="Cv121189mav")
            # create a cursor
            self.cur = self.conn.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def __del__(self):
        self.cur.close()
        self.conn.commit()
        if self.conn is not None:
            self.conn.close()
            print('Database connection closed.')

    def create_group_table(self):
        self.cur.execute(
            'CREATE TABLE "group" '
            '("id" integer NOT NULL PRIMARY KEY, '
            '"title" varchar(155) NOT NULL);'
        )

    def create_user_table(self):
        self.cur.execute(
            'CREATE TABLE "user" ('
            '"id" integer NOT NULL PRIMARY KEY, '
            '"login" varchar(255) NOT NULL, '
            '"password" varchar(255) NOT NULL, '
            '"name" varchar(25) NOT NULL, '
            '"surname" varchar(25) NOT NULL, '
            '"logo" varchar(100) NOT NULL);'
        )

    def create_users_groups_table(self):
        self.cur.execute(
            'CREATE TABLE "users_groups" ('
            '"id" integer NOT NULL PRIMARY KEY, '
            '"user_id" integer NOT NULL REFERENCES '
            '"user" ("id") DEFERRABLE INITIALLY DEFERRED, '
            '"group_id" integer NOT NULL REFERENCES '
            '"group" ("id") DEFERRABLE INITIALLY DEFERRED);'
            
        )


if __name__ == '__main__':
    run_script = DB()
    run_script.create_user_table()
    run_script.create_group_table()
    run_script.create_users_groups_table()
