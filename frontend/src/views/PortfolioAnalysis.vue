<template>
  <div class="portfolio-analysis">
    <div class="analysis-sections">
      <div class="section portfolio-overview">
        <h3>组合概览</h3>
        <div class="overview-cards">
          <div class="overview-card">
            <div class="card-label">总价值</div>
            <div class="card-value">¥{{ portfolio.total_value.toLocaleString() }}</div>
          </div>
          <div class="overview-card">
            <div class="card-label">现金</div>
            <div class="card-value">¥{{ portfolio.cash.toLocaleString() }}</div>
          </div>
          <div class="overview-card">
            <div class="card-label">持仓价值</div>
            <div class="card-value">¥{{ portfolio.positions_value.toLocaleString() }}</div>
          </div>
          <div class="overview-card">
            <div class="card-label">收益率</div>
            <div class="card-value positive">+{{ portfolio.return_rate }}%</div>
          </div>
        </div>
      </div>
      
      <div class="section allocation-section">
        <h3>资产配置</h3>
        <div class="allocation-content">
          <div class="chart-container">
            <!-- 这里可以集成图表库，如ECharts或Chart.js -->
            <div class="allocation-simulation">
              <div class="allocation-item" v-for="item in allocationData" :key="item.sector">
                <div class="item-label">{{ item.sector }}</div>
                <div class="item-bar-container">
                  <div class="item-bar" :style="{ width: `${item.percentage}%`, backgroundColor: item.color }"></div>
                  <span class="item-percentage">{{ item.percentage }}%</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      
      <div class="section holdings-section">
        <h3>持仓明细</h3>
        <div class="table-container">
          <table class="holdings-table">
            <thead>
              <tr>
                <th>代码</th>
                <th>名称</th>
                <th>持仓数量</th>
                <th>成本价</th>
                <th>当前价</th>
                <th>市值</th>
                <th>收益率</th>
                <th>持仓占比</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="holding in holdings" :key="holding.id">
                <td>{{ holding.symbol }}</td>
                <td>{{ holding.name }}</td>
                <td>{{ holding.quantity }}</td>
                <td>¥{{ holding.cost_price }}</td>
                <td>¥{{ holding.current_price }}</td>
                <td>¥{{ holding.market_value.toLocaleString() }}</td>
                <td :class="holding.return_rate >= 0 ? 'positive' : 'negative'">
                  {{ holding.return_rate >= 0 ? '+' : '' }}{{ holding.return_rate }}%
                </td>
                <td>{{ holding.percentage }}%</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
      
      <div class="section performance-section">
        <h3>绩效分析</h3>
        <div class="performance-metrics">
          <div class="metric-group">
            <div class="metric-item">
              <div class="metric-label">年化收益率</div>
              <div class="metric-value positive">18.56%</div>
            </div>
            <div class="metric-item">
              <div class="metric-label">夏普比率</div>
              <div class="metric-value">1.98</div>
            </div>
            <div class="metric-item">
              <div class="metric-label">最大回撤</div>
              <div class="metric-value negative">-9.23%</div>
            </div>
            <div class="metric-item">
              <div class="metric-label">波动率</div>
              <div class="metric-value">14.67%</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'PortfolioAnalysis',
  data() {
    return {
      portfolio: {
        total_value: 5000000,
        cash: 1000000,
        positions_value: 4000000,
        return_rate: 12.34
      },
      allocationData: [
        { sector: '金融', percentage: 35, color: '#3498db' },
        { sector: '科技', percentage: 30, color: '#27ae60' },
        { sector: '消费', percentage: 20, color: '#f39c12' },
        { sector: '医药', percentage: 10, color: '#e74c3c' },
        { sector: '其他', percentage: 5, color: '#95a5a6' }
      ],
      holdings: [
        { id: 1, symbol: '600036', name: '招商银行', quantity: 5000, cost_price: 35.67, current_price: 38.90, market_value: 194500, return_rate: 9.05, percentage: 3.89 },
        { id: 2, symbol: '000858', name: '五粮液', quantity: 1000, cost_price: 165.45, current_price: 178.50, market_value: 178500, return_rate: 7.89, percentage: 3.57 },
        { id: 3, symbol: '300750', name: '宁德时代', quantity: 500, cost_price: 215.67, current_price: 234.50, market_value: 117250, return_rate: 8.73, percentage: 2.35 },
        { id: 4, symbol: '601318', name: '中国平安', quantity: 3000, cost_price: 42.34, current_price: 46.00, market_value: 138000, return_rate: 8.64, percentage: 2.76 },
        { id: 5, symbol: '002415', name: '海康威视', quantity: 2000, cost_price: 32.45, current_price: 35.67, market_value: 71340, return_rate: 9.92, percentage: 1.43 },
        { id: 6, symbol: '600519', name: '贵州茅台', quantity: 100, cost_price: 1580.00, current_price: 1680.00, market_value: 168000, return_rate: 6.33, percentage: 3.36 },
        { id: 7, symbol: '000001', name: '平安银行', quantity: 10000, cost_price: 11.56, current_price: 12.56, market_value: 125600, return_rate: 8.65, percentage: 2.51 },
        { id: 8, symbol: '600000', name: '浦发银行', quantity: 8000, cost_price: 8.23, current_price: 9.05, market_value: 72400, return_rate: 9.96, percentage: 1.45 }
      ]
    }
  }
}
</script>

