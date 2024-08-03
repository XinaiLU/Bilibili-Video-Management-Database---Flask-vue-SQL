<template>
    <div class="container">
      <div class="content">
          <!-- 主要内容区域 -->
          <!-- ...其他内容... -->
      </div>
      
      <div class="side-by-side">
  
  
        <div class="vloggers-table">
          <div class="row">
            <div class="col-sm-10">
              <h1><center>Videos</center></h1>
              <hr><br><br>
              <!-- hr是水平线 -->
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
                <th scope="col">Video ID</th>
                
                <th scope="col">Video URL</th>
                <th scope="col">Caption</th>
                <th scope="col">Play Number</th>
                <th scope="col">Update Time</th>
                <th scope="col">Like Number</th>
                <th scope="col">Vlogger ID</th>
                <th scope="col">Rec Caption</th>

                <th scope="col">Length</th>
                <th scope="col">Tag</th>
                <th scope="col">Length in Second</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(video,index) in basic_videos" 
              :key="index" 
              :class="{'small-font': 1}"
              >
                <td>{{ video.video_id }}</td>
                <td>{{ video.video_url }}</td>
                <td>{{ video.video_caption }}</td>
                <td>{{ video.play_num }}</td>
                <td>{{ video.update_time }}</td>
                <td>{{ video.like_num }}</td>
                <td>{{ video.vlogger_id }}</td>

                <td>{{ video.video_len}}</td>
                <td>{{ video.tag_name}}</td>
                <td>{{ video.video_len_second}}</td>

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
        basic_videos: []
      };
    },
    
    components: {
      alert: Alert,
    },
    
    methods: {
      getbasic_videos() {
        const path = 'http://localhost:5001/basic_videos';
        axios.get(path)
          .then((res) => {
            this.basic_videos = res.data.basic_videos;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    
    created() {
    this.getbasic_videos();
    }
  };
  </script>
  
  <style>
  .small-font {
    font-size: 10px;
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
      margin-bottom: 20px; /* 添加此行以在下方留出空间 */
  }
  
  .vloggers-table {
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
    z-index: 10; /* 确保它的z-index是一个较高的值，使其与其他元素重叠 */
    background-color: rgba(255, 255, 255, 0.1); /* 添加透明度 */
  }
  
  html, body {
    height: 100%;
    margin: 0;
    padding: 0;
  }
  
  </style>