import Vue from 'vue'
import VueRouter from 'vue-router'
import DataManagement from '../views/DataManagement.vue'
import Stocks from '../views/Stocks.vue'
import Indices from '../views/Indices.vue'
import Strategies from '../views/Strategies.vue'
import BacktestResults from '../views/BacktestResults.vue'
import PortfolioAnalysis from '../views/PortfolioAnalysis.vue'
import ModelManagement from '../views/ModelManagement.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/data-management'
  },
  {
    path: '/data-management',
    name: 'DataManagement',
    component: DataManagement
  },
  {
    path: '/stocks',
    name: 'Stocks',
    component: Stocks
  },
  {
    path: '/indices',
    name: 'Indices',
    component: Indices
  },
  {
    path: '/strategies',
    name: 'Strategies',
    component: Strategies
  },
  {
    path: '/backtest-results',
    name: 'BacktestResults',
    component: BacktestResults
  },
  {
    path: '/portfolio-analysis',
    name: 'PortfolioAnalysis',
    component: PortfolioAnalysis
  },
  {
    path: '/model-management',
    name: 'ModelManagement',
    component: ModelManagement
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
