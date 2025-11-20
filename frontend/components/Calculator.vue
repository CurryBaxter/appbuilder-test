<template>
  <div>
    <label>Number 1:</label>
    <input type="number" v-model.number="num1" />
    <br />
    <label>Number 2:</label>
    <input type="number" v-model.number="num2" />
    <br />
    <PhButton @click="calculate('+')">+</PhButton>
    <PhButton @click="calculate('-')">-</PhButton>
    <PhButton @click="calculate('*')">×</PhButton>
    <PhButton @click="calculate('/')">÷</PhButton>
    <br />
    Result: {{ result }}
  </div>
</template>

<script setup>
import { ref } from 'vue';

const num1 = ref(0);
const num2 = ref(0);
const result = ref(0);

function calculate(operation) {
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
}
</script>
