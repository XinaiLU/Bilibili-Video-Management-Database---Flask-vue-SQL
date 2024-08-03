<template>
  <div class="ordering">
    <div class="heading">Comments列表</div>
    <div class="content">
      <!-- 主要内容区域 -->
      <!-- ...其他内容... -->
    </div>

    <div class="side-by-side">


      <div class="Tags-table">
        <div class="row">
          <div class="col-sm-10">
            <alert :message=message v-if="showMessage"></alert>
            <!-- ...其他内容... -->
          </div>
        </div>

        <table class="table table-hover">
          <!-- ...原始的表格内容... -->
          <colgroup>
            <col style="width: auto;"> 
            <!-- ... 添加其他列 ... -->
          </colgroup>

          <thead>
            <tr>
              <th scope="col">Comment ID</th>
              <th scope="col">User name</th>
              <th scope="col">Comment Content</th>
              <th scope="col">Comment Time</th>
              <th scope="col">Tag Name</th>
              <th scope="col">Like Number</th>
              <th scope="col">Video URL</th>
              <th scope="col">Video Caption</th>
              <th scope="col">Actions</th>

            </tr>
          </thead>
          <tbody>
            <tr v-for="(comment, index) in Comments" :key="index" :class="{ 'small-font': 1 }">
              <td>{{ comment.comment_id }}</td>
              <td>{{ comment.user_name }}</td>
              <td>{{ comment.comment_content }}</td>
              <td>{{ comment.comment_time }}</td>
              <td>{{ comment.tag_name }}</td>
              <td>{{ comment.comment_like_num }}</td>
              <td>{{ comment.video_url }}</td>
              <td>{{ comment.video_caption }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm" @click="toggleEditBookModal(video)">
                    Update
                  </button>
                  <button type="button" class="btn btn-danger btn-sm" @click="handleDeleteBook(video)">
                    Delete
                  </button>
                </div>
              </td>

            </tr>
          </tbody>
        </table>
      </div>


    </div>
  </div>
</template>
  
<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      Comments: []
    };
  },
  components: {
    alert: Alert,
  },

  methods: {
    getComments() {
      const path = 'http://localhost:5001/comments';
      axios.get(path)
        .then((res) => {
          this.Comments = res.data.Comments;
        })
        .catch((error) => {
          console.error(error);
        });
    }
  },
  created() {
    this.getComments();
  }

}
</script>
  
<style>
.small-font {
  font-size: 10px;
}

.alternate-color {
  background-color: rgba(251, 114, 153, 0.4);
}

.table th {
  font-size: 12px;
}

/* .container {
      display: flex;
      justify-content: space-between;
      background-image: url('blueblbl.jpg');  /* 这里假设你的图片位于 assets 文件夹中 */
/* background-repeat: no-repeat;
      background-size: 10%;
      background-position: center;
  } */


.content {
  flex: 1;
}

.side-by-side {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
}

.hotlist {
  width: 170px;
  /* border-left: 1px solid #ccc; */
  padding-left: 30px;
  margin-bottom: 20px;
  /* 添加此行以在下方留出空间 */
}

.Tags-table {
  flex: 1;
  margin-left: 10px;
}
</style>
  
<style>
body {
  background-image: url('blueblbl.jpg');
  background-repeat: no-repeat;
  background-position: top center;
  background-attachment: fixed;
  background-size: cover;
  z-index: 10;
  /* 确保它的z-index是一个较高的值，使其与其他元素重叠 */
  background-color: rgba(255, 255, 255, 0.1);
  /* 添加透明度 */
}

html,
body {
  height: 100%;
  margin: 0;
  padding: 0;
}
</style>