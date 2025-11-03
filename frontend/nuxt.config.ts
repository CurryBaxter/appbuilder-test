// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: true,
  modules: ['@pinia/nuxt'],
  css: ['@pharen/ui/dist/style.css'],
  build: {
    transpile: ['@pharen/ui']
  }
})
