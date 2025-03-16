<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Text Editor</h5>
        </div>
      </div>
      <div class="row">
        <!-- Editor -->
        <div class="col-md-12">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Editor</h5>
            </div>
            <div class="card-body">
              <editor v-model="content" />
            </div>
          </div>
        </div>
        <!-- /Editor -->
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
import Editor from "@tinymce/tinymce-vue";
export default {
  components: {
    editor: Editor,
  },
  data() {
    return {
      title: "Dashboard",
      content: "Description",
    };
  },
  name: "text-editor",
};
</script>
