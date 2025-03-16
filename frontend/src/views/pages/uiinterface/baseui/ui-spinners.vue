<template>
  <layout-header></layout-header>
  <layout-sidebar></layout-sidebar>
  
  <!-- Page Wrapper -->
  <div class="page-wrapper">
    <div class="content container-fluid">
      <div class="page-header">
        <div class="content-page-header">
          <h5>Spinner</h5>
        </div>
      </div>
      <div class="row">
        <div class="col-lg-6">
          <div class="card">
            <div class="card-body card-buttons">
              <h4 class="mt-0 header-title">Border spinner</h4>
              <p class="mb-4">
                Use the border spinners for a lightweight loading indicator.
              </p>
              <b-spinner label="Loading..." class="m-2"></b-spinner>
            </div>
            <!--end card-body card-buttons-->
          </div>
          <!--end card-->
        </div>
        <!-- end col -->

        <div class="col-lg-6">
          <div class="card">
            <div class="card-body card-buttons">
              <h4 class="mt-0 header-title">Growing spinner</h4>
              <p class="mb-4">
                If you don’t fancy a border spinner, switch to the grow spinner. While
                it doesn’t technically spin, it does repeatedly grow!
              </p>
              <b-spinner type="grow" label="Loading..."></b-spinner>
            </div>
            <!--end card-body card-buttons-->
          </div>
          <!--end card-->
        </div>
        <!-- end col -->
      </div>
      <!-- end row -->

      <div class="row">
        <div class="col-lg-6">
          <div class="card">
            <div class="card-body card-buttons">
              <h4 class="mt-0 header-title">Colors</h4>
              <p class="mb-4">
                You can use any of our text color utilities on the standard spinner.
              </p>
              <b-spinner v-for="variant in variants" :variant="variant" :key="variant" class="m-2"></b-spinner>
            </div>
            <!--end card-body card-buttons-->
          </div>
          <!--end card-->
        </div>
        <!-- end col -->

        <div class="col-lg-6">
          <div class="card">
            <div class="card-body card-buttons">
              <h4 class="mt-0 header-title">Color Growing spinner</h4>
              <p class="mb-4">Here it is in blue, along with the supported variants.</p>
              <b-spinner v-for="variant in variants" :variant="variant" :key="variant" type="grow"
                class="m-2"></b-spinner>
            </div>
            <!--end card-body card-buttons-->
          </div>
          <!--end card-->
        </div>
        <!-- end col -->
      </div>
      <!-- end row -->

      <div class="row">
        <div class="col-lg-6">
          <div class="card">
            <div class="card-body card-buttons">
              <h4 class="mt-0 header-title">Alignment</h4>
              <p class="mb-4">
                Use flexbox utilities, float utilities, or text alignment utilities to
                place spinners exactly where you need them in any situation.
              </p>
              <div class="d-flex justify-content-center">
                <b-spinner label="Loading..."></b-spinner>
              </div>
            </div>
            <!--end card-body card-buttons-->
          </div>
          <!--end card-->
        </div>
        <!-- end col -->

        <div class="col-lg-6">
          <div class="card">
            <div class="card-body card-buttons">
              <h4 class="mt-0 header-title">Placement</h4>
              <p class="mb-4">
                Use <code>flexbox utilities</code>, <code>float utilities</code>, or
                <code>text alignment</code> utilities to place spinners exactly where
                you need them in any situation.
              </p>
              <div class="d-flex align-items-center">
                <strong>Loading...</strong>
                <b-spinner label="Loading..." class="ms-auto"></b-spinner>
              </div>
            </div>
            <!--end card-body card-buttons-->
          </div>
          <!--end card-->
        </div>
        <!-- end col -->
      </div>
      <!-- end row -->

      <div class="row">
        <div class="col-lg-6">
          <div class="card">
            <div class="card-body card-buttons">
              <h4 class="mt-0 header-title">Size</h4>
              <p class="mb-4">
                Add <code>.spinner-border-sm</code> and
                <code>.spinner-border.avatar-**</code>
                to make a smaller spinner that can quickly be used within other
                components.
              </p>
              <div class="row">
                <div class="col-lg-6">
                  <b-spinner label="Large Spinner" class="avatar-lg text-primary m-2"></b-spinner>
                  <b-spinner type="grow" label="Large Spinner" class="avatar-lg text-secondary m-2"></b-spinner>
                </div>
                <!-- end col -->

                <div class="col-lg-6">
                  <b-spinner label="Large Spinner" class="avatar-md text-primary m-2"></b-spinner>
                  <b-spinner type="grow" label="Large Spinner" class="avatar-md text-secondary m-2"></b-spinner>
                </div>
                <!-- end col -->

                <div class="col-lg-6">
                  <b-spinner label="Large Spinner" class="avatar-sm text-primary m-2"></b-spinner>
                  <b-spinner type="grow" label="Large Spinner" class="avatar-sm text-secondary m-2"></b-spinner>
                </div>
                <!-- end col -->

                <div class="col-lg-6">
                  <b-spinner small label="Small Spinner" class="m-2"></b-spinner>
                  <b-spinner small label="Small Spinner" type="grow" class="m-2"></b-spinner>
                </div>
                <!-- end col -->
              </div>
              <!--end row-->
            </div>
            <!--end card-body card-buttons-->
          </div>
          <!--end card-->
        </div>
        <!-- end col -->

        <div class="col-lg-6">
          <div class="card">
            <div class="card-body card-buttons">
              <h4 class="mt-0 header-title">Buttons spinner</h4>
              <p class="mb-4">
                Use spinners within buttons to indicate an action is currently
                processing or taking place. You may also swap the text out of the
                spinner element and utilize button text as needed.
              </p>
              <div class="row">
                <div class="col-md-6">
                  <div class="button-list mb-1 mb-sm-0">
                    <b-button variant="primary me-1" disabled>
                      <b-spinner class="spinner-border-sm"></b-spinner>
                    </b-button>
                    <b-button variant="primary" disabled>
                      <b-spinner class="spinner-border-sm me-1"></b-spinner>
                      Loading...
                    </b-button>
                  </div>
                </div>
                <!-- end col -->
                <div class="col-md-6">
                  <div class="button-list">
                    <b-button variant="primary me-1" disabled>
                      <b-spinner type="grow" class="spinner-grow-sm"></b-spinner>
                    </b-button>
                    <b-button variant="primary" disabled>
                      <b-spinner type="grow" class="spinner-grow-sm me-1"></b-spinner>
                      Loading...
                    </b-button>
                  </div>
                </div>
                <!-- end col -->
              </div>
              <!-- end row -->
            </div>
            <!--end card-body card-buttons-->
          </div>
          <!--end card-->
        </div>
        <!-- end col -->
      </div>
      <!-- end row -->
    </div>
  </div>
  <!-- /Page Wrapper -->
</template>
<script>
export default {
  data() {
    return {
      title: "Spinner",
      variants: [
        "primary",
        "secondary",
        "success",
        "danger",
        "warning",
        "info",
        "light",
        "dark",
        "blue",
        "pink",
      ],
    };
  },
};
</script>
