<template>
  <div class="row">
    <div class="col-xxl-6">
      <div class="card">
        <div class="card-header align-items-center d-flex">
          <h4 class="card-title mb-0">Default Badges</h4>
        </div>
        <!-- end card header -->

        <div class="card-body">
          <p class="text-muted">
            Use the <code>badge</code> class to set a default badge.
          </p>
          <div class="d-flex flex-wrap gap-2">
            <b-badge variant="primary">Primary</b-badge>
            <b-badge variant="secondary">Secondary</b-badge>
            <b-badge variant="success">Success</b-badge>
            <b-badge variant="info text-light">Info</b-badge>
            <b-badge variant="warning text-light">Warning</b-badge>
            <b-badge variant="danger">Danger</b-badge>
            <b-badge variant="dark">Dark</b-badge>
            <b-badge variant="light text-dark">Light</b-badge>
          </div>
        </div>
        <!-- end card-body -->
      </div>
      <!-- end card -->
    </div>
    <div class="col-xxl-6">
      <div class="card">
        <div class="card-header align-items-center d-flex">
          <h4 class="card-title mb-0">Soft Badges</h4>
        </div>
        <!-- end card header -->
        <div class="card-body">
          <p class="text-muted">
            Use the <code>badge-soft-</code> class with below-mentioned variation to
            create softer badge.
          </p>
          <div class="d-flex flex-wrap gap-2">
            <span class="badge badge-soft-primary">Primary</span>
            <span class="badge badge-soft-secondary">Secondary</span>
            <span class="badge badge-soft-success">Success</span>
            <span class="badge badge-soft-info">Info</span>
            <span class="badge badge-soft-warning">Warning</span>
            <span class="badge badge-soft-danger">Danger</span>
            <span class="badge badge-soft-dark">Dark</span>
            <span class="badge badge-soft-light text-dark">Light</span>
          </div>
        </div>
        <!-- end card-body -->
      </div>
      <!-- end card -->
    </div>
  </div>
  <div class="row">
    <div class="col-xxl-6">
      <div class="card">
        <div class="card-header align-items-center d-flex">
          <h4 class="card-title mb-0">Outline Badges</h4>
        </div>
        <!-- end card header -->
        <div class="card-body">
          <p class="text-muted">
            Use the <code>badge-outline-</code> class with the below-mentioned variation
            to create a badge with the outline.
          </p>
          <div class="d-flex flex-wrap gap-2">
            <a href="javascript:;" class="badge badge-outline-primary">Primary</a>
            <span class="badge badge-outline-secondary">Secondary</span>
            <span class="badge badge-outline-success">Success</span>
            <span class="badge badge-outline-info">Info</span>
            <span class="badge badge-outline-warning">Warning</span>
            <span class="badge badge-outline-danger">Danger</span>
            <span class="badge badge-outline-dark">Dark</span>
            <span class="badge badge-outline-light text-dark">Light</span>
          </div>
        </div>
        <!-- end card-body -->
      </div>
      <!-- end card -->
    </div>

    <div class="col-xxl-6">
      <div class="card">
        <div class="card-header align-items-center d-flex">
          <h4 class="card-title mb-0">Rounded Pill Badges</h4>
        </div>
        <!-- end card header -->

        <div class="card-body">
          <p class="text-muted">
            Use the <code>rounded-pill</code> class to make badges more rounded with a
            larger border-radius.
          </p>
          <div class="d-flex flex-wrap gap-2">
            <b-badge pill variant="primary">Primary</b-badge>
            <b-badge pill variant="secondary">Secondary</b-badge>
            <b-badge pill variant="success">Success</b-badge>
            <b-badge pill variant="info text-light">Info</b-badge>
            <b-badge pill variant="warning text-light">Warning</b-badge>
            <b-badge pill variant="danger">Danger</b-badge>
            <b-badge pill variant="dark">Dark</b-badge>
            <b-badge pill variant="light text-dark">Light</b-badge>
          </div>
        </div>
        <!-- end card-body -->
      </div>
      <!-- end card -->
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>
