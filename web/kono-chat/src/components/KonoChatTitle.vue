<template>
  <div class="kono-chat-title">
    <h1> Kono-Chat </h1>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'KonoChatTitle',
});
</script>

<style scoped>
  .kono-chat-title {
    @apply pb-10;
  }
  .kono-chat-title > h1 {
    @apply font-bold text-center text-white text-5xl;
  }
</style>
