<template>
  <div class="container">
    <div class="animate three">
      <span>W</span><span>e</span><span>l</span><span>c</span><span>o</span><span>m</span><span>e</span>
      <br>
      <span>T</span><span>o</span>
      <br>
      <span>K</span><span>o</span><span>n</span><span>o</span><span>-</span><span>C</span><span>h</span><span>a</span><span>t</span>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'Home',
});
</script>
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Lato:100,100i,300,300i,400,400i,700,700i,900,900i');

  *
  {
    margin: 0;
    padding: 0;
  }

  body
  {
    font-family: 'Lato', sans-serif;
    font-size: 14px;
    color: #999999;
    word-wrap:break-word;
  }

  p
  {
    margin: 0 0 10px;
  }

  ul
  {
    list-style: none;
  }

  .container {
    width: 100%;
    margin: auto;
    font-weight: 900;
    text-transform: uppercase;
    text-align: center;
    padding: 0 0 200px;
  }

  a, a:link, a:visited {
    text-decoration: none;
    padding: 9px 15px;
    border: 1px solid #ececec;
    border-radius: 5px;
    color: gray;
  }
  .animate {
    font-size: 50px;
    margin: 100px 0 0;
    border-bottom: 2px solid #ccc;
  }

  .animate span {
    display: inline-block;
  }
  .animate span:nth-of-type(2) {
    animation-delay: .05s;
  }
  .animate span:nth-of-type(3) {
    animation-delay: .1s;
  }
  .animate span:nth-of-type(4) {
    animation-delay: .15s;
  }
  .animate span:nth-of-type(5) {
    animation-delay: .2s;
  }
  .animate span:nth-of-type(6) {
    animation-delay: .25s;
  }
  .animate span:nth-of-type(7) {
    animation-delay: .3s;
  }
  .animate span:nth-of-type(8) {
    animation-delay: .35s;
  }
  .animate span:nth-of-type(9) {
    animation-delay: .4s;
  }
  .animate span:nth-of-type(10) {
    animation-delay: .45s;
  }
  .animate span:nth-of-type(11) {
    animation-delay: .5s;
  }
  .animate span:nth-of-type(12) {
    animation-delay: .55s;
  }
  .animate span:nth-of-type(13) {
    animation-delay: .6s;
  }
  .animate span:nth-of-type(14) {
    animation-delay: .65s;
  }
  .animate span:nth-of-type(15) {
    animation-delay: .7s;
  }
  .animate span:nth-of-type(16) {
    animation-delay: .75s;
  }
  .animate span:nth-of-type(17) {
    animation-delay: .8s;
  }
  .animate span:nth-of-type(18) {
    animation-delay: .85s;
  }
  .animate span:nth-of-type(19) {
    animation-delay: .9s;
  }
  .animate span:nth-of-type(20) {
    animation-delay: .95s;
  }

.three span {
  font-size: 10vw;
  color: #26A69A;
  opacity: 0;
  transform: translate(-300px, 0) scale(0);
  animation: sideSlide .5s forwards;
}

@keyframes sideSlide {
  60% {
    transform: translate(20px, 0) scale(1);
    color: #26A69A;
  }

  80% {
    transform: translate(20px, 0) scale(1);
    color: #26A69A;
  }

  99% {
    transform: translate(0) scale(1.2);
    color: #00f0ff;
  }

  100% {
    transform: translate(0) scale(1);
    opacity: 1;
    color: #26A69A;
  }
}
</style>
