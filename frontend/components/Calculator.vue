<template>
  <div>
    <input type="number" v-model.number="num1" />
    <input type="number" v-model.number="num2" />
    <br />
    <button @click="add">+</button>
    <button @click="subtract">-</button>
    <button @click="multiply">×</button>
    <button @click="divide">÷</button>
    <br />
    Result: {{ result }}
  </div>
</template>

<script setup>
import { ref } from 'vue';

const num1 = ref(0);
const num2 = ref(0);
const result = ref(0);

const add = () => {
  result.value = num1.value + num2.value;
};

const subtract = () => {
  result.value = num1.value - num2.value;
};

const multiply = () => {
  result.value = num1.value * num2.value;
};

const divide = () => {
  if (num2.value === 0) {
    result.value = NaN;
  } else {
    result.value = num1.value / num2.value;
  }
};
</script>
