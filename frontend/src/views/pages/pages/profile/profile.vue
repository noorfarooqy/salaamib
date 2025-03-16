<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="row justify-content-lg-center">
        <div class="col-lg-10">
          <div class="page-header">
            <div class="content-page-header">
              <h5>Profile</h5>
            </div>
          </div>

          <profilecontent />

          <div class="row">
            <profiletable />

            <profiletable1 />
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  setup() {
    return {
      title: "Profile",
    };
  },
};
</script>
