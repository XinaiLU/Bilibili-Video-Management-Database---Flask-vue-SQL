## Bilibili Video Dynamic Web Programming Experiment
--- 
<img src="https://github.com/user-attachments/assets/88fa9158-fcaa-4e9e-9367-7f1051a628cf" width="250" height="150">
<img src="https://github.com/user-attachments/assets/3d137532-f24f-4c74-9b4e-bb2bb1e75383" width="250" height="150">


## Objective

Master the framework of dynamic web programming and implement the application of databases in web programming.

## Content and Requirements

### Experiment Content

Based on the chosen research object and scenario (videos, patents, corporate innovation, etc.), design a database application system and implement it using a dynamic web programming framework (Vue + Flask-restful + MySQL).

### Experiment Requirements

1. Define at least three stored procedures or functions, including at least one scheduled task.
2. Design a data dashboard to display data from the database.
3. Integrate the content from Comprehensive Experiments 1 and 2 into the framework.
4. Provide test cases.
5. Advanced requirement: Support dynamic interactions.

## Key Points and Challenges

- **Key Points**: Web programming, database application, backend operations on databases.
- **Challenges**: Dynamic interaction.

---

## Experiment Report

### Title

Bilibili Video Dynamic Web Programming Experiment

### Experiment Environment

- **Computer Configuration**:
  - CPU: AMD Ryzen 7 5800H with Radeon Graphics
  - Base Speed: 3.20 GHz
  - Sockets: 1
  - Cores: 8
  - Logical Processors: 16
- **Operating System**: Windows 10 Home 64-bit
- **RDBMS Version**: MySQL 8.0.34

---

## Experiment Content

### 1. Define at least three stored procedures or functions, including at least one scheduled task

#### 1. Move videos before a given date to an inactive video tracking table (inactive_video)

```sql
CREATE TABLE IF NOT EXISTS inactive_video (
  video_id INT PRIMARY KEY AUTO_INCREMENT,
  video_url VARCHAR(250) UNIQUE,
  video_caption VARCHAR(500),
  vlogger_id VARCHAR(250),
  play_num INT CHECK (play_num >= 0),
  like_num INT CHECK (like_num >= 0),
  update_time DATETIME CHECK (update_time >= '2009-06-26'),
  rec_video_caption VARCHAR(250),
  video_len VARCHAR(20),
  video_len_second INT CHECK (video_len_second > 0),
  tag_name VARCHAR(5)
);

DELIMITER //

CREATE PROCEDURE video_date_track (given_day DATETIME)
BEGIN
  INSERT INTO inactive_video SELECT * FROM video WHERE update_time < given_day;
  DELETE FROM video WHERE video_id IN (SELECT video_id FROM inactive_video);
END //

DELIMITER ;

CALL video_date_track('2018-10-30');

-- Test case
SELECT * FROM video ORDER BY update_time ASC;
SELECT * FROM inactive_video;

-- Restore sample
INSERT INTO video SELECT * FROM inactive_video;
```

#### 2. Count the number of videos under a specific tag

```sql
DELIMITER //

CREATE PROCEDURE count_tag (tag_label VARCHAR(50))
BEGIN
  SELECT COUNT(*) FROM video WHERE tag_name = tag_label;
END //

DELIMITER ;

CALL count_tag('Technology');
```

#### 3. Create a hot video table that updates every minute (scheduled task)

```sql
SET GLOBAL event_scheduler = ON;

CREATE TABLE IF NOT EXISTS hot_video_table (
  video_id INT DEFAULT NULL,
  video_caption VARCHAR(100) DEFAULT NULL,
  play_num INT DEFAULT NULL
);

DELIMITER //

CREATE PROCEDURE refresh_hot_video()
BEGIN
  DELETE FROM hot_video_table;
  INSERT INTO hot_video_table (video_id, video_caption, play_num)
  (SELECT video_id, video_caption, play_num FROM video ORDER BY play_num DESC LIMIT 10);
END //

DELIMITER ;

DELIMITER //

CREATE EVENT refresh_hot_video_every_minute
  ON SCHEDULE
  EVERY 1 MINUTE
  DO CALL refresh_hot_video();

DELIMITER ;

-- Test case
SELECT * FROM hot_video_table;
```

### Front-End Design

#### (1) Login Interface (to be completed)

Components:

