<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <allblogheader :title="title" :text="text" />
      <!-- Search Filter -->
      <div id="filter_inputs" class="card filter-card">
        <div class="card-body pb-0">
          <div class="row">
            <div class="col-sm-6 col-md-3">
              <div class="form-group">
                <label>Name</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="form-group">
                <label>Email</label>
                <input type="text" class="form-control" />
              </div>
            </div>
            <div class="col-sm-6 col-md-3">
              <div class="form-group">
                <label>Phone</label>
                <input type="text" class="form-control" />
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Search Filter -->

      <!-- Blogs-->
      <div class="card invoices-tabs-card">
        <div class="invoices-main-tabs">
          <div class="row align-items-center">
            <div class="col-lg-12">
              <div class="invoices-tabs">
                <ul>
                  <li>
                    <router-link to="all-blogs" class="active">Active Blog</router-link>
                  </li>
                  <li><router-link to="inactive-blog">Inactive Blog</router-link></li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Blogs-->

      <blog-list></blog-list>
    </div>
  </div>
  <!-- /Page Wrapper -->

  <allblogmodel></allblogmodel>
</template>
<script>
export default {
  components: {},
  data() {
    return {
      title: "Blog",
      text: "Add Blog",
    };
  },
};
</script>
