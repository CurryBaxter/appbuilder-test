<template>
  <div>
    <input type="number" v-model.number="num1" />
    <input type="number" v-model.number="num2" />
    <div>
      <button @click="operate('+')">+</button>
      <button @click="operate('-')">-</button>
      <button @click="operate('*')">×</button>
      <button @click="operate('/')">÷</button>
    </div>
    <div>Result: {{ result }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const num1 = ref(0);
const num2 = ref(0);
const result = ref(0);

const operate = (operation) => {
  switch (operation) {
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
      result.value = num1.value / num2.value;
      break;
  }
};
</script>
