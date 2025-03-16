<template>
  <div class="row">
    <div class="col-xxl-12">
      <div class="card">
        <div class="card-header align-items-center d-flex">
          <h4 class="card-title mb-0">Gradient Badges</h4>
        </div>
        <!-- end card header -->

        <div class="card-body">
          <p class="text-muted">
            Use the <code>badge-gradient-*</code> class to create a gradient styled badge.
          </p>
          <div class="d-flex flex-wrap gap-2">
            <span class="badge badge-gradient-primary">Primary</span>
            <span class="badge badge-gradient-secondary">Secondary</span>
            <span class="badge badge-gradient-success">Success</span>
            <span class="badge badge-gradient-danger">Danger</span>
            <span class="badge badge-gradient-warning">Warning</span>
            <span class="badge badge-gradient-info">Info</span>
            <span class="badge badge-gradient-dark">Dark</span>
          </div>
        </div>
        <!-- end card-body -->
      </div>
      <!-- end card -->
    </div>
    <!--end col-->
  </div>

  <div class="row">
    <div class="col-xxl-6">
      <div class="card">
        <div class="card-header align-items-center d-flex">
          <h4 class="card-title mb-0">Button Position Badges</h4>
        </div>
        <!-- end card header -->

        <div class="card-body">
          <p class="text-muted">
            Use the below utilities to modify a badge and position it in the corner of a
            link or button.
          </p>
          <div class="d-flex flex-wrap gap-4">
            <b-button variant="primary position-relative">
              Mails
              <span
                class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-success"
                >+99 <span class="visually-hidden">unread messages</span></span
              >
            </b-button>
            <b-button variant="light position-relative">
              Alerts
              <span
                class="position-absolute top-0 start-100 translate-middle badge border border-light rounded-circle bg-danger p-1"
                ><span class="visually-hidden">unread messages</span></span
              >
            </b-button>
            <b-button variant="primary position-relative p-0 avatar-xs rounded">
              <span class="avatar-title bg-transparent">
                <i class="fas fa-envelope"></i>
              </span>
              <span
                class="position-absolute top-0 start-100 translate-middle badge border border-light rounded-circle bg-danger p-1"
                ><span class="visually-hidden">unread messages</span></span
              >
            </b-button>
            <b-button variant="light position-relative p-0 avatar-xs rounded-circle">
              <span class="avatar-title bg-transparent text-reset">
                <i class="fas fa-bell"></i>
              </span>
            </b-button>
            <b-button variant="light position-relative p-0 avatar-xs rounded-circle">
              <span class="avatar-title bg-transparent text-reset">
                <i class="fas fa-bars"></i>
              </span>
              <span
                class="position-absolute top-0 start-100 translate-middle badge border border-light rounded-circle bg-success p-1"
                ><span class="visually-hidden">unread messages</span></span
              >
            </b-button>
          </div>
        </div>
        <!-- end card-body -->
      </div>
      <!-- end card -->
      <div class="card">
        <div class="card-header align-items-center d-flex">
          <h4 class="card-title mb-0">Badges With Button</h4>
        </div>
        <!-- end card header -->
        <div class="card-body">
          <p class="text-muted">
            Badges can be used as part of buttons to provide a counter.
          </p>
          <div class="d-flex flex-wrap gap-2">
            <b-button variant="primary">
              Notifications <span class="badge bg-success ms-1">4</span>
            </b-button>
            <b-button variant="success">
              Messages <span class="badge bg-danger ms-1">2</span>
            </b-button>
            <b-button variant="outline-secondary">
              Draft <span class="badge bg-success ms-1">2</span>
            </b-button>
          </div>
        </div>
        <!-- end card-body -->
      </div>
      <!-- end card -->
    </div>
    <div class="col-xxl-6">
      <div class="card">
        <div class="card-header align-items-center d-flex">
          <h4 class="card-title mb-0">Badges with Heading</h4>
        </div>
        <!-- end card header -->
        <div class="card-body">
          <p class="text-muted">Example of the badge used in the HTML Heading.</p>
          <div>
            <h1>Example heading <b-badge>New</b-badge></h1>
            <h2>Example heading <b-badge>New</b-badge></h2>
            <h3>Example heading <b-badge>New</b-badge></h3>
            <h4>Example heading <b-badge>New</b-badge></h4>
            <h5>Example heading <b-badge>New</b-badge></h5>
            <h6 class="mb-0">Example heading <b-badge>New</b-badge></h6>
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
