<template>
  <div class="stocks">
    <div class="header-actions">
      <div class="search-box">
        <input 
          type="text" 
          placeholder="搜索股票代码或名称" 
          v-model="searchQuery"
          @input="handleSearch"
        />
      </div>
      <div class="filter-box">
        <select v-model="selectedSector">
          <option value="">全部行业</option>
          <option value="金融">金融</option>
          <option value="科技">科技</option>
          <option value="消费">消费</option>
          <option value="医药">医药</option>
          <option value="能源">能源</option>
        </select>
      </div>
    </div>
    <div class="stocks-grid">
      <div class="stock-card" v-for="stock in filteredStocks" :key="stock.id">
        <div class="stock-header">
          <div class="stock-info">
            <div class="stock-symbol">{{ stock.symbol }}</div>
            <div class="stock-name">{{ stock.name }}</div>
          </div>
          <div class="stock-sector">{{ stock.sector }}</div>
        </div>
        <div class="stock-price">
          <div class="price-value">{{ stock.price }}</div>
          <div class="price-change" :class="stock.change >= 0 ? 'positive' : 'negative'">
            {{ stock.change >= 0 ? '+' : '' }}{{ stock.change }} ({{ stock.change_percent }}%)
          </div>
        </div>
        <div class="stock-metrics">
          <div class="metric-item">
            <span class="metric-label">市盈率</span>
            <span class="metric-value">{{ stock.pe_ratio }}</span>
          </div>
          <div class="metric-item">
            <span class="metric-label">市净率</span>
            <span class="metric-value">{{ stock.pb_ratio }}</span>
          </div>
          <div class="metric-item">
            <span class="metric-label">市值</span>
            <span class="metric-value">{{ stock.market_cap }}亿</span>
          </div>
          <div class="metric-item">
            <span class="metric-label">成交量</span>
            <span class="metric-value">{{ stock.volume }}万</span>
          </div>
        </div>
      </div>
    </div>
    <div class="pagination">
      <button @click="currentPage--" :disabled="currentPage === 1">上一页</button>
      <span>第 {{ currentPage }} 页，共 {{ totalPages }} 页</span>
      <button @click="currentPage++" :disabled="currentPage === totalPages">下一页</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Stocks',
  data() {
    return {
      searchQuery: '',
      selectedSector: '',
      currentPage: 1,
      pageSize: 12,
      stocks: [
        { id: 1, symbol: '000001', name: '平安银行', sector: '金融', price: 12.56, change: 0.22, change_percent: 1.78, pe_ratio: 6.78, pb_ratio: 0.78, market_cap: 2800, volume: 12345 },
        { id: 2, symbol: '000002', name: '万科A', sector: '地产', price: 15.89, change: 0.22, change_percent: 1.40, pe_ratio: 8.90, pb_ratio: 1.05, market_cap: 2000, volume: 9876 },
        { id: 3, symbol: '600000', name: '浦发银行', sector: '金融', price: 9.05, change: 0.15, change_percent: 1.69, pe_ratio: 5.45, pb_ratio: 0.58, market_cap: 2200, volume: 15432 },
        { id: 4, symbol: '600036', name: '招商银行', sector: '金融', price: 38.90, change: 0.45, change_percent: 1.17, pe_ratio: 9.87, pb_ratio: 1.20, market_cap: 10000, volume: 23456 },
        { id: 5, symbol: '601318', name: '中国平安', sector: '金融', price: 46.00, change: 0.33, change_percent: 0.72, pe_ratio: 7.65, pb_ratio: 1.02, market_cap: 8000, volume: 18765 },
        { id: 6, symbol: '000858', name: '五粮液', sector: '消费', price: 178.50, change: -2.30, change_percent: -1.27, pe_ratio: 28.90, pb_ratio: 7.89, market_cap: 6800, volume: 8765 },
        { id: 7, symbol: '002415', name: '海康威视', sector: '科技', price: 35.67, change: 0.89, change_percent: 2.56, pe_ratio: 22.34, pb_ratio: 3.45, market_cap: 3800, volume: 16789 },
        { id: 8, symbol: '300750', name: '宁德时代', sector: '新能源', price: 234.50, change: 5.67, change_percent: 2.48, pe_ratio: 45.67, pb_ratio: 8.90, market_cap: 12000, volume: 34567 },
        { id: 9, symbol: '600519', name: '贵州茅台', sector: '消费', price: 1680.00, change: -12.50, change_percent: -0.74, pe_ratio: 33.45, pb_ratio: 12.34, market_cap: 21000, volume: 3456 },
        { id: 10, symbol: '000568', name: '泸州老窖', sector: '消费', price: 234.56, change: -1.23, change_percent: -0.52, pe_ratio: 31.23, pb_ratio: 8.76, market_cap: 3200, volume: 5678 },
        { id: 11, symbol: '601888', name: '中国中免', sector: '消费', price: 123.45, change: 2.34, change_percent: 1.93, pe_ratio: 42.34, pb_ratio: 6.78, market_cap: 4500, volume: 7890 },
        { id: 12, symbol: '603288', name: '海天味业', sector: '消费', price: 89.76, change: -0.56, change_percent: -0.62, pe_ratio: 38.45, pb_ratio: 10.23, market_cap: 3800, volume: 4321 },
        { id: 13, symbol: '000063', name: '中兴通讯', sector: '科技', price: 32.12, change: 1.23, change_percent: 3.98, pe_ratio: 28.76, pb_ratio: 2.34, market_cap: 1500, volume: 21345 },
        { id: 14, symbol: '002594', name: '比亚迪', sector: '新能源', price: 256.78, change: 4.32, change_percent: 1.71, pe_ratio: 89.45, pb_ratio: 13.21, market_cap: 7000, volume: 28765 },
        { id: 15, symbol: '600887', name: '伊利股份', sector: '消费', price: 38.90, change: -0.12, change_percent: -0.31, pe_ratio: 22.34, pb_ratio: 4.56, market_cap: 2500, volume: 6543 }
      ]
    }
  },
  computed: {
    filteredStocks() {
      let result = [...this.stocks]
      
      // 搜索过滤
      if (this.searchQuery) {
        const query = this.searchQuery.toLowerCase()
        result = result.filter(stock => 
          stock.symbol.toLowerCase().includes(query) || 
          stock.name.toLowerCase().includes(query)
        )
      }
      
      // 行业过滤
      if (this.selectedSector) {
        result = result.filter(stock => stock.sector === this.selectedSector)
      }
      
      // 分页
      const startIndex = (this.currentPage - 1) * this.pageSize
      const endIndex = startIndex + this.pageSize
      result = result.slice(startIndex, endIndex)
      
      return result
    },
    totalPages() {
      let result = [...this.stocks]
      
      // 搜索过滤
      if (this.searchQuery) {
        const query = this.searchQuery.toLowerCase()
        result = result.filter(stock => 
          stock.symbol.toLowerCase().includes(query) || 
          stock.name.toLowerCase().includes(query)
        )
      }
      
      // 行业过滤
      if (this.selectedSector) {
        result = result.filter(stock => stock.sector === this.selectedSector)
      }
      
      return Math.ceil(result.length / this.pageSize)
    }
  },
  methods: {
    handleSearch() {
      this.currentPage = 1 // 搜索时重置到第一页
    }
  }
}
</script>

