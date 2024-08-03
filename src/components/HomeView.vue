<template>
    <el-container class="layout-container-demo" style="height: 500px">
        <el-aside width="200px" :style="{ height: '100vh' }">
            <el-menu :default-active="1">
                <div v-for="(item, index) in menu" :key="index">

                    <el-menu-item v-if="item.Subclass.length == 0" :index="item.id">
                        <template #title>
                            <el-icon>
                                <component :is="item.icon"></component>
                            </el-icon>
                            <span>{{ item.title }}</span>
                        </template>
                    </el-menu-item>

                    <el-sub-menu v-if="item.Subclass.length > 0" :index="item.id">
                        <template #title>
                            <el-icon>
                                <component :is="item.icon"></component>
                            </el-icon>
                            <span>{{ item.title }}</span>
                        </template>
                        <div v-for="(two, index_two) in item.Subclass" :key="index_two">
                            <el-menu-item :index="two.id">{{ two.title }}</el-menu-item>
                        </div>
                    </el-sub-menu>
                </div>
            </el-menu>

        </el-aside>

        <el-container :style="{ height: '100vh' }">
            <el-header style="text-align: right; font-size: 12px;height: 50px;">
                <div class="toolbar">
                    <el-dropdown>
                        <el-icon style="margin-right: 8px; margin-top: 1px">
                            <setting />
                        </el-icon>
                        <template #dropdown>
                            <el-dropdown-menu>
                                <el-dropdown-item>View</el-dropdown-item>
                                <el-dropdown-item>Add</el-dropdown-item>
                                <el-dropdown-item>Delete</el-dropdown-item>
                            </el-dropdown-menu>
                        </template>
                    </el-dropdown>
                    <span>Tom</span>
                </div>
            </el-header>

        </el-container>

        <router-view></router-view>
    </el-container>
</template>


<script>

import { ref } from 'vue'
import { Menu as IconMenu, Message, Setting } from '@element-plus/icons-vue'
import axios from 'axios'
import Alert from './Alert.vue'
import { ElAside, ElMenu, ElMenuItem } from 'element-plus';
import { Histogram, FolderOpened, User, WarnTriangleFilled } from '@element-plus/icons-vue'
import { shallowRef } from 'vue'
export default {
    components: { Histogram, FolderOpened, User, WarnTriangleFilled },
    setup() {
        const Array = [
            {
                id: '1',
                icon: Histogram,
                title: '数据分析',
                router: '',
                Subclass: [] //是否有二级三级
            },
            {
                id: '2',
                icon: FolderOpened,
                title: '数据管理',
                router: '',
                Subclass: [
                    {
                        id: '2-1',
                        title: '视频管理',
                        router: '',
                    },
                    {
                        id: '2-2',
                        title: 'UP主管理',
                        router: '',
                    },
                    {
                        id: '2-3',
                        title: '评论管理',
                        router: '',
                    },
                    {
                        id: '2-4',
                        title: 'Tag管理',
                        router: '',
                    }
                ] //是否有二级三级
            },
            {
                id: '3',
                icon: User,
                title: '账户管理',
                router: '',
                Subclass: [
                    {
                        id: '3-1',
                        title: '管理员账户',
                        router: '',
                    },
                ] //是否有二级三级
            },
            {
                id: '4',
                icon: WarnTriangleFilled,
                title: '异常跟踪',
                router: '',
                Subclass: [
                    {
                        id: '4-1',
                        title: '跟踪表1',
                        router: '',
                    },
                    {
                        id: '4-2',
                        title: '跟踪表2',
                        router: '',
                    },
                ] //是否有二级三级
            }
        ]
        const menu = shallowRef(Array)

        return { menu }
    },

};

</script>

<style scoped>
.layout-container-demo .el-header {
    position: relative;
    background-color: var(--el-color-primary-light-7);
    color: var(--el-text-color-primary);
}

.layout-container-demo .el-aside {
    color: var(--el-text-color-primary);
    background: var(--el-color-primary-light-8);
}

.layout-container-demo .el-menu {
    border-right: none;
}

.layout-container-demo .el-main {
    height: 100%;
    padding: 0;
}


.layout-container-demo .toolbar {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    right: 20px;
}
</style>
  
  