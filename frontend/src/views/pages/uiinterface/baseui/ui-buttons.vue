<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Buttons</h5>
        </div>
      </div>
      <!-- Buttons -->
      <div class="card card-buttons">
        <div class="card-body">
          <h5 class="card-title">Default Button</h5>
          <b-button variant="primary me-1">Primary</b-button>
          <b-button variant="secondary me-1">Secondary</b-button>
          <b-button variant="success me-1">Success</b-button>
          <b-button variant="danger me-1">Danger</b-button>
          <b-button variant="warning me-1">Warning</b-button>
          <b-button variant="info me-1">Info</b-button>
          <b-button variant="light me-1">Light</b-button>
          <b-button variant="dark me-1">Dark</b-button>
          <b-button class="btn-link">Link</b-button>
          <hr />
          <h5 class="card-title">Button Sizes</h5>
          <p>
            <b-button variant="primary btn-lg me-1">Primary</b-button>
            <b-button variant="secondary btn-lg me-1">Secondary</b-button>
            <b-button variant="success btn-lg me-1">Success</b-button>
            <b-button variant="danger btn-lg me-1">Danger</b-button>
            <b-button variant="warning btn-lg me-1">Warning</b-button>
            <b-button variant="info btn-lg me-1">Info</b-button>
            <b-button variant="light btn-lg me-1">Light</b-button>
            <b-button variant="dark btn-lg">Dark</b-button>
          </p>
          <p>
            <b-button variant="primary me-1">Primary</b-button>
            <b-button variant="secondary me-1">Secondary</b-button>
            <b-button variant="success me-1">Success</b-button>
            <b-button variant="danger me-1">Danger</b-button>
            <b-button variant="warning me-1">Warning</b-button>
            <b-button variant="info me-1">Info</b-button>
            <b-button variant="light me-1">Light</b-button>
            <b-button variant="dark">Dark</b-button>
          </p>
          <p>
            <b-button size="sm" variant="primary me-1">Primary</b-button>
            <b-button size="sm" variant="secondary me-1">Secondary</b-button>
            <b-button size="sm" variant="success me-1">Success</b-button>
            <b-button size="sm" variant="danger me-1">Danger</b-button>
            <b-button size="sm" variant="warning me-1">Warning</b-button>
            <b-button size="sm" variant="info me-1">Info</b-button>
            <b-button size="sm" variant="light me-1">Light</b-button>
            <b-button size="sm" variant="dark">Dark</b-button>
          </p>
        </div>
      </div>
      <!-- Rounded Button -->
      <div class="card card-buttons">
        <div class="card-header">
          <h5 class="card-title">Rounded Button</h5>
          <p class="card-text">
            use <code>.btn-rounded</code> in class <code>.btn</code> class to get
            Rounded button
          </p>
        </div>
        <div class="card-body">
          <b-button pill variant="primary me-1">Primary</b-button>
          <b-button pill variant="secondary me-1">Secondary</b-button>
          <b-button pill variant="success me-1">Success</b-button>
          <b-button pill variant="danger me-1">Danger</b-button>
          <b-button pill variant="warning me-1">Warning</b-button>
          <b-button pill variant="info me-1">Info</b-button>
          <b-button pill variant="light me-1">Light</b-button>
          <b-button pill variant="dark">Dark</b-button>
          <hr />
          <p>
            use <code>.btn-rounded</code> in class <code>.btn-outline-*</code> class to
            get Rounded Outline button
          </p>
          <b-button pill variant="outline-primary me-1">Primary</b-button>
          <b-button pill variant="outline-secondary me-1">Secondary</b-button>
          <b-button pill variant="outline-success me-1">Success</b-button>
          <b-button pill variant="outline-danger me-1">Danger</b-button>
          <b-button pill variant="outline-warning me-1">Warning</b-button>
          <b-button pill variant="outline-info me-1">Info</b-button>
          <b-button pill variant="outline-light me-1">Light</b-button>
          <b-button pill variant="outline-dark">Dark</b-button>
        </div>
      </div>
      <!-- /Rounded Button -->

      <!-- Outline Buttons -->
      <div class="card card-buttons">
        <div class="card-header">
          <h5 class="card-title">Outline Buttons</h5>
          <p class="card-text">
            Use <code>.btn-outline-*</code> class for outline buttons.
          </p>
        </div>
        <div class="card-body">
          <div class="row row-sm align-items-center">
            <div class="col-12 col-xl mb-3 mb-xl-0">Normal</div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-primary btn-block">Primary</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-secondary btn-block">Secondary</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-success btn-block">Success</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-warning btn-block">Warning</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-danger btn-block">Danger</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-info btn-block">Info</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-light btn-block">Light</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-dark btn-block">Dark</b-button>
            </div>
          </div>
          <div class="row row-sm align-items-center mt-3">
            <div class="col-12 col-xl mb-3 mb-xl-0">Active</div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-primary btn-block active">Primary</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-secondary btn-block active">Secondary</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-success btn-block active">Success</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-warning btn-block active">Warning</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-danger btn-block active">Danger</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-info btn-block active">Info</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-light btn-block active">Light</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button variant="outline-dark btn-block active">Dark</b-button>
            </div>
          </div>
          <div class="row row-sm align-items-center mt-3">
            <div class="col-12 col-xl mb-3 mb-xl-0">Disabled</div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button disabled variant="outline-primary btn-block">Primary</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button disabled variant="outline-secondary btn-block">Secondary</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button disabled variant="outline-success btn-block">Success</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button disabled variant="outline-warning btn-block">Warning</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button disabled variant="outline-danger btn-block">Danger</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button disabled variant="outline-info btn-block">Info</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button disabled variant="outline-light btn-block">Light</b-button>
            </div>
            <div class="col-6 col-sm-4 col-md-2 col-xl mb-3 mb-xl-0">
              <b-button disabled variant="outline-dark btn-block">Dark</b-button>
            </div>
          </div>
        </div>
      </div>
      <!-- /Outline Buttons -->

      <!-- Progress Button -->
      <div class="pb-1">
        <div class="card mb-4">
          <div class="card-header">
            <h5 class="card-title">Progress Button</h5>
          </div>
          <div class="card-body bg-white">
            <b-button variant="primary me-1"><span class="spinner-border spinner-border-sm me-2"
                role="status"></span>Primary</b-button>
            <b-button variant="secondary me-1"><span class="spinner-border spinner-border-sm me-2"
                role="status"></span>Secondary</b-button>
            <b-button variant="success me-1"><span class="spinner-border spinner-border-sm me-2"
                role="status"></span>Success</b-button>
            <b-button variant="danger me-1"><span class="spinner-border spinner-border-sm me-2"
                role="status"></span>Danger</b-button>
            <b-button variant="warning me-1"><span class="spinner-border spinner-border-sm me-2"
                role="status"></span>Warning</b-button>
            <b-button variant="info me-1"><span class="spinner-border spinner-border-sm me-2"
                role="status"></span>Info</b-button>
            <b-button variant="dark me-1"><span class="spinner-border spinner-border-sm me-2"
                role="status"></span>Dark</b-button>
          </div>
        </div>
      </div>
      <!-- /Progress Button -->
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Buttons",
    };
  },
};
</script>
