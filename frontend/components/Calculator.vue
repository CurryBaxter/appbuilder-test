<template>
  <div>
    <UInput v-model.number="num1" type="number" />
    <UInput v-model.number="num2" type="number" />

    <UButton @click="calculate('+')">+</UButton>
    <UButton @click="calculate('-')">-</UButton>
    <UButton @click="calculate('*')">×</UButton>
    <UButton @click="calculate('/')">÷</UButton>

    <p>Result: {{ result }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const num1 = ref(0)
const num2 = ref(0)
const result = ref(0)

function calculate(operation) {
  switch (operation) {
    case '+':
      result.value = num1.value + num2.value
      break;
    case '-':
      result.value = num1.value - num2.value
      break;
    case '*':
      result.value = num1.value * num2.value
      break;
    case '/':
      if (num2.value === 0) {
        result.value = NaN
      } else {
        result.value = num1.value / num2.value
      }
      break;
  }
}
</script>
