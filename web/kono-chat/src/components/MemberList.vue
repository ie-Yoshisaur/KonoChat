<template>
  <div class="member-list">
      <template v-for="member in memberList" :key="member.id">
          <div class="all">
            <p>
              Name : {{ member.name }}
            </p>
            <p>
              Hobby : {{ member.hobby }}
            </p>
            <p>
              HomeTown : {{ member.homeTown }}
            </p>
            <p>
              Role : {{ member.role }}
            </p>
          </div>
          <div class="line">
            <p>
              {{member.hoge}}
            </p>
          </div>
      </template>
  </div>
</template>

<script lang="ts">
import {
  defineComponent,
} from 'vue';
import Member from '../types/Member';

export default defineComponent({
  name: 'MemberList',
  setup() {
    const memberList: Member[] = [
      {
        id: 1,
        name: 'Taro Asahina',
        hobby: 'soccer',
        homeTown: 'Miyazaki',
        role: 'Web development with vue',
        hoge: '--------------------------------------',
      },
      {
        id: 2,
        name: 'Yugo Nishimura',
        hobby: 'Clash Royale',
        homeTown: 'Chiba',
        role: 'Linking API servers to machine learning models',
        hoge: '--------------------------------------',
      },
      {
        id: 3,
        name: 'Takeru Naito',
        hobby: 'Biological observation',
        homeTown: 'Okinawa',
        role: 'Machine learning',
        hoge: '--------------------------------------',
      },
      {
        id: 4,
        name: 'Yoshisaur',
        hobby: 'Watching movies and animes, Studying English, programming',
        homeTown: 'Hokkaido',
        role: 'Tech lead',
        hoge: '--------------------------------------',
      },
      {
        id: 5,
        name: 'Moe Asato',
        hobby: 'Karaoke, Dance coaching',
        homeTown: 'Okinawa',
        role: 'Scraping Twitter',
        hoge: '--------------------------------------',
      },
      {
        id: 6,
        name: 'Ryoya Gibo',
        hobby: 'Karaoke, Playing game and bowling ',
        homeTown: 'Okinawa',
        role: 'Load balancing of API servers',
        hoge: '--------------------------------------',
      },
    ];

    return {
      memberList,
    };
  },
});
</script>

<style scoped>
  .chat {
    @apply h-full w-full;
  }
  .all > p {
    @apply text-white;
  }
  .line{
    color: #26A69A;
  }
</style>
