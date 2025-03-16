<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Accordions</h5>
        </div>
      </div>
      <div class="row">
        <default></default>
        <!-- end col -->

        <justified></justified>
        <!-- end col -->
      </div>
      <!-- end row -->

      <div class="row">
        <verticalleft></verticalleft>
        <!-- end col -->

        <verticalright></verticalright>
        <!-- end col -->
      </div>
      <!-- end row -->

      <div class="row">
        <bordered></bordered>
        <!-- end col -->

        <borderedjustified></borderedjustified>
        <!-- end col -->
      </div>
      <!-- end row -->

      <div class="row">
        <vakal></vakal>
        <!-- end col -->

        <questions></questions>
      </div>
      <!-- end row -->
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Accordions",
    };
  },
};
</script>
