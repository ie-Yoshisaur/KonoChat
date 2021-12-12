<template>
  <div class="chat">
    <div ref="messageList" class="message-list">
      <template v-for="n in store.getters.messageList.length" :key="n">
        <div v-bind:class="{'sender-kono': store.getters.messageList[n - 1].sender == 'Kono', 'sender-you': store.getters.messageList[n - 1].sender == 'You'}">
          <p> {{ store.getters.messageList[n - 1].sender }} </p>
        </div>
        <div v-bind:class="{'message-kono': store.getters.messageList[n - 1].sender == 'Kono', 'message-you': store.getters.messageList[n - 1].sender == 'You'}">
          <p> {{ store.getters.messageList[n - 1].message }} </p>
        </div>
      </template>
    </div>
    <div class="send-message">
      <input v-model='messageToSend'
             v-on:keypress.enter='buttonAction'
             class="send-input"
             placeholder="Type text.">
      <button v-on:click='buttonAction' class="send-button">
        <font>Send</font>
      </button>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, onUpdated, nextTick, } from 'vue';
import { useStore } from 'vuex';

export default defineComponent({
  name: 'Chat',
  setup() {
    const store = useStore();
    const messageToSend = ref<string>('');
    const messageList = ref<HTMLImageElement>();
    let messageListLength: number = 0;

    const buttonAction = () => {
      if (messageToSend.value) {
        store.dispatch('addUserMessage', messageToSend.value);
        store.dispatch('getKonoMessage', { route: 'test', message: messageToSend.value });
        messageToSend.value = '';
      }
    };

    onUpdated(() => {
      nextTick(() => {
        if (!messageList.value) return;
        if (messageListLength.value != store.getters.messageList.length) {
          messageListLength = store.getters.messageList.length;
          messageList.value.scrollTop = messageList.value.scrollHeight;
        }
      });
    });

    return {
      store, messageToSend, messageList, buttonAction,
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
  .sender-you {
    @apply flex justify-end;
  }
  .sender-you > p {
    @apply pt-2 pr-2 text-left text-white;
  }
  .message-you {
    @apply flex justify-end;
  }
  .message-you > p {
    @apply p-2 max-w-full inline-flex bg-white text-black break-all text-left rounded-tl-2xl rounded-tr-sm rounded-bl-2xl rounded-br-2xl;
  }
  .sender-kono {
    @apply flex justify-start;
  }
  .sender-kono > p {
    @apply pt-2 pl-2 text-left text-white;
  }
  .message-kono {
    @apply flex justify-start;
  }
  .message-kono > p {
    @apply p-2 max-w-full inline-flex bg-gray-300 text-black break-all text-left rounded-tl-sm rounded-tr-2xl rounded-bl-2xl rounded-br-2xl;
  }
  .send-message {
    @apply h-12 w-5/6 flex justify-around container mx-auto
           border-white border-t-2 border-r-4 border-b-4 border-l-4 rounded-b-2xl;
  }
  .send-input {
    @apply w-4/6 h-full border-r-4 border-l-4 rounded-lg text-center text-white bg-gray-900;
  }
  .send-button {
    @apply w-1/6 h-full border-r-4 border-l-4 rounded-lg text-white font-bold
           sm:text-base md:text-lg lg:text-xl xl:text-2xl 2xl:text-3xl;
  }
</style>
