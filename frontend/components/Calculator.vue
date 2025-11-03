<template>
  <div class="flex flex-col items-center">
    <input v-model.number="num1" type="number" class="border p-2 mb-2">
    <input v-model.number="num2" type="number" class="border p-2 mb-4">
    <div class="flex gap-2">
      <button @click="operate('+')" class="px-4 py-2 bg-blue-500 text-white rounded">+</button>
      <button @click="operate('-')" class="px-4 py-2 bg-blue-500 text-white rounded">-</button>
      <button @click="operate('*')" class="px-4 py-2 bg-blue-500 text-white rounded">×</button>
      <button @click="operate('/')" class="px-4 py-2 bg-blue-500 text-white rounded">÷</button>
    </div>
    <p class="mt-4">Result: {{ result }}</p>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const num1 = ref(0);
const num2 = ref(0);
const result = ref(0);

function operate(operator: string) {
  switch (operator) {
    case '+':
      result.value = num1.value + num2.value;
      break;
    case '-':
      result.value = num1.value - num2.value;
      break;
    case '*':
      result.value = num1.value * num2.value;
      break;
    case '/':
      if (num2.value === 0) {
        result.value = NaN;
      } else {
        result.value = num1.value / num2.value;
      }
      break;
  }
}
</script>
