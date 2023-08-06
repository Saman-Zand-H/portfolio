const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    devServer: {
        proxy: {
            '^/api': {
                target: `http://${process.env.VUE_APP_BACKEND_HOST}:8000`,
                ws: true,
                changeOrigin: true
            },
            '^/graphql': {
                target: `http://${process.env.VUE_APP_BACKEND_HOST}:8000`,
                ws: true,
                changeOrigin: true
            }
        }
    }
})