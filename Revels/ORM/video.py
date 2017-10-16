from ORM.dbconnect import Connector;

class VideoManager():

    def __init__(self):

        #initiates the database Connector
        self.conn = Connector()

    def createTable(self):

        self.conn.query("""
            CREATE TABLE IF NOT EXISTS Video (
              video_id INTEGER AUTO_INCREMENT,
              title    VARCHAR(200) NOT NULL,
              descr    TEXT(1000),
              url      VARCHAR(200) NOT NULL,
              img      VARCHAR(200) NOT NULL,
              user_id  INT          NOT NULL,

              PRIMARY KEY (video_id),
              UNIQUE (user_id, url, title, img),
              FOREIGN KEY (user_id) REFERENCES User (user_id)
            );
            """)


    def insert(self,data):
        self.conn.query("""
            INSERT INTO Video(title, descr, url, img, user_id) VALUES (%s,%s,%s,%s,%s)
            """ ,data['title'],data['descr'],data['url'],data['img'],int(data['user_id']))
        self.conn.commit()

    def update(self,data):
        self.conn.query("""
            UPDATE Video SET title ="%s",descr ="%s",url ="%s",img ="%s",user_id ="%d"
            WHERE video_id = %d;
            """,data['video_id'],data['title'],data['descr'],data['url'],data['img'],data['user_id'] )
        self.conn.commit()

    def remove(self,data):
        self.conn.query("""
            DELETE FROM Video WHERE video_id = %d
        """ , data['video_id'])
        self.__del__()
