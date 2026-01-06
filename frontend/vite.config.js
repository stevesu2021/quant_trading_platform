const { defineConfig } = require('vite')
const vue2 = require('@vitejs/plugin-vue2')

// https://vitejs.dev/config/
module.exports = defineConfig({
  plugins: [vue2()],
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true
      }
    }
  }
})
