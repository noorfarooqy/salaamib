<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Basic Tables</h5>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-6">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Basic Table</h5>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <b-table :items="tableitems"></b-table>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-6">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Striped Rows</h5>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <b-table striped hover :items="tableitems" class="mb-0"></b-table>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="row">
        <div class="col-lg-6">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Bordered Table</h5>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <b-table bordered :items="tableitems" class="mb-0"></b-table>
              </div>
            </div>
          </div>
        </div>
        <div class="col-lg-6">
          <div class="card">
            <div class="card-header">
              <h5 class="card-title">Hover Rows</h5>
            </div>
            <div class="card-body">
              <div class="table-responsive">
                <b-table hover :items="tableitems" class="mb-0"></b-table>
              </div>
            </div>
          </div>
        </div>
      </div>

      <contexttable />
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Basic Tables",
      tableitems: [
        { firstname: "John", lastname: "Doe", email: "john@example.com" },
        { firstname: "Mary", lastname: "Moe", email: "mary@example.com" },
        { firstname: "July", lastname: "Dooley", email: "july@example.com" },
      ],
    };
  },
};
</script>
