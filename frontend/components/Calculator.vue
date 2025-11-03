<template>
  <div>
    <PhInput v-model.number="num1" type="number" placeholder="Number 1" />
    <PhInput v-model.number="num2" type="number" placeholder="Number 2" />
    <div class="buttons">
      <PhButton @click="operate('+')">+</PhButton>
      <PhButton @click="operate('-')">-</PhButton>
      <PhButton @click="operate('*')">×</PhButton>
      <PhButton @click="operate('/')">÷</PhButton>
    </div>
    <p>Result: {{ result }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const num1 = ref(0)
const num2 = ref(0)
const result = ref(0)

const operate = (operation) => {
  switch (operation) {
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
      if (num2.value === 0) {
        result.value = 'Division by zero!'
      } else {
        result.value = num1.value / num2.value
      }
      break
    default:
      result.value = 'Invalid operation'
  }
}
</script>
