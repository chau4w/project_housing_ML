# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3


class CrawlDataPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connect("manga.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        # TODO: change table name
        self.curr.execute("""DROP TABLE IF EXISTS fantasy_tb""")

        # TODO: change table name
        self.curr.execute("""create table fantasy_tb(
            title text,
            read text,
            comment text, 
            heart text,
            new_chap text,
            time_new_chap text,
            url text
                            )""")
        self.conn.commit()

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        for i in range(len(item['read'])):

            # TODO: change table name
            self.curr.execute("""insert into fantasy_tb values(?, ?, ?, ?, ?, ?, ?)""", (
                item['title'][i],
                item['read'][i],
                item['comment'][i],
                item['heart'][i],
                item['new_chap'][i],
                item['time_new_chap'][i],
                item['url'][i]
            ))
            self.conn.commit()
