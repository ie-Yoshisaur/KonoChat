<template>
  <div class="credits">
    <MemberList />

  </div>
</template>

<script>
import MemberList from '../components/MemberList.vue';

export default {
  name: 'Credits',
  components: {
    MemberList,
  },
};
</script>

<style scoped>
  .credits {
    @apply h-5/6;
  }
</style>
