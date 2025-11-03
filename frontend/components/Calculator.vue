<template>
  <div class="calculator">
    <PInput v-model.number="num1" type="number" placeholder="Number 1" />
    <PInput v-model.number="num2" type="number" placeholder="Number 2" />
    <div class="buttons">
      <PButton @click="operate('+')">+</PButton>
      <PButton @click="operate('-')">-</PButton>
      <PButton @click="operate('*')">×</PButton>
      <PButton @click="operate('/')">÷</PButton>
    </div>
    <p>Result: {{ result }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const num1 = ref(0);
const num2 = ref(0);
const result = ref(0);

const operate = (operator) => {
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
        result.value = 'Cannot divide by zero';
      } else {
        result.value = num1.value / num2.value;
      }
      break;
    default:
      result.value = 'Invalid operator';
  }
};
</script>

<style scoped>
.calculator {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

.buttons {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}
</style>
