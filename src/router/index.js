import { createRouter, createWebHistory } from 'vue-router'
import Videos from '../components/Videos.vue'
import Ping from '../components/Ping.vue'
import HelloWorld from '../components/HelloWorld.vue'
import Login from '../components/Login.vue'
import HomeView from '../components/HomeView.vue'
import Video from '../components/Video.vue'
import Vlogger from '../components/Vlogger.vue'
import Tags from '../components/Tags.vue'
import Comments from '../components/Comments.vue'
import basic_videos from '../components/basic_videos.vue'
import ab_video from '../components/ab_video.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView,
      redirect: '/ab_video',
      // 二级路由
      children: [
        {
          // 视频列表
          path: '/video',
          name: 'video',
          component: Video,
        },
        {
          // UP主列表
          path: '/vlogger',
          name: 'vlogger',
          component: Vlogger,
        },
        {//Tag列表
          path : '/tags',
          name : ' Tags',
          component :Tags
        },
        {//Comments列表
          path : '/comments',
          name : ' Comments',
          component :Comments
        },
        {//ab_video
          path : '/ab_video',
          name : ' ab_video',
          component :ab_video
        }
      ]
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/videos',
      name: 'videos',
      component: Videos,
    },
    {
      path: '/ping',
      name: 'ping',
      component: Ping
    },
    {
      path: '/Helloworld',
      name: 'HelloWorld',
      component: HelloWorld
    },

    {
      path : '/basic_videos',
      name : ' basic_videos',
      component :basic_videos
    },
  ]
});    

export default router