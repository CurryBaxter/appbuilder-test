// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  modules: [
    '@nuxtjs/tailwindcss',
    '@pinia/nuxt'
  ],
  build: {
    transpile: ['@pharen/ui']
  },
  vite: {
    optimizeDeps: {
      include: ['@pharen/ui']
    }
  }
})
