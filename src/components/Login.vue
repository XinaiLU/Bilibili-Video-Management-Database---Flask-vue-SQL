<template>
    <div class="login-container">
      <form @submit.prevent="login" class="login-form">
        <div class="form-header">
          <h2>登录</h2>
        </div>
        <div class="form-group">
          <label for="username">账号：</label>
          <input type="text" id="username" v-model="username" required>
        </div>
        <div class="form-group">
          <label for="password">密码：</label>
          <input type="password" id="password" v-model="password" required>
        </div>
        <div class="form-footer">
            <button @click="login" class="action-button">登录</button>
            <button @click="navigateToSetup" class="action-button">注册</button>
        </div>

      </form>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        username: '',
        password: ''
      };
    },
    methods: {
      login() {
        // 这里可以添加登录逻辑，例如发送登录请求到服务器
        // 登录成功后可以使用如下方式跳转到 /video 页面
        this.$router.push('/videos');
      },
      navigateToSetup() {
        // 跳转到 setup 页面
        this.$router.push('/setup');
      }
    }
  };
  </script>
  
  <style scoped>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* 使其占据整个视口高度 */
    /* background-color: #f4f4f4; 可选：为背景设置一个浅灰色 */
  }
  
  .login-form {
    width: 300px;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* 添加阴影效果 */
    background-color: #f4f4f4; /* 白色背景 */
  }
  
  h2 {
    text-align: center;
    margin-bottom: 20px;
    color: #333333; /* 黑色文字 */
  }
  
  input[type="text"],
  input[type="password"] {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
    border: 1px solid #ccc;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: rgba(35, 173, 229, 0.8); /* 蓝色按钮 */
    color: #ffffff; /* 白色文字 */
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3; /* 深蓝色悬停状态 */
  }

  .register-button {
  margin-left: 10px; /* 为注册按钮添加一些间距 */
}

  

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

  .form-footer {
  display: flex;
  justify-content: space-between; /* 让按钮之间有空间 */
  margin-top: 20px;
}

.action-button {
  flex: 1; /* 使按钮平均占据可用空间 */
  margin: 0 5px; /* 为按钮添加一些左右间距 */
}

  
  </style>