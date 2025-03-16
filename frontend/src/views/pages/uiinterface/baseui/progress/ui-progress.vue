<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Progress</h5>
        </div>
      </div>
      <!-- Progress -->
      <largeprogress></largeprogress>

      <defaultprogress></defaultprogress>

      <mediumprogress></mediumprogress>

      <smallprogress></smallprogress>

      <extrasmallprogress></extrasmallprogress>
      <!-- /Progress -->
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Progress",
    };
  },
  mounted() { },
};
</script>
