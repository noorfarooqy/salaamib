<template>
  <div class="page-header">
    <div class="content-page-header">
      <h5>{{ title }}</h5>
    </div>
  </div>
</template>
<script>
export default {
  components: {},
  props: {
    title: {
      type: String,
      default: "",
    },
  },
};
</script>
