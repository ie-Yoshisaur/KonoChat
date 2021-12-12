<template>
  <div class="chat">
    <div class="message-list">
      <template v-for="n in store.getters.messageList.length" :key="n">
        <p> {{ store.getters.messageList[n - 1].sender }} </p>
        <p> {{ store.getters.messageList[n - 1].message }} </p>
      </template>
    </div>
    <div class="send-message">
      <input v-model="messageToSend" class="send-input" placeholder="Please enter the text you want to send to Kono-Sensei">
      <button v-on:click='buttonAction' class="send-button">
        <font>Send</font>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useStore } from 'vuex';

export default defineComponent({
  name: 'Chat',
  setup() {
    const store = useStore();
    const messageToSend = ref<string>('');

    const buttonAction = () => {
      store.dispatch('addUserMessage', messageToSend.value);
      store.dispatch('getKonoMessage', { route: 'test', message: 'Hello, World!' });
    };

    return {
      store, messageToSend, buttonAction,
    };
  },
});
</script>

<style scoped>
  .chat {
    @apply h-full w-full;
  }
  .message-list {
    @apply overflow-auto h-full w-5/6 container mx-auto
           border-white border-t-4 border-r-4 border-b-2 border-l-4 rounded-t-lg;
  }
  .send-message {
    @apply h-12 w-5/6 flex justify-around container mx-auto
           border-white border-t-2 border-r-4 border-b-4 border-l-4 rounded-b-2xl;
  }
  .send-input {
    @apply w-4/6 h-full border-r-4 border-l-4 text-center text-white bg-gray-900;
  }
  .send-button {
    @apply w-1/6 h-full border-r-4 border-l-4 text-white font-bold sm:text-base md:text-lg lg:text-xl xl:text-2xl 2xl:text-3xl bg-gray-800;
  }
</style>
