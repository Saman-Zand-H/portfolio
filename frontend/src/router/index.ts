import isEmpty from 'lodash/isEmpty';
import HomeView from '@/views/HomeView.vue'
import ProjectView from '@/views/ProjectView.vue'
import ProjectsListView from '@/views/ProjectsListView.vue'
import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      title: 'Portfolio Home'
    }
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectsListView,
    meta: {
      title: 'Portfolio Projects'
    }
  },
  {
    path: '/projects/:slug',
    component: ProjectView,
    name: 'project',
    meta: {
      title: 'Project'
    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})


router.beforeEach((to, from, next) => {
  document.title = to.meta.title ? String(to.meta.title) : document.title;
  next();
})

export default router
