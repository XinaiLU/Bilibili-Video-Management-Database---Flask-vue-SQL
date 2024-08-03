<template>
  <div class="container">
    <div class="content">
        <!-- 主要内容区域 -->
        <!-- ...其他内容... -->
    </div>
    
    <div class="side-by-side">


      <div class="videos-table">
        <div class="row">
          <div class="col-sm-10">
            <h1><center>BILIBILI 视频大赏</center></h1>
            <hr><br><br>
            <!-- hr是水平线 -->
            <alert :message=message v-if="showMessage"></alert>

        <div class="vvideolist">
          <h2>查询视频</h2>
          <!-- 添加一个表单，让用户输入一个数字和一个符号 -->
          <form @submit.prevent="getVideos">
            <label for="number">点赞率阈值：</label>
            <input type="number" id="number" v-model="number" min="0" max="1" step="0.01">
            <label for="symbol">标题符号：</label>
            <input type="text" id="symbol" v-model="symbol" maxlength="1">
            <button type="submit">查询</button>
          </form>
          <table class="table">
            <!-- ...其他内容... -->
            <thead>
              <tr>
                <th>Video ID</th>
                <th>标题</th>
                <th>点赞率</th>
                <!-- 其他表头列 -->
              </tr>
            </thead>
            <tbody>
              <!-- 修改v-for的绑定数组为filteredVideos -->
              <tr v-for="(video, index) in filteredVideos" :key="index">
                <td>{{ video.video_id }}</td>
                <td>{{ video.video_caption }}</td>
                <td>{{ video.like_rate }}</td>
              </tr>
            </tbody>
          </table>
        </div>



          <div>
            <input type="text" v-model="query" placeholder="Enter video ID">
            <button @click="search">Search</button>
            <div v-if="video" :key="video.video_id">
              <h2>{{ video.video_caption }}</h2>
              <p>Video URL: {{ video.video_url }}</p>
              <p>Video Length: {{ video.video_len }}</p>
              <p>Tag Name: {{ video.tag_name }}</p>
              <p>Vlogger Name: {{ video.vlogger_name }}</p>
              <p>Vlogger ID: {{ video.vlogger_id }}</p>
            </div>
            <p v-else>No video found</p>
          </div>

            
            
          
            <button
              type="button"
              class="btn btn-success btn-sm"
              @click="toggleAddBookModal">
              Add Video
            </button>

        <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">Video ID</th>
                <th scope="col">Caption</th>
                <th scope="col">Video URL</th>
                <th scope="col">Length</th>
                <th scope="col">Tag</th>
                <th scope="col">Vlogger Name</th>
                <th scope="col">Vlogger ID</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(video, index) in videos" :key="index">
                <td>{{ video.video_id }}</td>
                <td>{{ video.video_caption }}</td>
                <td>{{ video.video_url }}</td>
                <td>{{ video.video_len }}</td>
                <td>{{ video.tag_name }}</td>
                <td>{{ video.vlogger_name }}</td>
                <td>{{ video.vlogger_id }}</td>
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

            
          <!-- ...其他内容... -->
        </div>
      </div>
    </div>

    <!-- add new book modal -->
    <div
      ref="addBookModal"
      class="modal fade"
      :class="{ show: activeAddBookModal, 'd-block': activeAddBookModal }"
      tabindex="-1"
      role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a new video</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleAddBookModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addBookVideo_ID" class="form-label">Video ID:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookVideo_ID"
                  v-model="addBookForm.video_id"
                  placeholder="Enter Video ID">
              </div>
              <div class="mb-3">
                <label for="addBookCaption" class="form-label">Caption:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookCaption"
                  v-model="addBookForm.video_caption"
                  placeholder="Enter Caption">
              </div>
              <div class="mb-3">
                <label for="addBookVideo_URL" class="form-label">Video URL:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookVideo_URL"
                  v-model="addBookForm.video_url"
                  placeholder="Enter Video URL">
              </div>
              <div class="mb-3">
                <label for="addBookLength" class="form-label">Length:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookLength"
                  v-model="addBookForm.video_len"
                  placeholder="Enter Length">
              </div>
              <div class="mb-3">
                <label for="addBookTag" class="form-label">Tag:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookTag"
                  v-model="addBookForm.tag_name"
                  placeholder="Enter Tag">
              </div>
              <div class="mb-3">
                <label for="addBookVlogger_name" class="form-label">Vlogger Name:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookVlogger_name"
                  v-model="addBookForm.vlogger_name"
                  placeholder="Enter Vlogger Name">
              </div>
              <div class="mb-3">
                <label for="addBookVlogger_ID" class="form-label">Vlogger ID:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookVlogger_ID"
                  v-model="addBookForm.vlogger_id"
                  placeholder="Enter Vlogger ID">
              </div>
              
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleAddSubmit">
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleAddReset">
                  Reset
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddBookModal" class="modal-backdrop fade show">
    </div>

    <!-- edit book modal -->
    <div
      ref="editBookModal"
      class="modal fade"
      :class="{ show: activeEditBookModal, 'd-block': activeEditBookModal }"
      tabindex="-1"
      role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Update</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleEditBookModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="editBookVideo_ID" class="form-label">Video ID:</label>
                <input
                  type="number"
                  class="form-control"
                  id="editBookVideo_ID"
                  v-model="editBookForm.video_id"
                  placeholder="Enter Video ID">
              </div>
              <div class="mb-3">
                <label for="editBookCaption" class="form-label">Caption:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookCaption"
                  v-model="editBookForm.video_caption"
                  placeholder="Enter Caption">
              </div>
              <div class="mb-3">
                <label for="editBookVideo_URL" class="form-label">Video URL:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookVideo_URL"
                  v-model="editBookForm.video_url"
                  placeholder="Enter Video URL">
              </div>
              <div class="mb-3">
                <label for="editBookLength" class="form-label">Length:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookLength"
                  v-model="editBookForm.video_len"
                  placeholder="Enter Length">
              </div>
              <div class="mb-3">
                <label for="editBookTag" class="form-label">Tag:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookTag"
                  v-model="editBookForm.tag_name"
                  placeholder="Enter Tag">
              </div>
              <div class="mb-3">
                <label for="editBookVlogger_name" class="form-label">Vlogger Name:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookVlogger_name"
                  v-model="editBookForm.vlogger_name"
                  placeholder="Enter Vlogger Name">
              </div>
              <div class="mb-3">
                <label for="editBookVlogger_ID" class="form-label">Vlogger ID:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookVlogger_ID"
                  v-model="editBookForm.vlogger_id"
                  placeholder="Enter Vlogger ID">
              </div>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleEditSubmit">
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleEditCancel">
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeEditBookModal" class="modal-backdrop fade show">
  </div>

      <div class="hotlist">
          <!-- 热榜内容 -->
          <h2>热搜视频</h2>
          <table class="table">
            <!-- ...其他内容... -->
            <thead>
                <tr>
                    <th>Video ID</th>
                    <th>标题</th>
                    <th>播放量</th>
                    <!-- 其他表头列 -->
                </tr>
            </thead>
            <tbody>
              <tr v-for="(video, index) in hotvideos" :key="index">
                <td>{{ video.video_id }}</td>
                <td>{{ video.video_caption }}</td>
                <td>{{ video.play_num }}</td>
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

      query: '',
      video: null,
      activeAddBookModal: false,
      activeEditBookModal: false,
      
      addBookForm: {
        video_id: 0,
        video_caption: '',
        video_url: '',
        video_len: '',
        tag_name: '',
        vlogger_name: '',
        vlogger_id: '',
      },
      videos: [],
      hotvideos:[],
      filteredVideos: [], // 存储筛选后的视频信息的数组
      number: 0.1, // 存储用户输入的数字的变量
      symbol: "?", // 存储用户输入的符号的变量
      editBookForm: {
        video_id: 0,
        video_caption: '',
        video_url: '',
        video_len: '',
        tag_name: '',
        vlogger_name: '',
        vlogger_id: '',
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {

    search() {
      const path = `http://localhost:5001/videos/${this.query}`;
      axios.get(path)
        .then((res) => {
          this.video = res.data.data;
        })
        .catch((error) => {
          console.error(error);
          this.video = null;
        });
    },

    getVideos() {
        const path = `http://localhost:5001/filteredVideos?number=${this.number}&symbol=${this.symbol}`;
        // 发送GET请求
        axios
          .get(path)
          .then(res => {
            // 将返回的数据赋值给filteredVideos数组
            this.filteredVideos = res.data.filteredVideos;
          })
          .catch(error => {
            console.error(error);
          });
    },
    


    addBook(payload) {
      const path = 'http://localhost:5001/videos';
      axios.post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Video added!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getBooks();
        });
    },

    getBooks() {
      const path = 'http://localhost:5001/videos';
      axios.get(path)
        .then((res) => {
          this.videos = res.data.videos;
        })
        .catch((error) => {

          console.error(error);
        });
    },

    getHotBooks() {
      const path = 'http://localhost:5001/hotvideos';
      axios.get(path)
        .then((res) => {
          this.hotvideos = res.data.hotvideos;
        })
        .catch((error) => {

          console.error(error);
        });
    },

    

    handleAddReset() {
      this.initForm();
    },
    handleAddSubmit() {
      this.toggleAddBookModal();
      const payload = {
        video_id: this.addBookForm.video_id,
        video_caption: this.addBookForm.video_caption,
        video_url: this.addBookForm.video_url,
        video_len: this.addBookForm.video_len,
        tag_name: this.addBookForm.tag_name,
        vlogger_name: this.addBookForm.vlogger_name,
        vlogger_id: this.addBookForm.vlogger_id,
        // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    handleDeleteBook(databoard) {
      this.removeBook(databoard.video_id);
    },
    handleEditCancel() {
      this.toggleEditBookModal(null);
      this.initForm();
      this.getBooks(); // why?
    },
    handleEditSubmit() {
      this.toggleEditBookModal(null);
      const payload = {
        video_id: this.editBookForm.video_id,
        video_caption: this.editBookForm.video_caption,
        video_url: this.editBookForm.video_url,
        video_len: this.editBookForm.video_len,
        tag_name: this.editBookForm.tag_name,
        vlogger_name: this.editBookForm.vlogger_name,
        vlogger_id: this.editBookForm.vlogger_id,
      };
      this.updateBook(payload, this.editBookForm.video_id);
    },
    initForm() {
      this.addBookForm.video_id = 0;
      this.addBookForm.video_caption = '';
      this.addBookForm.video_url = '';
      this.addBookForm.video_len = '';
      this.addBookForm.tag_name = '';
      this.addBookForm.vlogger_name = '';
      this.addBookForm.vlogger_id = '';
      this.editBookForm.video_id = 0;
      this.editBookForm.video_caption = '';
      this.editBookForm.video_url = '';
      this.editBookForm.video_len = '';
      this.editBookForm.tag_name = '';
      this.editBookForm.vlogger_name = '';
      this.editBookForm.vlogger_id = '';
    },
    removeBook(videoID) {
      const path = `http://localhost:5001/videos/${videoID}`;
      axios.delete(path)
        .then(() => {
          this.getBooks();
          this.message = 'Video removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },

    
    
    toggleAddBookModal() {
      const body = document.querySelector('body');
      this.activeAddBookModal = !this.activeAddBookModal;
      if (this.activeAddBookModal) {
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
    toggleEditBookModal(video) {
      if (video) {
        this.editBookForm = video;
      }
      const body = document.querySelector('body');
      this.activeEditBookModal = !this.activeEditBookModal;
      if (this.activeEditBookModal) {
        body.classList.add('modal-open');
      } else{
        body.classList.remove('modal-open');
      }
    },
    updateBook(payload, videoID) {
      const path = `http://localhost:5001/videos/${videoID}`;
      axios.put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = 'Video updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },
  },
  

  created() {
    this.getBooks();
    this.search();
    this.getHotBooks();
    this.getVideos();
  },
};


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
    margin-bottom: 20px; /* 添加此行以在下方留出空间 */
}

.videos-table {
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

