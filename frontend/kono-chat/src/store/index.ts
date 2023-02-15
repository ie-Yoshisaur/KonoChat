import axios from 'axios';
import { createStore } from 'vuex';
import Message from '@/types/Message';

axios.defaults.baseURL = process.env.VUE_APP_BASE_URL;

export type State = { messageList: Message[] }

const state: State = { messageList: [] };

export const store = createStore({
  state,
  mutations: {
    /* eslint no-shadow: ["error", { "allow": ["state"] }] */
    addUserMessage(state: State, message: string) {
      const messageObj: Message = {
        sender: 'You',
        message,
      };
      state.messageList.push(messageObj);
    },
    /* eslint no-shadow: ["error", { "allow": ["state"] }] */
    addKonoMessage(state: State, message: string) {
      const messageObj: Message = {
        sender: 'Kono',
        message,
      };
      state.messageList.push(messageObj);
    },
  },
  actions: {
    addUserMessage({ commit }, message) {
      commit('addUserMessage', message);
    },
    getKonoMessage({ commit }, message) {
      /* eslint-disable-next-line */
      axios.post('/api/reply', { message: message }).then((response) => {
        commit('addKonoMessage', JSON.parse(JSON.stringify(response.data)).message);
      });
    },
  },
  getters: {
    /* eslint no-shadow: ["error", { "allow": ["state"] }] */
    messageList(state: State) {
      return state.messageList;
    },
  },
});
