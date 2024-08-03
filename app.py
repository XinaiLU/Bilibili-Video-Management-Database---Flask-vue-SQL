from flask import Flask, jsonify, request
from flask_cors import CORS



import pymysql

VIDEOS = []
#Videos
def getBOOKsFromMysql():
    connect = pymysql.Connect(
     host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '2021201327wyy',
        db = 'bilibili',
        charset = 'utf8'
    ) #建立数据库连接
    cursor = connect.cursor()
    sql = 'select * from databoard'
    cursor.execute(sql)
    data = cursor.fetchall()
    result = []
    for i in range(len(data)):
        result.append({
            'video_id' : data[i][0],
            'video_caption' : data[i][1],
            'video_url' : data[i][2],
            'video_len' : data[i][3],
            'tag_name' : data[i][4],
            'vlogger_name' : data[i][5],
            'vlogger_id' : data[i][6]
        })
    print(result)
    cursor.close()
    connect.close()
    return result




#Videos
# 获取视频信息
def getVideosFromMysql(number, symbol):
  connect = pymysql.Connect(
     host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '2021201327wyy',
        db = 'bilibili',
        charset = 'utf8'
    ) #建立数据库连接
  cursor = connect.cursor()
  # 修改SQL语句，根据用户输入的参数来筛选视频
  sql = f"select video.video_id,video.video_caption,(like_num/play_num) as like_rate from video where (like_num/play_num) > {number} and video_caption like '%{symbol}%'"
  cursor.execute(sql)
  data = cursor.fetchall()
  result = []
  for i in range(len(data)):
    result.append(
      {
        "video_id": data[i][0],
        "video_caption": data[i][1],
        "like_rate": data[i][2],
      }
    )
  print(result)
  cursor.close()
  connect.close()
  return result


#Videos
#获取热门视频
def getHotVideosFromMysql():
    connect = pymysql.Connect(
     host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '2021201327wyy',
        db = 'bilibili',
        charset = 'utf8'
    ) #建立数据库连接
    cursor = connect.cursor()
    sql = 'select * from hot_video'
    cursor.execute(sql)
    data = cursor.fetchall()
    result = []
    for i in range(len(data)):
        result.append({
            'video_id' : data[i][0],
            'video_caption' : data[i][2],
            'play_num':data[i][4],
        })
    print(result)
    cursor.close()
    connect.close()
    return result



#Videos
def add_video (data):
    tag=0
    connect = pymysql.Connect(
                host = '127.0.0.1',
                port = 3306,
                user = 'root',
                passwd = '2021201327wyy',
                db = 'bilibili',
                charset = 'utf8'
                ) #建立数据库连接
    cursor = connect.cursor()
    sql = 'insert into databoard values(%s,%s,%s,%s,%s,%s,%s)'
    values = (data.get('video_id'),data.get('video_caption'),data.get('video_url'),data.get('video_len'),data.get('tag_name'),data.get('vlogger_name'),data.get('vlogger_id'))
    cursor.execute(sql,values)
    tag = cursor.fetchall()
    connect.commit()
    cursor.close()
    connect.close()
    return tag

# VIDEOS = [
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'On the Road',
#         'author': 'Jack Kerouac',
#         'read': True
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Harry Potter and the Philosopher\'s Stone',
#         'author': 'J. K. Rowling',
#         'read': False
#     },
#     {
#         'id': uuid.uuid4().hex,
#         'title': 'Green Eggs and Ham',
#         'author': 'Dr. Seuss',
#         'read': True
#     }
# ]



# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

#Vloggers
Vloggers = []

def getVloggersFromMysql():
    connect = pymysql.Connect(
     host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '2021201327wyy',
        db = 'bilibili',
        charset = 'utf8'
    ) #建立数据库连接
    cursor = connect.cursor()
    sql = 'select * from vlogger'
    cursor.execute(sql)
    data = cursor.fetchall()
    result = []
    for i in range(len(data)):
        result.append({
            'vlogger_name' : data[i][0],
            'vlogger_id' : data[i][1],
            'vlogger_url' : data[i][2]
        })
    print(result)
    cursor.close()
    connect.close()
    return result



#Tags
def getTagsFromMysql():
    connect = pymysql.Connect(
     host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '2021201327wyy',
        db = 'bilibili',
        charset = 'utf8'
    ) #建立数据库连接
    cursor = connect.cursor()
    sql = 'select * from tag'
    cursor.execute(sql)
    data = cursor.fetchall()
    result = []
    for i in range(len(data)):
        result.append({
            'tag_id' : data[i][0],
            'tag_name' : data[i][1],
        })
    print(result)
    cursor.close()
    connect.close()
    return result


#basic_videos
BASIC_VIEDOS = []
def getbasic_videosFromMysql():
    connect = pymysql.Connect(
     host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '2021201327wyy',
        db = 'bilibili',
        charset = 'utf8'
    ) #建立数据库连接
    cursor = connect.cursor()
    sql = 'select * from video'
    cursor.execute(sql)
    data = cursor.fetchall()
    result = []
    for i in range(len(data)):
        result.append({
            'video_id' : data[i][0],
            'video_url' : data[i][1],
            'video_caption' : data[i][2],
            'play_num' : data[i][3],
            'update_time ' : data[i][4],
            'like_num' : data[i][5],
            'vlogger_id ' : data[i][6],
            'video_len' : data[i][7],
            'tag_name' : data[i][8],
            'video_len_second' : data[i][9]
        })
    print(result)
    cursor.close()
    connect.close()
    return result

