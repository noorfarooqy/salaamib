<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Offcanvas</h5>
        </div>
      </div>
      <div class="row">
        <div class="col-xl-6">
          <offcanvasone></offcanvasone>
          <!-- end card-->

          <placement></placement>
          <!-- end card-->
        </div>
        <!-- end col-->
        <backdrop></backdrop>
        <!-- end col-->
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Offcanvas",
    };
  },
};
</script>
