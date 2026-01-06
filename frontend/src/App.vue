<template>
  <div class="app-container">
    <aside class="sidebar">
      <div class="sidebar-header">
        <h1 class="logo">量化策略平台</h1>
      </div>
      <nav class="menu">
        <router-link
          v-for="item in menuItems"
          :key="item.path"
          :to="item.path"
          class="menu-item"
          active-class="active"
        >
          <span class="menu-icon">{{ item.icon }}</span>
          <span class="menu-text">{{ item.label }}</span>
        </router-link>
      </nav>
    </aside>
    <main class="main-content">
      <header class="header">
        <h2>{{ currentTitle }}</h2>
      </header>
      <div class="content">
        <router-view />
      </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  data() {
    return {
      menuItems: [
        { path: '/data-management', label: '数据管理', icon: '💾' },
        { path: '/stocks', label: '股票列表', icon: '📈' },
        { path: '/indices', label: '指数列表', icon: '📊' },
        { path: '/strategies', label: '策略列表', icon: '🎯' },
        { path: '/backtest-results', label: '回测结果', icon: '🔄' },
        { path: '/portfolio-analysis', label: '组合分析', icon: '📋' },
        { path: '/model-management', label: '模型管理', icon: '🤖' }
      ],
      currentTitle: '数据管理'
    }
  },
  watch: {
    $route(to) {
      const menuItem = this.menuItems.find(item => item.path === to.path)
      if (menuItem) {
        this.currentTitle = menuItem.label
      }
    }
  }
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
  background-color: #f5f7fa;
  color: #333;
}

.app-container {
  display: flex;
  height: 100vh;
  overflow: hidden;
}

/* Sidebar Styles */
.sidebar {
  width: 250px;
  background-color: #2c3e50;
  color: white;
  display: flex;
  flex-direction: column;
}

.sidebar-header {
  padding: 20px;
  border-bottom: 1px solid #34495e;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  text-align: center;
}

.menu {
  flex: 1;
  padding: 20px 0;
  overflow-y: auto;
}

.menu-item {
  display: flex;
  align-items: center;
  padding: 15px 20px;
  text-decoration: none;
  color: #ecf0f1;
  transition: all 0.3s ease;
  border-left: 3px solid transparent;
}

.menu-item:hover {
  background-color: #34495e;
}

.menu-item.active {
  background-color: #3498db;
  border-left-color: #2980b9;
}

.menu-icon {
  margin-right: 10px;
  font-size: 1.2rem;
}

.menu-text {
  font-size: 1rem;
}

/* Main Content Styles */
.main-content {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
}

.header {
  padding: 20px;
  background-color: white;
  border-bottom: 1px solid #e0e0e0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header h2 {
  font-size: 1.8rem;
  color: #2c3e50;
}

.content {
  flex: 1;
  padding: 20px;
  overflow-y: auto;
  background-color: #f5f7fa;
}

/* Responsive Design */
@media (max-width: 768px) {
  .sidebar {
    width: 200px;
  }
  
  .logo {
    font-size: 1.2rem;
  }
  
  .menu-text {
    font-size: 0.9rem;
  }
}
</style>