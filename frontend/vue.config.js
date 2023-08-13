const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    pages: {
        index: {
            title: 'SamanZND',
            entry: "src/main.ts"
        }
    },
    devServer: {
        proxy: {
            '^/api': {
                target: `http://172.17.0.1:8000`,
                ws: true,
                changeOrigin: true
            },
            '^/graphql': {
                target: `http://172.17.0.1:8000`,
                ws: true,
                changeOrigin: true
            },
            '^/rss': {
                target: `http://172.17.0.1:8000`,
                ws: true,
                changeOrigin: true
            },
        }
    },
    chainWebpack (config) {
        config.module.rule('pdf')
            .test(/\.pdf$/)
            .use('file-loader')
            .loader('file-loader')
    }
})