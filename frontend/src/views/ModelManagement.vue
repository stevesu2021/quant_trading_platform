<template>
  <div class="model-management">
    <div class="models-grid">
      <div class="model-card" v-for="model in models" :key="model.id">
        <div class="model-header">
          <h3 class="model-name">{{ model.name }}</h3>
          <span class="model-status" :class="model.status">
            {{ model.status === 'trained' ? '已训练' : model.status === 'training' ? '训练中' : '未训练' }}
          </span>
        </div>
        <div class="model-description">{{ model.description }}</div>
        <div class="model-meta">
          <div class="meta-item">
            <span class="meta-label">类型：</span>
            <span class="meta-value">{{ model.type }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">训练时间：</span>
            <span class="meta-value">{{ model.trained_at || '未训练' }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">准确率：</span>
            <span class="meta-value">{{ model.accuracy ? `${model.accuracy}%` : '未训练' }}</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">F1分数：</span>
            <span class="meta-value">{{ model.f1_score || '未训练' }}</span>
          </div>
        </div>
        <div class="model-actions">
          <button class="btn btn-primary" @click="trainModel(model.id)">训练模型</button>
          <button class="btn btn-secondary" @click="deployModel(model.id)">部署模型</button>
          <button class="btn btn-danger" @click="deleteModel(model.id)">删除</button>
        </div>
      </div>
    </div>
    
    <div class="add-model-section">
      <h3>添加新模型</h3>
      <div class="add-model-form">
        <div class="form-row">
          <div class="form-group">
            <label for="model-name">模型名称</label>
            <input type="text" id="model-name" v-model="newModel.name" placeholder="输入模型名称" />
          </div>
          <div class="form-group">
            <label for="model-type">模型类型</label>
            <select id="model-type" v-model="newModel.type">
              <option value="LightGBM">LightGBM</option>
              <option value="XGBoost">XGBoost</option>
              <option value="RandomForest">RandomForest</option>
              <option value="SVM">SVM</option>
              <option value="NeuralNetwork">神经网络</option>
            </select>
          </div>
        </div>
        <div class="form-row">
          <div class="form-group full-width">
            <label for="model-description">模型描述</label>
            <textarea id="model-description" v-model="newModel.description" placeholder="输入模型描述"></textarea>
          </div>
        </div>
        <div class="form-actions">
          <button class="btn btn-primary" @click="addModel">添加模型</button>
          <button class="btn btn-secondary" @click="resetForm">重置</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ModelManagement',
  data() {
    return {
      models: [
        {
          id: 1,
          name: 'LightGBM_Alpha158',
          description: '基于LightGBM的Alpha158因子模型',
          type: 'LightGBM',
          status: 'trained',
          trained_at: '2023-06-15',
          accuracy: 78.5,
          f1_score: 0.76
        },
        {
          id: 2,
          name: 'XGBoost_Alpha158',
          description: '基于XGBoost的Alpha158因子模型',
          type: 'XGBoost',
          status: 'trained',
          trained_at: '2023-06-14',
          accuracy: 77.2,
          f1_score: 0.75
        },
        {
          id: 3,
          name: 'RandomForest_Alpha158',
          description: '基于随机森林的Alpha158因子模型',
          type: 'RandomForest',
          status: 'trained',
          trained_at: '2023-06-13',
          accuracy: 75.8,
          f1_score: 0.73
        },
        {
          id: 4,
          name: 'NeuralNetwork_Alpha158',
          description: '基于神经网络的Alpha158因子模型',
          type: 'NeuralNetwork',
          status: 'training',
          trained_at: null,
          accuracy: null,
          f1_score: null
        },
        {
          id: 5,
          name: 'SVM_Alpha158',
          description: '基于SVM的Alpha158因子模型',
          type: 'SVM',
          status: 'untrained',
          trained_at: null,
          accuracy: null,
          f1_score: null
        }
      ],
      newModel: {
        name: '',
        description: '',
        type: 'LightGBM'
      }
    }
  },
  methods: {
    trainModel(modelId) {
      // 训练模型的逻辑
      console.log('训练模型:', modelId)
      alert(`正在训练模型 ${modelId}`)
    },
    deployModel(modelId) {
      // 部署模型的逻辑
      console.log('部署模型:', modelId)
      alert(`正在部署模型 ${modelId}`)
    },
    deleteModel(modelId) {
      // 删除模型的逻辑
      console.log('删除模型:', modelId)
      if (confirm('确定要删除这个模型吗？')) {
        this.models = this.models.filter(model => model.id !== modelId)
        alert('模型已删除')
      }
    },
    addModel() {
      // 添加模型的逻辑
      if (!this.newModel.name || !this.newModel.description) {
        alert('请填写模型名称和描述')
        return
      }
      
      const newId = Math.max(...this.models.map(m => m.id)) + 1
      
      const model = {
        id: newId,
        ...this.newModel,
        status: 'untrained',
        trained_at: null,
        accuracy: null,
        f1_score: null
      }
      
      this.models.push(model)
      this.resetForm()
      alert('模型已添加')
    },
    resetForm() {
      this.newModel = {
        name: '',
        description: '',
        type: 'LightGBM'
      }
    }
  }
}
</script>

<style scoped>
.model-management {
  background-color: white;
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.models-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.model-card {
  background-color: #f8f9fa;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 20px;
  transition: all 0.3s ease;
}

.model-card:hover {
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  transform: translateY(-5px);
}

.model-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.model-name {
  margin: 0;
  color: #2c3e50;
  font-size: 1.2rem;
}

.model-status {
  padding: 3px 8px;
  border-radius: 12px;
  font-size: 0.75rem;
  font-weight: 500;
}

.model-status.trained {
  background-color: #27ae60;
  color: white;
}

.model-status.training {
  background-color: #f39c12;
  color: white;
}

.model-status.untrained {
  background-color: #95a5a6;
  color: white;
}

.model-description {
  color: #666;
  margin-bottom: 15px;
  line-height: 1.4;
}

.model-meta {
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

.model-actions {
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

.add-model-section {
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
}

.add-model-section h3 {
  margin-bottom: 20px;
  color: #2c3e50;
}

.add-model-form {
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
  .models-grid {
    grid-template-columns: 1fr;
  }
  
  .model-actions {
    flex-direction: column;
  }
  
  .form-row {
    flex-direction: column;
  }
}
</style>