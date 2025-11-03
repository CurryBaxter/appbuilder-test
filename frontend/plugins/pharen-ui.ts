import { defineNuxtPlugin } from '#app'
import * as components from '@pharen/ui'

export default defineNuxtPlugin((nuxtApp) => {
  for (const key in components) {
    nuxtApp.vueApp.component(key, components[key])
  }
})
