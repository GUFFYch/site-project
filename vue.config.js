const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  publicPath: process.env.NODE_ENV === 'production' ? '/site-project/' : '/',
  transpileDependencies: [
    'vuetify'
  ]
})


// module.exports = {
//   publicPath: process.env.NODE_ENV === "production" ? "/site-project/" : "/",
// };