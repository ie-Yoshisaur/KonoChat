import { createStore } from 'vuex';
import Message from '@/types/Message';

export type State = { messageList: Message[] }

const state: State = { messageList: [] };

export const store = createStore({
  state,
  mutations: {
  },
  actions: {
  },
  getters: {
  },
});
