<template>
  <div class="strategies">
    <div class="strategies-grid">
      <div class="strategy-card" v-for="strategy in strategies" :key="strategy.id">
        <div class="strategy-header">
          <h3 class="strategy-name">{{ strategy.name }}</h3>
          <span class="strategy-status" :class="strategy.status">
            {{ strategy.status === 'active' ? '运行中' : strategy.status === 'inactive' ? '已停用' : '已废弃' }}
          </span>
        </div>
        <div class="strategy-description">{{ strategy.description }}</div>
        <div class="strategy-meta">
          <div class="meta-item">
            <span class="meta-label">类型：</span>
            <span class="meta-value">{{ strategy.type }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">创建时间：</span>
            <span class="meta-value">{{ strategy.created_at }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">更新时间：</span>
            <span class="meta-value">{{ strategy.updated_at }}</span>
          </div>
        </div>
        <div class="strategy-actions">
          <button class="btn btn-primary" @click="runStrategy(strategy.id)">运行策略</button>
          <button class="btn btn-secondary" @click="viewStrategy(strategy.id)">查看详情</button>
          <button class="btn btn-danger" @click="deleteStrategy(strategy.id)">删除</button>
        </div>
      </div>
    </div>
    <div class="add-strategy-section">
      <h3>添加新策略</h3>
      <div class="add-strategy-form">
        <div class="form-row">
          <div class="form-group">
            <label for="strategy-name">策略名称</label>
            <input type="text" id="strategy-name" v-model="newStrategy.name" placeholder="输入策略名称" />
          </div>
          <div class="form-group">
            <label for="strategy-type">策略类型</label>
            <select id="strategy-type" v-model="newStrategy.type">
              <option value="LightGBM_Alpha158">LightGBM_Alpha158</option>
              <option value="RandomForest_Alpha158">RandomForest_Alpha158</option>
              <option value="XGBoost_Alpha158">XGBoost_Alpha158</option>
              <option value="Custom_Strategy">自定义策略</option>
            </select>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group full-width">
            <label for="strategy-description">策略描述</label>
            <textarea id="strategy-description" v-model="newStrategy.description" placeholder="输入策略描述"></textarea>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group">
            <label for="strategy-config">配置文件路径</label>
            <input type="text" id="strategy-config" v-model="newStrategy.config_path" placeholder="输入配置文件路径" />
          </div>
          <div class="form-group">
            <label for="strategy-status">状态</label>
            <select id="strategy-status" v-model="newStrategy.status">
              <option value="active">运行中</option>
              <option value="inactive">已停用</option>
            </select>
          </div>
        </div>
        <div class="form-actions">
          <button class="btn btn-primary" @click="addStrategy">添加策略</button>
          <button class="btn btn-secondary" @click="resetForm">重置</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Strategies',
  data() {
    return {
      strategies: [
        {
          id: 1,
          name: 'LightGBM_Alpha158',
          description: '基于LightGBM的Alpha158因子模型',
          type: 'LightGBM_Alpha158',
          config_path: 'configs/LightGBM_Alpha158.yaml',
          status: 'active',
          created_at: '2023-06-01',
          updated_at: '2023-06-15'
        },
        {
          id: 2,
          name: 'RandomForest_Alpha158',
          description: '基于随机森林的Alpha158因子模型',
          type: 'RandomForest_Alpha158',
          config_path: 'configs/RandomForest_Alpha158.yaml',
          status: 'active',
          created_at: '2023-06-05',
          updated_at: '2023-06-10'
        },
        {
          id: 3,
          name: 'XGBoost_Alpha158',
          description: '基于XGBoost的Alpha158因子模型',
          type: 'XGBoost_Alpha158',
          config_path: 'configs/XGBoost_Alpha158.yaml',
          status: 'inactive',
          created_at: '2023-05-20',
          updated_at: '2023-06-01'
        },
        {
          id: 4,
          name: 'Custom_Momentum',
          description: '自定义动量策略',
          type: 'Custom_Strategy',
          config_path: 'configs/Custom_Momentum.yaml',
          status: 'active',
          created_at: '2023-06-10',
          updated_at: '2023-06-15'
        }
      ],
      newStrategy: {
        name: '',
        description: '',
        type: 'LightGBM_Alpha158',
        config_path: '',
        status: 'active'
      }
    }
  },
  methods: {
    runStrategy(strategyId) {
      // 运行策略的逻辑
      console.log('运行策略:', strategyId)
      // 这里可以调用API运行策略
      alert(`正在运行策略 ${strategyId}`)
    },
    viewStrategy(strategyId) {
      // 查看策略详情的逻辑
      console.log('查看策略详情:', strategyId)
      alert(`查看策略 ${strategyId} 详情`)
    },
    deleteStrategy(strategyId) {
      // 删除策略的逻辑
      console.log('删除策略:', strategyId)
      if (confirm('确定要删除这个策略吗？')) {
        this.strategies = this.strategies.filter(strategy => strategy.id !== strategyId)
        alert('策略已删除')
      }
    },
    addStrategy() {
      // 添加策略的逻辑
      if (!this.newStrategy.name || !this.newStrategy.description) {
        alert('请填写策略名称和描述')
        return
      }
      
      const newId = Math.max(...this.strategies.map(s => s.id)) + 1
      const now = new Date().toISOString().split('T')[0]
      
      const strategy = {
        id: newId,
        ...this.newStrategy,
        created_at: now,
        updated_at: now
      }
      
      this.strategies.push(strategy)
      this.resetForm()
      alert('策略已添加')
    },
    resetForm() {
      this.newStrategy = {
        name: '',
        description: '',
        type: 'LightGBM_Alpha158',
        config_path: '',
        status: 'active'
      }
    }
  }
}
</script>

<style scoped>
.strategies {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.strategies-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.strategy-card {
  background-color: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  transition: all 0.3s ease;
}

.strategy-card:hover {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transform: translateY(-5px);
}

.strategy-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.strategy-name {
  margin: 0;
  color: #2c3e50;
  font-size: 1.2rem;
}

.strategy-status {
  padding: 3px 8px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
}

.strategy-status.active {
  background-color: #27ae60;
  color: white;
}

.strategy-status.inactive {
  background-color: #f39c12;
  color: white;
}

.strategy-status.deprecated {
  background-color: #e74c3c;
  color: white;
}

.strategy-description {
  color: #666;
  margin-bottom: 15px;
  line-height: 1.4;
}

.strategy-meta {
  background-color: white;
  padding: 15px;
  border-radius: 6px;
  margin-bottom: 15px;
  border: 1px solid #e0e0e0;
}

.meta-item {
  margin-bottom: 8px;
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

.strategy-actions {
  display: flex;
  gap: 10px;
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

.add-strategy-section {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
}

.add-strategy-section h3 {
  margin-bottom: 20px;
  color: #2c3e50;
}

.add-strategy-form {
  max-width: 800px;
}

.form-row {
  display: flex;
  gap: 20px;
  margin-bottom: 15px;
}

.form-group {
  flex: 1;
}

.form-group.full-width {
  flex: 100%;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
  color: #2c3e50;
  font-weight: 500;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  font-size: 0.9rem;
}

.form-group textarea {
  height: 80px;
  resize: vertical;
}

.form-actions {
  display: flex;
  gap: 10px;
  margin-top: 20px;
}

@media (max-width: 768px) {
  .strategies-grid {
    grid-template-columns: 1fr;
  }
  
  .strategy-actions {
    flex-direction: column;
  }
  
  .form-row {
    flex-direction: column;
  }
}
</style>