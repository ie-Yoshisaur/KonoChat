<template>
  <div class="chat">
    <div class="message-list">
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
    @apply h-5/6 w-5/6 container mx-auto bg-gray-700;
  }
  .message-list {
  }
</style>
