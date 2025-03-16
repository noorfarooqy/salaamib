<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Button Group</h5>
        </div>
      </div>
      <!-- Button Group -->
      <div class="row">
        <div class="col-md-6">
          <div class="card card-buttons">
            <div class="card-header">
              <h5 class="card-title">Horizontal</h5>
            </div>
            <div class="card-body">
              <div class="btn-group">
                <b-button variant="primary">Left</b-button>
                <b-button variant="primary">Middle</b-button>
                <b-button variant="primary">Right</b-button>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card card-buttons">
            <div class="card-header">
              <h5 class="card-title">Input Group</h5>
            </div>
            <div class="card-body">
              <div class="btn-group">
                <b-button variant="primary">1</b-button>
                <b-button variant="primary">2</b-button>
                <b-button variant="primary">3</b-button>
                <b-button variant="primary">4</b-button>
              </div>
            </div>
          </div>
        </div>
        <div class="col-md-6">
          <div class="card card-buttons">
            <div class="card-header">
              <h5 class="card-title">Vertical</h5>
            </div>
            <div class="card-body">
              <div class="btn-group">
                <b-button-group vertical>
                  <b-button variant="primary">Button</b-button>
                  <b-button-group>
                    <button id="btngroupverticaldrop1" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown"
                      aria-expanded="false">
                      Dropdown
                    </button>
                    <div class="dropdown-menu" aria-labelledby="btngroupverticaldrop1">
                      <a class="dropdown-item" href="javascript:;">Dropdown link</a>
                      <a class="dropdown-item" href="javascript:;">Dropdown link</a>
                    </div>
                  </b-button-group>
                  <b-button variant="primary">Button</b-button>
                  <b-button variant="primary">Button</b-button>
                  <b-button-group>
                    <button id="btngroupverticaldrop2" class="btn btn-primary dropdown-toggle" data-bs-toggle="dropdown"
                      aria-expanded="false">
                      Dropdown
                    </button>
                    <div class="dropdown-menu" aria-labelledby="btngroupverticaldrop2">
                      <a class="dropdown-item" href="javascript:;">Dropdown link</a>
                      <a class="dropdown-item" href="javascript:;">Dropdown link</a>
                    </div>
                  </b-button-group>
                </b-button-group>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- /Button group-->
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Button Group",
    };
  },
};
</script>
