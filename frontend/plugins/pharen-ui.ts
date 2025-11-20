import { defineNuxtPlugin } from '#app'
import * as components from '@pharen/ui'

export default defineNuxtPlugin((nuxtApp) => {
  for (const name in components) {
    nuxtApp.vueApp.component(name, components[name])
  }
})
