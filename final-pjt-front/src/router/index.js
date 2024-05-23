import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'

// cards
import HomeView from '@/views/cards/HomeView.vue'
import SurveyView from '@/views/cards/SurveyView.vue'
import CardListView from '@/views/cards/CardListView.vue'
import RecommendView from '@/views/cards/RecommendView.vue'
import CardDetailView from '@/views/cards/CardDetailView.vue'
// users
import MyPageView from '@/views/users/MyPageView.vue'
import SignInView from '@/views/users/SignInView.vue'
import SignUpView from '@/views/users/SignUpView.vue'
import MyCardView from '@/views/users/MyCardView.vue'
import PasswordChangeView from '@/views/users/PasswordChangeView.vue'
// posts
import PostListView from '@/views/posts/PostListView.vue'
import PostCreateView from '@/views/posts/PostCreateView.vue'
import PostUpdateView from '@/views/posts/PostUpdateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // cards
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/cards',
      name: 'cardList',
      component: CardListView
    },
    {
      path: '/cards/:id',
      name: 'cardDetail',
      component: CardDetailView
    },
    {
      path: '/:username/survey',
      name: 'survey',
      component: SurveyView,
      // beforeEnter: () => {
      //   const userStore = useUserStore()
      //   if (userStore.userInfo.survey_set.length > 0) {
      //     router.push({name:'recommend', params:{username:userStore.userInfo.username}})
      //   }
      // }
    },
    {
      path: '/:username/recommend',
      name: 'recommend',
      component: RecommendView
    },
    // users
    {
      path: '/:username',
      name: 'myPage',
      component: MyPageView
    },
    {
      path: '/signin',
      name: 'signIn',
      component: SignInView
    },
    {
      path: '/signup',
      name: 'signUp',
      component: SignUpView
    },
    {
      path: '/:username/cards',
      name: 'myCard',
      component: MyCardView
    },
    {
      path: '/:username/password',
      name: 'passwordChange',
      component: PasswordChangeView
    },
    // posts
    {
      path: '/posts',
      name: 'postList',
      component: PostListView
    },
    // {
    //   path: '/posts/:id',
    //   name: 'postDetail',
    //   component: PostDetailView
    // },
    {
      path: '/posts/create',
      name: 'postCreate',
      component: PostCreateView
    },
    {
      path: '/posts/:id/update',
      name: 'postUpdate',
      component: PostUpdateView,
    },
  ]
})

export default router
