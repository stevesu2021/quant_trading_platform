<template>
  <div class="data-management">
    <div class="tab-container">
      <div 
        v-for="tab in tabs" 
        :key="tab.name"
        class="tab-item"
        :class="{ active: activeTab === tab.name }"
        @click="activeTab = tab.name"
      >
        {{ tab.label }}
      </div>
    </div>
    <div class="tab-content">
      <div v-if="activeTab === 'daily'" class="daily-data">
        <h3>天级数据</h3>
        <div class="data-grid">
          <div class="data-item">
            <div class="data-label">股票数据</div>
            <div class="data-value">10,000+ 条</div>
          </div>
          <div class="data-item">
            <div class="data-label">指数数据</div>
            <div class="data-value">500+ 条</div>
          </div>
          <div class="data-item">
            <div class="data-label">最新更新</div>
            <div class="data-value">2023-06-15</div>
          </div>
          <div class="data-item">
            <div class="data-label">数据状态</div>
            <div class="data-value status-success">已更新</div>
          </div>
        </div>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>代码</th>
                <th>名称</th>
                <th>日期</th>
                <th>开盘价</th>
                <th>收盘价</th>
                <th>最高价</th>
                <th>最低价</th>
                <th>成交量</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in dailyData" :key="item.id">
                <td>{{ item.symbol }}</td>
                <td>{{ item.name }}</td>
                <td>{{ item.date }}</td>
                <td>{{ item.open }}</td>
                <td>{{ item.close }}</td>
                <td>{{ item.high }}</td>
                <td>{{ item.low }}</td>
                <td>{{ item.volume }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      <div v-else-if="activeTab === 'minute'" class="minute-data">
        <h3>分钟级数据</h3>
        <div class="data-grid">
          <div class="data-item">
            <div class="data-label">1分钟数据</div>
            <div class="data-value">500,000+ 条</div>
          </div>
          <div class="data-item">
            <div class="data-label">5分钟数据</div>
            <div class="data-value">100,000+ 条</div>
          </div>
          <div class="data-item">
            <div class="data-label">最新更新</div>
            <div class="data-value">2023-06-15 15:00</div>
          </div>
          <div class="data-item">
            <div class="data-label">数据状态</div>
            <div class="data-value status-success">已更新</div>
          </div>
        </div>
        <div class="table-container">
          <table class="data-table">
            <thead>
              <tr>
                <th>代码</th>
                <th>名称</th>
                <th>时间</th>
                <th>开盘价</th>
                <th>收盘价</th>
                <th>最高价</th>
                <th>最低价</th>
                <th>成交量</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in minuteData" :key="item.id">
                <td>{{ item.symbol }}</td>
                <td>{{ item.name }}</td>
                <td>{{ item.time }}</td>
                <td>{{ item.open }}</td>
                <td>{{ item.close }}</td>
                <td>{{ item.high }}</td>
                <td>{{ item.low }}</td>
                <td>{{ item.volume }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DataManagement',
  data() {
    return {
      activeTab: 'daily',
      tabs: [
        { name: 'daily', label: '天级数据' },
        { name: 'minute', label: '分钟级数据' }
      ],
      dailyData: [
        { id: 1, symbol: '000001', name: '平安银行', date: '2023-06-15', open: 12.34, close: 12.56, high: 12.78, low: 12.20, volume: 12345678 },
        { id: 2, symbol: '000002', name: '万科A', date: '2023-06-15', open: 15.67, close: 15.89, high: 16.00, low: 15.50, volume: 9876543 },
        { id: 3, symbol: '600000', name: '浦发银行', date: '2023-06-15', open: 8.90, close: 9.05, high: 9.15, low: 8.85, volume: 15432109 },
        { id: 4, symbol: '600036', name: '招商银行', date: '2023-06-15', open: 38.45, close: 38.90, high: 39.20, low: 38.30, volume: 23456789 },
        { id: 5, symbol: '601318', name: '中国平安', date: '2023-06-15', open: 45.67, close: 46.00, high: 46.50, low: 45.50, volume: 18765432 }
      ],
      minuteData: [
        { id: 1, symbol: '000001', name: '平安银行', time: '2023-06-15 14:59', open: 12.55, close: 12.56, high: 12.57, low: 12.54, volume: 123456 },
        { id: 2, symbol: '000001', name: '平安银行', time: '2023-06-15 14:58', open: 12.53, close: 12.55, high: 12.56, low: 12.52, volume: 98765 },
        { id: 3, symbol: '000001', name: '平安银行', time: '2023-06-15 14:57', open: 12.50, close: 12.53, high: 12.54, low: 12.49, volume: 154321 },
        { id: 4, symbol: '000001', name: '平安银行', time: '2023-06-15 14:56', open: 12.48, close: 12.50, high: 12.51, low: 12.47, volume: 87654 },
        { id: 5, symbol: '000001', name: '平安银行', time: '2023-06-15 14:55', open: 12.45, close: 12.48, high: 12.49, low: 12.44, volume: 134567 }
      ]
    }
  }
}
</script>

<style scoped>
.data-management {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.tab-container {
  display: flex;
  margin-bottom: 20px;
  border-bottom: 2px solid #e0e0e0;
}

.tab-item {
  padding: 10px 20px;
  cursor: pointer;
  font-weight: 500;
  color: #666;
  border-bottom: 2px solid transparent;
  transition: all 0.3s ease;
}

.tab-item:hover {
  color: #3498db;
}

.tab-item.active {
  color: #3498db;
  border-bottom-color: #3498db;
}

.tab-content {
  padding: 20px 0;
}

h3 {
  margin-bottom: 20px;
  color: #2c3e50;
  font-size: 1.2rem;
}

.data-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
  margin-bottom: 20px;
}

.data-item {
  background-color: #f8f9fa;
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.data-label {
  font-size: 0.9rem;
  color: #666;
  margin-bottom: 5px;
}

.data-value {
  font-size: 1.2rem;
  font-weight: 600;
  color: #2c3e50;
}

.status-success {
  color: #27ae60;
}

.status-warning {
  color: #f39c12;
}

.status-error {
  color: #e74c3c;
}

.table-container {
  overflow-x: auto;
  margin-top: 20px;
}

.data-table {
  width: 100%;
  border-collapse: collapse;
  background-color: white;
}

.data-table th,
.data-table td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #e0e0e0;
}

.data-table th {
  background-color: #f5f7fa;
  font-weight: 600;
  color: #2c3e50;
  font-size: 0.9rem;
}

.data-table td {
  color: #333;
  font-size: 0.9rem;
}

.data-table tr:hover {
  background-color: #f8f9fa;
}
</style>