<style scoped>
.stocks {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header-actions {
  display: flex;
  justify-content: space-between;
  margin-bottom: 20px;
  gap: 20px;
}

.search-box input {
  padding: 10px 15px;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  font-size: 14px;
  width: 300px;
  transition: border-color 0.3s ease;
}

.search-box input:focus {
  outline: none;
  border-color: #3498db;
}

.filter-box select {
  padding: 10px 15px;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  font-size: 14px;
  background-color: white;
  cursor: pointer;
  transition: border-color 0.3s ease;
}

.filter-box select:focus {
  outline: none;
  border-color: #3498db;
}

.stocks-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 20px;
  margin-bottom: 20px;
}

.stock-card {
  background-color: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 15px;
  transition: all 0.3s ease;
  cursor: pointer;
}

.stock-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.stock-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 10px;
}

.stock-info {
  flex: 1;
}

.stock-symbol {
  font-weight: 600;
  font-size: 1.1rem;
  color: #2c3e50;
  margin-bottom: 5px;
}

.stock-name {
  font-size: 0.9rem;
  color: #666;
}

.stock-sector {
  background-color: #3498db;
  color: white;
  padding: 3px 8px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
}

.stock-price {
  margin-bottom: 15px;
}

.price-value {
  font-size: 1.8rem;
  font-weight: 700;
  color: #2c3e50;
  margin-bottom: 5px;
}

.price-change {
  font-size: 0.9rem;
  font-weight: 500;
}

.price-change.positive {
  color: #27ae60;
}

.price-change.negative {
  color: #e74c3c;
}

.stock-metrics {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  font-size: 0.85rem;
}

.metric-item {
  display: flex;
  justify-content: space-between;
}

.metric-label {
  color: #666;
}

.metric-value {
  font-weight: 600;
  color: #2c3e50;
}

.pagination {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  margin-top: 30px;
}

.pagination button {
  padding: 8px 16px;
  background-color: #3498db;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.pagination button:hover:not(:disabled) {
  background-color: #2980b9;
}

.pagination button:disabled {
  background-color: #bdc3c7;
  cursor: not-allowed;
}

.pagination span {
  color: #666;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .header-actions {
    flex-direction: column;
    gap: 10px;
  }
  
  .search-box input {
    width: 100%;
  }
  
  .stocks-grid {
    grid-template-columns: 1fr;
  }
}
</style>