def add_basic_video (data):
    tag=0
    connect = pymysql.Connect(
                host = '127.0.0.1',
                port = 3306,
                user = 'root',
                passwd = '2021201327wyy',
                db = 'bilibili',
                charset = 'utf8'
                ) #建立数据库连接
    cursor = connect.cursor()
    sql = 'insert into video values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    values = (data.get('video_id'),data.get('video_url'),data.get('video_caption'),data.get('play_num'),data.get('update_time'),data.get('like_num'),data.get('vlogger_id'),data.get('rec_video_caption'),data.get('video_len'),data.get('tag_name'),data.get('video_len_second'))
    cursor.execute(sql,values)
    tag = cursor.fetchall()
    connect.commit()
    cursor.close()
    connect.close()
    return tag







#Comments
def getCommentsFromMysql():
    connect = pymysql.Connect(
     host = '127.0.0.1',
        port = 3306,
        user = 'root',
        passwd = '2021201327wyy',
        db = 'bilibili',
        charset = 'utf8'
    ) #建立数据库连接
    cursor = connect.cursor()
    sql = 'select * from comments'
    cursor.execute(sql)
    data = cursor.fetchall()
    result = []
    for i in range(len(data)):
        result.append({
            'comment_id' : data[i][0],
            'user_name' : data[i][1],
            'comment_content' : data[i][2],
            'comment_time' : data[i][3],
            'tag_name' : data[i][4],
            'comment_like_num' : data[i][5],
            'video_url' : data[i][6],
            'video_caption' : data[i][7]
        })
    print(result)
    cursor.close()
    connect.close()
    return result


#Videos
def remove_video(videoid):
    connect = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='2021201327wyy',
        db='bilibili',
        charset='utf8'
    )
    cursor = connect.cursor()

    try:
        sql = "DELETE FROM databoard WHERE video_id = %s;"
        cursor.execute(sql, (videoid,))
        connect.commit()

        if cursor.rowcount > 0:
            return True  # Video successfully deleted
        else:
            return False  # Video with the specified ID was not found
    except Exception as e:
        # Handle the exception (e.g., log the error, return False, etc.)
        return False
    finally:
        cursor.close()
        connect.close()




def update_video_in_database(video_id, data):
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='2021201327wyy',
            db='bilibili',
            charset='utf8'
        )
        with connection.cursor() as cursor:
            sql = 'UPDATE databoard SET video_caption=%s, video_url=%s, video_len=%s, tag_name=%s, vlogger_name=%s, vlogger_id=%s WHERE video_id=%s'
            values = (data.get('video_caption'), data.get('video_url'), data.get('video_len'), data.get('tag_name'), data.get('vlogger_name'), data.get('vlogger_id'), video_id)
            cursor.execute(sql, values)
            connection.commit()
            rows_affected = cursor.rowcount
        return True, None if rows_affected > 0 else (False, 'Video not found or update failed.')
    except Exception as e:
        return False, f'Database error: {str(e)}'
    finally:
        if connection:
            connection.close()


