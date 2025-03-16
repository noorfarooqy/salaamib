<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Modal</h5>
        </div>
      </div>
      <div class="row">
        <bootstrapmodal></bootstrapmodal>
        <!-- end col -->

        <pagemodals></pagemodals>
        <!-- end col -->
      </div>
      <!-- end row -->

      <div class="row">
        <positionmodal></positionmodal>
        <!-- end col -->

        <modalalert></modalalert>
        <!-- end col -->
      </div>
      <!-- end row -->

      <div class="row">
        <multiplemodal></multiplemodal>
        <!-- end col -->

        <custommodal></custommodal>
        <!-- end col -->
      </div>
      <!-- end row -->

      <staticmodal></staticmodal>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Modal",
    };
  },
};
</script>
