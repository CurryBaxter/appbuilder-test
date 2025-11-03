<template>
  <div>
    <input type="number" v-model.number="num1" />
    <input type="number" v-model.number="num2" />
    <br />
    <button @click="operate('+')">+</button>
    <button @click="operate('-')">-</button>
    <button @click="operate('*')">×</button>
    <button @click="operate('/')">÷</button>
    <br />
    Result: {{ result }}
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const num1 = ref(0)
const num2 = ref(0)
const operation = ref('')

const result = ref(0)

const operate = (op) => {
  operation.value = op
  switch (op) {
    case '+':
      result.value = num1.value + num2.value
      break
    case '-':
      result.value = num1.value - num2.value
      break
    case '*':
      result.value = num1.value * num2.value
      break
    case '/':
      result.value = num1.value / num2.value
      break
  }
}
</script>
