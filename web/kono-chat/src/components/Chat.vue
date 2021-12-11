<template>
  <div class="chat">
    <div class="message-list">
    </div>
    <div class="send-button">
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Chat',
});
</script>

<style scoped>
  .chat {
    @apply h-full w-full;
  }
  .message-list {
    @apply h-full w-5/6 bg-gray-700 container mx-auto;
  }
  .send-button {
    @apply h-10 w-5/6 bg-gray-100 container mx-auto;
  }
</style>
