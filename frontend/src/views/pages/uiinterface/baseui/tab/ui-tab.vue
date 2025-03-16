<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
    <!-- Page Wrapper -->
    <div class="page-wrapper">
      <div class="content container-fluid">
        <div class="page-header">
          <div class="content-page-header">
            <h5>Tabs</h5>
          </div>
        </div>
        <!-- Tabs -->
        <basictab></basictab>
        <linetab></linetab>
        <bottomtab></bottomtab>
        <solidtab></solidtab>
        <roundtab></roundtab>
        <!-- /Tabs -->
      </div>
    </div>
    <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Tabs",
    };
  },
};
</script>
