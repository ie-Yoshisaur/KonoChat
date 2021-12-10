<template>
  <div class="kono-chat">
    <KonoChatTitle />
    <Chat />
  </div>
</template>

<script>
import KonoChatTitle from '@/components/KonoChatTitle.vue';
import Chat from '@/components/Chat.vue';

export default {
  name: 'Kono-Chat',
  components: {
    KonoChatTitle,
    Chat,
  },
};
</script>

<style scoped>
  .kono-chat {
    @apply h-5/6;
  }
</style>
