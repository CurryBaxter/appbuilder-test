<template>
  <div>
    <p-input v-model.number="num1" type="number" />
    <p-input v-model.number="num2" type="number" />
    <p>
      Result: {{ result }}
    </p>
    <p-button @click="operate('+')">+</p-button>
    <p-button @click="operate('-')">-</p-button>
    <p-button @click="operate('*')">×</p-button>
    <p-button @click="operate('/')">÷</p-button>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const num1 = ref(0);
const num2 = ref(0);
const operation = ref('+');

const result = computed(() => {
  switch (operation.value) {
    case '+':
      return num1.value + num2.value;
    case '-':
      return num1.value - num2.value;
    case '*':
      return num1.value * num2.value;
    case '/':
      if (num2.value === 0) return 'Cannot divide by zero';
      return num1.value / num2.value;
    default:
      return 0;
  }
});

const operate = (op) => {
  operation.value = op;
};
</script>
