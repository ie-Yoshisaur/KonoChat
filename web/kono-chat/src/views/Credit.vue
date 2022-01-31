<template>
  <div class="credit">
    <MemberList />

  </div>
</template>

<script>
import MemberList from '../components/MemberList.vue';

export default {
  name: 'Credit',
  components: {
    MemberList,
  },
};
</script>

<style scoped>
  .credit {
    @apply h-5/6;
  }
</style>
