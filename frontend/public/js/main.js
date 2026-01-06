// 页面标题映射
const pageTitles = {
  'data-management': '数据管理',
  'stocks': '股票列表',
  'indices': '指数列表',
  'strategies': '策略列表',
  'backtest-results': '回测结果',
  'portfolio-analysis': '组合分析',
  'model-management': '模型管理'
};

// 页面切换函数
function switchPage(pageId) {
  // 移除所有页面的active类
  document.querySelectorAll('.page').forEach(page => {
    page.classList.remove('active');
  });
  
  // 移除所有菜单项的active类
  document.querySelectorAll('.menu-item').forEach(item => {
    item.classList.remove('active');
  });
  
  // 添加当前页面的active类
  document.getElementById(pageId).classList.add('active');
  
  // 添加当前菜单项的active类
  document.querySelector(`[data-page="${pageId}"]`).classList.add('active');
  
  // 更新页面标题
  document.getElementById('current-title').textContent = pageTitles[pageId];
}

// 标签切换函数
function switchTab(pageId, tabId) {
  // 移除所有标签按钮的active类
  document.querySelectorAll(`#${pageId} .tab-btn`).forEach(btn => {
    btn.classList.remove('active');
  });
  
  // 移除所有标签内容的active类
  document.querySelectorAll(`#${pageId} .tab-content`).forEach(content => {
    content.classList.remove('active');
  });
  
  // 添加当前标签按钮的active类
  document.querySelector(`#${pageId} [data-tab="${tabId}"]`).classList.add('active');
  
  // 添加当前标签内容的active类
  document.getElementById(tabId).classList.add('active');
}

// 初始化事件监听器
document.addEventListener('DOMContentLoaded', function() {
  // 菜单项点击事件
  document.querySelectorAll('.menu-item').forEach(item => {
    item.addEventListener('click', function(e) {
      e.preventDefault();
      const pageId = this.getAttribute('data-page');
      switchPage(pageId);
    });
  });
  
  // 标签按钮点击事件
  document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', function() {
      const pageId = this.closest('.page').id;
      const tabId = this.getAttribute('data-tab');
      switchTab(pageId, tabId);
    });
  });
  
  // 监听URL哈希变化
  window.addEventListener('hashchange', function() {
    const hash = window.location.hash.substring(1);
    if (hash && pageTitles[hash]) {
      switchPage(hash);
    }
  });
});