<style scoped>
.portfolio-analysis {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.analysis-sections {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.section {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 20px;
  border: 1px solid #e0e0e0;
}

h3 {
  margin-bottom: 20px;
  color: #2c3e50;
  font-size: 1.2rem;
}

/* 组合概览样式 */
.overview-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 15px;
}

.overview-card {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.card-label {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 10px;
}

.card-value {
  font-size: 1.5rem;
  font-weight: 700;
  color: #2c3e50;
}

.card-value.positive {
  color: #27ae60;
}

.card-value.negative {
  color: #e74c3c;
}

/* 资产配置样式 */
.allocation-content {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.chart-container {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
}

.allocation-simulation {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.allocation-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.item-label {
  font-size: 0.9rem;
  color: #666;
}

.item-bar-container {
  display: flex;
  align-items: center;
  gap: 10px;
}

.item-bar {
  height: 20px;
  border-radius: 10px;
  transition: width 0.5s ease;
}

.item-percentage {
  font-size: 0.85rem;
  font-weight: 600;
  color: #2c3e50;
  min-width: 40px;
  text-align: right;
}

/* 持仓明细样式 */
.table-container {
  overflow-x: auto;
}

.holdings-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.holdings-table th {
  background-color: #f5f7fa;
  padding: 12px;
  text-align: left;
  font-weight: 600;
  color: #2c3e50;
  border-bottom: 2px solid #e0e0e0;
}

.holdings-table td {
  padding: 12px;
  border-bottom: 1px solid #e0e0e0;
  color: #333;
}

.holdings-table tbody tr:hover {
  background-color: #f8f9fa;
}

.positive {
  color: #27ae60;
  font-weight: 600;
}

.negative {
  color: #e74c3c;
  font-weight: 600;
}

/* 绩效分析样式 */
.performance-metrics {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
}

.metric-group {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 20px;
}

.metric-item {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.metric-label {
  color: #666;
  font-size: 0.9rem;
}

.metric-value {
  font-size: 1.2rem;
  font-weight: 700;
  color: #2c3e50;
}

@media (max-width: 768px) {
  .overview-cards {
    grid-template-columns: 1fr;
  }
  
  .metric-group {
    grid-template-columns: 1fr;
  }
  
  .holdings-table {
    font-size: 0.8rem;
  }
  
  .holdings-table th,
  .holdings-table td {
    padding: 8px;
  }
}
</style>