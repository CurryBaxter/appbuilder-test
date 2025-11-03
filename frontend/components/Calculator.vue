<template>
  <div class="calculator">
    <div class="input-group">
      <label for="num1">Number 1:</label>
      <input type="number" id="num1" v-model.number="num1">
    </div>
    <div class="input-group">
      <label for="num2">Number 2:</label>
      <input type="number" id="num2" v-model.number="num2">
    </div>

    <div class="buttons">
      <button @click="operate('+')">+</button>
      <button @click="operate('-')">-</button>
      <button @click="operate('*')">×</button>
      <button @click="operate('/')">÷</button>
    </div>

    <div class="result">
      Result: {{ result }}
    </div>
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

.input-group {
  margin-bottom: 10px;
}

label {
  margin-right: 10px;
}

.buttons {
  margin-bottom: 10px;
}

button {
  margin: 5px;
  padding: 5px 10px;
}

.result {
  font-weight: bold;
}
</style>
