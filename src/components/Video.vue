<template>
    <div class="ordering">
        <div class="heading">视频列表</div>
        <el-main style="flex: 1; height: 100%;">
            <el-scrollbar>
                <el-table :data="videos" style="width: 100%; height: 100%;" :row-key="row => row.video_id">
                    <el-table-column label="Video ID" prop="video_id" width="90"></el-table-column>
                    <el-table-column label="Caption" prop="video_caption"></el-table-column>
                    <el-table-column label="Video URL" prop="video_url"></el-table-column>
                    <el-table-column label="Length" prop="video_len"></el-table-column>
                    <el-table-column label="Tag" prop="tag_name"></el-table-column>
                    <el-table-column label="Vlogger Name" prop="vlogger_name"></el-table-column>
                    <el-table-column label="Vlogger ID" prop="vlogger_id"></el-table-column>
                    <el-table-column label="Actions" width="200">

                        <div class="btn-group" role="group">
                            <el-button type="warning" @click="toggleEditBookModal(scope.row)" title="Update Video"
                                aria-label="Update Video" style="background-color: red;">
                                Update
                            </el-button>
                            <el-button type="danger" @click="handleDeleteBook(scope.row)" title="Delete Video"
                                aria-label="Delete Video">
                                Delete
                            </el-button>
                        </div>

                    </el-table-column>


                </el-table>
            </el-scrollbar>
        </el-main>
    </div>
</template>


<script>
import { onMounted, reactive } from 'vue'
import { Menu as IconMenu, Message, Setting } from '@element-plus/icons-vue'
import axios from 'axios'
import Alert from './Alert.vue'
import { ElAside, ElMenu, ElMenuItem } from 'element-plus';
// import {urls} from './api.js'
// import { modeget, modepost } from './request.js';
export default {
    //     setup(){
    //         onMounted(()=>{
    //             videolist()
    //         })
    //         async function videolist() {
    //             try{
    //                 const res = await new proxy.$request(proxy.$urls.m().pullvideolist).modeget()
    //                 console.log(res);
    //             }catch(e){
    //                 console.error(e);
    //         }
    //     }
    //     const res=reactive([])
    //     return {res,onMounted,onMounted}
    // },

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
            hotvideos: [],
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
            const path = `http://localhost:5001/videos${this.query}`;
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
            } else {
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
../../api/api.js