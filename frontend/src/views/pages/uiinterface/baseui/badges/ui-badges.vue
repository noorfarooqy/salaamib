<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>

  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Badges</h5>
        </div>
      </div>
      <badgesone></badgesone>
      <pillbadges></pillbadges>
      <gradientbadges></gradientbadges>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Badges",
    };
  },
};
</script>
