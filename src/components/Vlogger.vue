<template>
    <div class="ordering">
      <div class="heading">UP主列表</div>
      <div class="content">
          <!-- 主要内容区域 -->
          <!-- ...其他内容... -->
      </div>
      
      <div class="side-by-side">
  
  
        <div class="vloggers-table">
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
                <th scope="col">Vlogger Name</th>
                <th scope="col">Vlogger ID</th>
                <th scope="col">Vlogger URL</th>
                <th scope="col">Actions</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(vlogger,index) in vloggers" 
              :key="index" 
              :class="{'small-font': 1}"
              >
                <td>{{ vlogger.vlogger_name}}</td>
                <td>{{ vlogger.vlogger_id}}</td>
                <td>{{ vlogger.vlogger_url}}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button
                      type="button"
                      class="btn btn-warning btn-sm"
                      @click="toggleEditBookModal(video)">
                      Update
                    </button>
                    <button
                      type="button"
                      class="btn btn-danger btn-sm"
                      @click="handleDeleteBook(video)">
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
        vloggers: []
      };
    },
    
    components: {
      alert: Alert,
    },
    
    methods: {
      getvloggers() {
        const path = 'http://localhost:5001/vlogger';
        axios.get(path)
          .then((res) => {
            this.vloggers = res.data.vloggers;
          })
          .catch((error) => {
            console.error(error);
          });
      }
    },
    
    created() {
    this.getvloggers();
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


<style>
.ordering {
    position: absolute;
    top: 50px;
    left: 200px;
    right: 0;
    padding: 10px 0;
    margin: 0 auto;
    max-width: 1400px;
}

.heading {
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 30px;
    margin-left: 50px;
}
</style>