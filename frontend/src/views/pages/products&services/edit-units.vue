<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="content-page-header">
        <h5>Edit Unit</h5>
      </div>
      <div class="row">
        <div class="col-md-12">
          <div class="card-body">
            <div class="form-group-item border-0 pb-0">
              <div class="row">
                <div class="col-lg-4 col-md-6 col-sm-12">
                  <div class="form-group">
                    <label>Name <span class="text-danger">*</span></label>
                    <input type="text" class="form-control" placeholder="kilogram" />
                  </div>
                </div>
                <div class="col-lg-4 col-md-6 col-sm-12">
                  <div class="form-group">
                    <label>Symbol <span class="text-danger">*</span></label>
                    <input type="text" class="form-control" placeholder="Slung" />
                  </div>
                </div>
                <div class="col-lg-4 col-md-6 col-sm-12">
                  <div class="form-group">
                    <label>Parent Unit <span class="text-danger">*</span></label>
                    <input type="text" class="form-control" placeholder="Kg" />
                  </div>
                </div>
              </div>
            </div>
            <div class="text-end mt-4">
              <router-link to="units" class="btn btn-primary cancel me-2">Cancel</router-link>
              <router-link to="units" class="btn btn-primary">Add Unit</router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