@app.route('/videos/<video_id>', methods=['PUT'])
def update_video(video_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        success, message = update_video_in_database(video_id, post_data)
        if success:
            response_object['message'] = 'Video updated!'
        else:
            response_object['status'] = 'error'
            response_object['message'] = message
    return jsonify(response_object)





@app.route('/videos', methods=['GET', 'POST'])
def all_videos():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # VIDEOS.append({
        #     'id': uuid.uuid4().hex,
        #     'title': post_data.get('title'),
        #     'author': post_data.get('author'),
        #     'read': post_data.get('read')
        # })
        print(post_data)
        add_video(post_data)
        response_object['message'] = 'Video added!'
    else:
        VIDEOS =getBOOKsFromMysql()
        response_object['videos'] = VIDEOS
    return jsonify(response_object)

@app.route('/videos/<video_id>', methods=['PUT', 'DELETE'])
def single_video(video_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        VIDEOS.append({
            
            'video_id' : post_data.get('video_id'),
            'video_caption' : post_data.get('video_caption'),
            'video_url' : post_data.get('video_url'),
            'video_len' : post_data.get('video_len'),
            'tag_name' : post_data.get('tag_name'),
            'vlogger_name' : post_data.get('vlogger_name'),
            'vlogger_id' : post_data.get('vlogger_id'),
        })
        response_object['message'] = 'Video updated!'
        
    if request.method == 'DELETE':
        if remove_video(video_id):
            response_object['message'] = 'Video removed!'
        else:
            response_object['message'] = 'Video with id {} not found'.format(video_id)
    return jsonify(response_object)

@app.route('/vlogger', methods=['GET', 'POST'])
def all_vloggers():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # VIDEOS.append({
        #     'id': uuid.uuid4().hex,
        #     'title': post_data.get('title'),
        #     'author': post_data.get('author'),
        #     'read': post_data.get('read')
        # })
        print(post_data)
        # add_vlogger(post_data)
        # response_object['message'] = 'Video added!'
    else:
        Vloggers =getVloggersFromMysql()
        response_object['vloggers'] = Vloggers
    return jsonify(response_object)

@app.route('/tags', methods=['GET', 'POST'])
def all_tags():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # VIDEOS.append({
        #     'id': uuid.uuid4().hex,
        #     'title': post_data.get('title'),
        #     'author': post_data.get('author'),
        #     'read': post_data.get('read')
        # })
        print(post_data)
        add_video(post_data)
        # response_object['message'] = 'Video added!'
    else:
        Tags =getTagsFromMysql()
        response_object['Tags'] = Tags
    return jsonify(response_object)

@app.route('/basic_videos', methods=['GET', 'POST'])
def all_basic_videos():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # VIDEOS.append({
        #     'id': uuid.uuid4().hex,
        #     'title': post_data.get('title'),
        #     'author': post_data.get('author'),
        #     'read': post_data.get('read')
        # })
        print(post_data)
        add_basic_video(post_data)
        # response_object['message'] = 'Video added!'
    else:
        basic_videos =getbasic_videosFromMysql()
        response_object['basic_videos'] = basic_videos
    return jsonify(response_object)

@app.route('/comments', methods=['GET', 'POST'])
def all_comments():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # VIDEOS.append({
        #     'id': uuid.uuid4().hex,
        #     'title': post_data.get('title'),
        #     'author': post_data.get('author'),
        #     'read': post_data.get('read')
        # })
        print(post_data)
        add_video(post_data)
        # response_object['message'] = 'Video added!'
    else:
        Comments =getCommentsFromMysql()
        response_object['Comments'] = Comments
    return jsonify(response_object)



def get_video_from_database(video_id):
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='2021201327wyy',  
            db='bilibili',
            charset='utf8'
        )
        with connection.cursor() as cursor:
            sql = 'SELECT video.video_id, video.video_caption,video.video_url,video.video_len,video.tag_name,vlogger.vlogger_name,vlogger.vlogger_id FROM video natural join vlogger where video_id=%s'
            cursor.execute(sql, (video_id,))
            result = cursor.fetchone()
            if result:
                video = {
                    'video_id': result[0],
                    'video_caption': result[1],
                    'video_url': result[2],
                    'video_len': result[3],
                    'tag_name': result[4],
                    'vlogger_name': result[5],
                    'vlogger_id': result[6]
                }
                return True, video
            else:
                return False, 'Video not found'
    except Exception as e:
        return False, f'Database error: {str(e)}'
    finally:
        if 'connection' in locals():
            connection.close()


def get_basic_video_from_database(video_id):
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='2021201327wyy',  
            db='bilibili',
            charset='utf8'
        )
        with connection.cursor() as cursor:
            sql = 'SELECT * FROM video WHERE video_id=%s'
            cursor.execute(sql, (video_id,))
            result = cursor.fetchone()
            if result:
                basic_video = {
                    
                    'video_id' : result[0],
                    'video_url' : result[1],
                    'video_caption' : result[2],
                    'play_num' : result[3],
                    'update_time ' : result[4],
                    'like_num' : result[5],
                    'vlogger_id ' : result[6],
                    'rec_video_caption':result[7],
                    'video_len' : result[8],
                    'tag_name' : result[10],
                    'video_len_second' : result[9]
                }
                return True, basic_video
            else:
                return False, 'Video not found'
    except Exception as e:
        return False, f'Database error: {str(e)}'
    finally:
        if 'connection' in locals():
            connection.close()



@app.route('/videos/<video_id>', methods=['GET'])
def get_video(video_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        success, data = get_video_from_database(video_id)
        if success:
            response_object['data'] = data
        else:
            response_object['status'] = 'error'
            response_object['message'] = data
    return jsonify(response_object)


@app.route('/basic_videos/<basic_video_id>', methods=['GET'])
def get_basic_video(basic_video_id):
    response_object = {'status': 'success'}
    if request.method == 'GET':
        success, data = get_basic_video_from_database(basic_video_id)
        if success:
            response_object['data'] = data
        else:
            response_object['status'] = 'error'
            response_object['message'] = data
    return jsonify(response_object)





# 展示视频信息
@app.route('/filteredVideos', methods=["GET"])
def f_videos():
  # 获取请求参数
  number = request.args.get("number")
  symbol = request.args.get("symbol")
  # 调用函数，获取视频信息
  f_response_object = {"status": "success"}
  FVIDEOS = getVideosFromMysql(number, symbol)
  f_response_object['filteredVideos'] = FVIDEOS
  return jsonify(f_response_object)


#展示热搜视频
@app.route('/hotvideos', methods=['GET'])
def hot_videos():
    hot_response_object = {'status': 'success'}
    HOTVIDEOS =getHotVideosFromMysql()
    hot_response_object['hotvideos'] = HOTVIDEOS
    return jsonify(hot_response_object)



if __name__ == '__main__':
    app.run()
