#
# Database access functions for the web forum.
# 

import time
import psycopg2

## Database connection
DB = []

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    
    dbConnection = psycopg2.connect("dbname=forum")
    
    dbCursor = dbConnection.cursor()
    query = "SELECT content, time FROM posts ORDER BY time DESC"
    dbCursor.execute(query)
    rows = dbCursor.fetchall()
    
    dbConnection.close()
    
    posts = [{'content': str(row[0]), 'time': str(row[1])} for row in rows]
    ##posts.sort(key=lambda row: row['time'], reverse=True)
    return posts    

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    
    ##t = time.strftime('%c', time.localtime())

    dbConnection = psycopg2.connect("dbname=forum")
    
    dbCursor = dbConnection.cursor()
    dbCursor.execute("INSERT INTO posts(content) VALUES(%s)", (content,))
    
    dbConnection.commit()
    dbConnection.close()
    
    ##DB.append((t, content))
