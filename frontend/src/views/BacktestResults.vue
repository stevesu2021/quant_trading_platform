<template>
  <div class="backtest-results">
    <div class="results-list">
      <div class="result-card" v-for="result in backtestResults" :key="result.id">
        <div class="result-header">
          <h3 class="result-title">
            {{ result.strategy_name }} - 回测结果
          </h3>
          <span class="result-status" :class="result.status">
            {{ result.status === 'completed' ? '已完成' : result.status === 'running' ? '运行中' : '失败' }}
          </span>
        </div>
        <div class="result-meta">
          <div class="meta-item">
            <span class="meta-label">回测时间：</span>
            <span class="meta-value">{{ result.start_date }} 至 {{ result.end_date }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">创建时间：</span>
            <span class="meta-value">{{ result.created_at }}</span>
          </div>
        </div>
        <div class="result-stats">
          <div class="stat-item">
            <div class="stat-label">总收益率</div>
            <div class="stat-value" :class="result.total_return >= 0 ? 'positive' : 'negative'">
              {{ result.total_return >= 0 ? '+' : '' }}{{ result.total_return }}%
            </div>
          </div>
          <div class="stat-item">
            <div class="stat-label">年化收益率</div>
            <div class="stat-value" :class="result.annual_return >= 0 ? 'positive' : 'negative'">
              {{ result.annual_return >= 0 ? '+' : '' }}{{ result.annual_return }}%
            </div>
          </div>
          <div class="stat-item">
            <div class="stat-label">夏普比率</div>
            <div class="stat-value">
              {{ result.sharpe_ratio }}
            </div>
          </div>
          <div class="stat-item">
            <div class="stat-label">最大回撤</div>
            <div class="stat-value negative">
              -{{ result.max_drawdown }}%
            </div>
          </div>
        </div>
        <div class="result-actions">
          <button class="btn btn-primary" @click="viewDetails(result.id)">查看详情</button>
          <button class="btn btn-secondary" @click="exportResults(result.id)">导出结果</button>
          <button class="btn btn-danger" @click="deleteResult(result.id)">删除</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BacktestResults',
  data() {
    return {
      backtestResults: [
        {
          id: 1,
          strategy_id: 1,
          strategy_name: 'LightGBM_Alpha158',
          start_date: '2023-01-01',
          end_date: '2023-06-15',
          total_return: 23.45,
          annual_return: 46.90,
          sharpe_ratio: 2.12,
          max_drawdown: 8.76,
          volatility: 12.34,
          win_rate: 65.32,
          avg_win: 2.34,
          avg_loss: 1.56,
          trade_count: 128,
          status: 'completed',
          created_at: '2023-06-15'
        },
        {
          id: 2,
          strategy_id: 2,
          strategy_name: 'RandomForest_Alpha158',
          start_date: '2023-01-01',
          end_date: '2023-06-15',
          total_return: 18.76,
          annual_return: 37.52,
          sharpe_ratio: 1.89,
          max_drawdown: 10.23,
          volatility: 14.56,
          win_rate: 61.23,
          avg_win: 2.12,
          avg_loss: 1.78,
          trade_count: 115,
          status: 'completed',
          created_at: '2023-06-14'
        },
        {
          id: 3,
          strategy_id: 3,
          strategy_name: 'XGBoost_Alpha158',
          start_date: '2023-01-01',
          end_date: '2023-06-15',
          total_return: 15.67,
          annual_return: 31.34,
          sharpe_ratio: 1.67,
          max_drawdown: 12.34,
          volatility: 16.78,
          win_rate: 58.90,
          avg_win: 1.98,
          avg_loss: 1.89,
          trade_count: 105,
          status: 'completed',
          created_at: '2023-06-13'
        },
        {
          id: 4,
          strategy_id: 4,
          strategy_name: 'Custom_Momentum',
          start_date: '2023-01-01',
          end_date: '2023-06-15',
          total_return: 12.34,
          annual_return: 24.68,
          sharpe_ratio: 1.45,
          max_drawdown: 15.67,
          volatility: 18.90,
          win_rate: 55.67,
          avg_win: 1.87,
          avg_loss: 2.12,
          trade_count: 98,
          status: 'completed',
          created_at: '2023-06-12'
        }
      ]
    }
  },
  methods: {
    viewDetails(resultId) {
      // 查看详情的逻辑
      console.log('查看回测结果详情:', resultId)
      alert(`查看回测结果 ${resultId} 详情`)
    },
    exportResults(resultId) {
      // 导出结果的逻辑
      console.log('导出回测结果:', resultId)
      alert(`导出回测结果 ${resultId}`)
    },
    deleteResult(resultId) {
      // 删除结果的逻辑
      console.log('删除回测结果:', resultId)
      if (confirm('确定要删除这个回测结果吗？')) {
        this.backtestResults = this.backtestResults.filter(result => result.id !== resultId)
        alert('回测结果已删除')
      }
    }
  }
}
</script>

<style scoped>
.backtest-results {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.results-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 20px;
}

.result-card {
  background-color: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  transition: all 0.3s ease;
}

.result-card:hover {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transform: translateY(-5px);
}

.result-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.result-title {
  margin: 0;
  color: #2c3e50;
  font-size: 1.1rem;
}

.result-status {
  padding: 3px 8px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
}

.result-status.completed {
  background-color: #27ae60;
  color: white;
}

.result-status.running {
  background-color: #f39c12;
  color: white;
}

.result-status.failed {
  background-color: #e74c3c;
  color: white;
}

.result-meta {
  background-color: white;
  padding: 12px;
  border-radius: 6px;
  margin-bottom: 15px;
  border: 1px solid #e0e0e0;
}

.meta-item {
  margin-bottom: 6px;
  font-size: 0.85rem;
}

.meta-item:last-child {
  margin-bottom: 0;
}

.meta-label {
  color: #666;
  font-weight: 500;
}

.meta-value {
  color: #2c3e50;
}

.result-stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  margin-bottom: 20px;
}

.stat-item {
  background-color: white;
  padding: 15px;
  border-radius: 6px;
  border: 1px solid #e0e0e0;
  text-align: center;
}

.stat-label {
  color: #666;
  font-size: 0.85rem;
  margin-bottom: 8px;
}

.stat-value {
  font-size: 1.2rem;
  font-weight: 700;
}

.stat-value.positive {
  color: #27ae60;
}

.stat-value.negative {
  color: #e74c3c;
}

.result-actions {
  display: flex;
  gap: 10px;
  justify-content: flex-end;
}

.btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.9rem;
  font-weight: 500;
  transition: background-color 0.3s ease;
}

.btn-primary {
  background-color: #3498db;
  color: white;
}

.btn-primary:hover {
  background-color: #2980b9;
}

.btn-secondary {
  background-color: #95a5a6;
  color: white;
}

.btn-secondary:hover {
  background-color: #7f8c8d;
}

.btn-danger {
  background-color: #e74c3c;
  color: white;
}

.btn-danger:hover {
  background-color: #c0392b;
}

@media (max-width: 768px) {
  .results-list {
    grid-template-columns: 1fr;
  }
  
  .result-actions {
    flex-direction: column;
  }
  
  .result-stats {
    grid-template-columns: 1fr;
  }
}
</style>