- **Input Fields**

```html
<label for="username">Username:</label>
<label for="password">Password:</label>
```

- **Navigation Buttons**

```html
<div class="form-footer">
  <button @click="login" class="action-button">Login</button>
  <button @click="navigateToSetup" class="action-button">Register</button>
</div>

methods: {
  login() {
    this.$router.push('/videos');
  },
  navigateToSetup() {
    this.$router.push('/setup');
  }
}
```

- **Theme Background**: Uses Bilibili-themed images to match the video management system.

### Data Dashboard

The dashboard is divided into three parts: a sidebar (aside), a right-side header, and the main content area. The sidebar is used for panel switching, displaying data analysis results, data management options, account management, and exception tracking.

---

## System Features

### (1) Query

1. **Single Table Query**

Function: Query video information where the like rate exceeds a threshold and the title contains a specific symbol.

```sql
SELECT video_id, video_caption, (like_num / play_num) AS like_rate
FROM databoard
WHERE (like_num / play_num) > threshold AND video_caption LIKE '%symbol%';
```

- Test Case: Threshold = 0.05, Symbol = "?"

2. **Multi-Table Query**

Function: Query video and vlogger information for a specific VideoID.

```sql
SELECT video.video_id, video.video_caption, video.video_url, video.video_len, video.tag_name, vlogger.vlogger_name, vlogger.vlogger_id
FROM video
NATURAL JOIN vlogger
WHERE video_id = %s;
```

- Test Case: VideoID = 35

---

### (2) Triggers + Insert Function

1. **Define Trigger**

```sql
CREATE TABLE IF NOT EXISTS track_ab_video_table (
  video_id INT,
  video_caption VARCHAR(500),
  video_url VARCHAR(50)
);

DELIMITER //

CREATE TRIGGER track_ab_video BEFORE INSERT ON databoard
FOR EACH ROW
BEGIN
  IF (NEW.video_id < 0) THEN
    INSERT INTO track_ab_video_table (video_id, video_caption, video_url)
    VALUES (NEW.video_id, NEW.video_caption, NEW.video_url);
  END IF;
END //

DELIMITER ;
```

- **Test Case**

```sql
INSERT INTO databoard VALUES (
  '-1',
  'Alchemy Secret Science and Technology #Alchemy #Physics #SciFi',
  'https://www.bilibili.com/video/BV1Zu411F769/-1',
  '0:34:33',
  'Food Test',
  'Universe',
  '674379847'
);
```

2. **Add Function**

```sql
INSERT INTO video VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
```

- Test Case: 666, "Test", "http", "0:30:00", "Tech", "user", 888

### (3) Update Function

```python
def update_video_in_database(video_id, data):
    try:
        connection = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='your_key',
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
```

### (4) Delete Function

```python
def remove_video(videoid):
    connect = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='your_key',
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
        return False
    finally:
        cursor.close()
        connect.close()
```

---

## Experiment Summary

Through this experiment, we built a more complete Bilibili video database management system based on previous work. This includes defining stored procedures and functions, a scheduled task, and multiple data dashboards. We used the Flask + Vue framework to display database data and implement dynamic CRUD operations. This experiment deepened our understanding of database systems and provided a solid foundation for future studies.


<img width="303" alt="image" src="https://github.com/user-attachments/assets/88fa9158-fcaa-4e9e-9367-7f1051a628cf">

<img width="385" alt="image" src="https://github.com/user-attachments/assets/3d137532-f24f-4c74-9b4e-bb2bb1e75383">

<img width="386" alt="image" src="https://github.com/user-attachments/assets/2441abc3-1cb9-4772-82f1-3f753045d13c">

<img width="386" alt="image" src="https://github.com/user-attachments/assets/6fa0748f-3386-4907-b6cc-851deea7cb63">

<img width="386" alt="image" src="https://github.com/user-attachments/assets/99f16fd4-35c3-44fe-9968-0b812cef2bed">

<img width="386" alt="image" src="https://github.com/user-attachments/assets/ccd15321-e474-4700-a2c7-03656c362d13">

<img width="371" alt="image" src="https://github.com/user-attachments/assets/e1274b7c-f665-4b2c-8ab7-9d7b6f083c5a">

![image](https://github.com/user-attachments/assets/50acd290-ad7a-4bbc-bc8f-5b5a8b23e91c)
