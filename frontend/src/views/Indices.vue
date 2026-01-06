<template>
  <div class="indices">
    <div class="indices-table-container">
      <table class="indices-table">
        <thead>
          <tr>
            <th>代码</th>
            <th>名称</th>
            <th>当前值</th>
            <th>涨跌额</th>
            <th>涨跌幅</th>
            <th>市值</th>
            <th>成分股数量</th>
            <th>发布日期</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="index in indices" :key="index.id" class="index-row">
            <td class="symbol">{{ index.symbol }}</td>
            <td class="name">{{ index.name }}</td>
            <td class="value">{{ index.current_value }}</td>
            <td class="change" :class="index.change >= 0 ? 'positive' : 'negative'">
              {{ index.change >= 0 ? '+' : '' }}{{ index.change }}
            </td>
            <td class="change-percent" :class="index.change_percent >= 0 ? 'positive' : 'negative'">
              {{ index.change_percent >= 0 ? '+' : '' }}{{ index.change_percent }}%
            </td>
            <td class="market-cap">{{ index.market_cap }}亿</td>
            <td class="constituents">{{ index.constituent_count }}</td>
            <td class="launch-date">{{ index.launch_date }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="indices-charts">
      <div class="chart-card">
        <h3>指数表现对比</h3>
        <div class="chart-placeholder">
          <!-- 这里可以集成图表库，如ECharts或Chart.js -->
          <div class="chart-simulation">
            <div class="chart-line">
              <div class="line" style="height: 40%; background: #3498db;"></div>
              <div class="line-label">沪深300</div>
            </div>
            <div class="chart-line">
              <div class="line" style="height: 60%; background: #27ae60;"></div>
              <div class="line-label">中证500</div>
            </div>
            <div class="chart-line">
              <div class="line" style="height: 80%; background: #f39c12;"></div>
              <div class="line-label">创业板指</div>
            </div>
            <div class="chart-line">
              <div class="line" style="height: 50%; background: #e74c3c;"></div>
              <div class="line-label">上证50</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Indices',
  data() {
    return {
      indices: [
        { id: 1, symbol: '000001', name: '上证指数', current_value: 3215.67, change: 12.34, change_percent: 0.39, market_cap: 450000, constituent_count: 1500, launch_date: '1990-12-19' },
        { id: 2, symbol: '000016', name: '上证50', current_value: 2890.45, change: 8.90, change_percent: 0.31, market_cap: 180000, constituent_count: 50, launch_date: '2004-01-02' },
        { id: 3, symbol: '000300', name: '沪深300', current_value: 4123.78, change: 15.67, change_percent: 0.38, market_cap: 320000, constituent_count: 300, launch_date: '2005-04-08' },
        { id: 4, symbol: '000905', name: '中证500', current_value: 6234.56, change: 23.45, change_percent: 0.38, market_cap: 150000, constituent_count: 500, launch_date: '2007-01-15' },
        { id: 5, symbol: '399001', name: '深证成指', current_value: 11567.89, change: 45.67, change_percent: 0.40, market_cap: 380000, constituent_count: 500, launch_date: '1991-04-03' },
        { id: 6, symbol: '399006', name: '创业板指', current_value: 2345.67, change: 18.90, change_percent: 0.81, market_cap: 120000, constituent_count: 100, launch_date: '2010-06-01' },
        { id: 7, symbol: '399016', name: '深证100', current_value: 7890.45, change: 12.34, change_percent: 0.16, market_cap: 100000, constituent_count: 100, launch_date: '2003-01-02' },
        { id: 8, symbol: '000852', name: '中证1000', current_value: 5678.90, change: 34.56, change_percent: 0.61, market_cap: 80000, constituent_count: 1000, launch_date: '2014-10-17' }
      ]
    }
  }
}
</script>

<style scoped>
.indices {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.indices-table-container {
  margin-bottom: 30px;
  overflow-x: auto;
}

.indices-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.indices-table th {
  background-color: #f5f7fa;
  padding: 12px;
  text-align: left;
  font-weight: 600;
  color: #2c3e50;
  border-bottom: 2px solid #e0e0e0;
}

.indices-table td {
  padding: 12px;
  border-bottom: 1px solid #e0e0e0;
  color: #333;
}

.index-row:hover {
  background-color: #f8f9fa;
}

.symbol {
  font-weight: 600;
  color: #2c3e50;
}

.name {
  font-weight: 500;
}

.value {
  font-weight: 600;
}

.change, .change-percent {
  font-weight: 600;
}

.positive {
  color: #27ae60;
}

.negative {
  color: #e74c3c;
}

.market-cap {
  color: #666;
}

.constituents {
  text-align: center;
  color: #666;
}

.launch-date {
  color: #666;
}

.indices-charts {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
}

.chart-card {
  background-color: #f8f9fa;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.chart-card h3 {
  margin-bottom: 20px;
  color: #2c3e50;
  font-size: 1.1rem;
}

.chart-placeholder {
  height: 300px;
  background-color: white;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid #e0e0e0;
}

.chart-simulation {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: flex-end;
  justify-content: space-around;
  padding: 20px;
}

.chart-line {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  max-width: 80px;
}

.line {
  width: 100%;
  border-radius: 4px 4px 0 0;
  margin-bottom: 10px;
  transition: height 0.5s ease;
}

.chart-line:hover .line {
  opacity: 0.8;
}

.line-label {
  font-size: 0.8rem;
  color: #666;
  text-align: center;
}

@media (max-width: 768px) {
  .indices-table {
    font-size: 0.8rem;
  }
  
  .indices-table th,
  .indices-table td {
    padding: 8px;
  }
  
  .chart-simulation {
    flex-direction: column;
    align-items: flex-start;
    justify-content: flex-end;
    overflow-x: auto;
    padding: 10px;
  }
  
  .chart-line {
    flex-direction: row;
    align-items: center;
    width: 100%;
    margin-bottom: 10px;
  }
  
  .line {
    height: 20px !important;
    width: 60%;
    margin-right: 10px;
    margin-bottom: 0;
    border-radius: 0 4px 4px 0;
  }
}
</style>